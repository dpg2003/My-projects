
#include "graph.h"
#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Declare the global maps defined in graph.cpp
extern map<string, City> cityMap;

int main() {
    // Replace with your actual file names
    string cityFile = "cities.txt";
    string roadFile = "roads.txt";

    readCities(cityFile);
    readRoads(roadFile);

    string startCity, goalCity;
    cout << "Enter start city name: ";
    cin >> startCity;
    cout << "Enter goal city name: ";
    cin >> goalCity;

    if (cityMap.find(startCity) == cityMap.end() || cityMap.find(goalCity) == cityMap.end()) {
        cerr << "Error: One or both cities not found!" << endl;
        return 1;
    }

    int startID = cityMap[startCity].id;
    int goalID = cityMap[goalCity].id;

    auto [distance, path] = dijkstra(startID, goalID);

    if (path.empty()) {
        cout << "No path found between " << startCity << " and " << goalCity << "." << endl;
    } else {
        cout << "Shortest distance: " << distance << endl;
        cout << "Path: ";
        for (int id : path) {
            for (const auto& pair : cityMap) {
                if (pair.second.id == id) {
                    cout << pair.second.name << " ";
                    break;
                }
            }
        }
        cout << endl;
    }

    return 0;
}
