
#include "graph.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>
#include <queue>
#include <limits>
#include <algorithm>

// Define global variables
std::map<int, std::vector<Edge>> graph;
std::map<std::string, City> cityMap;

// Function to read city data from a file
void readCities(const std::string& filename) {
    std::ifstream file(filename);
    if (!file) {
        std::cerr << "Error: Cannot open " << filename << std::endl;
        exit(1);
    }

    std::string line;
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        City city;
        ss >> city.id >> city.name >> city.population >> city.elevation;
        cityMap[city.name] = city;
    }

    file.close();
}

// Function to read road data from a file
void readRoads(const std::string& filename) {
    std::ifstream file(filename);
    if (!file) {
        std::cerr << "Error: Cannot open " << filename << std::endl;
        exit(1);
    }

    std::string line;
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        int from, to, distance;
        ss >> from >> to >> distance;
        graph[from].push_back({to, distance});
    }

    file.close();
}

// Function implementing Dijkstra's Algorithm
std::pair<int, std::vector<int>> dijkstra(int start, int goal) {
    std::map<int, int> distances;
    std::map<int, int> previous;
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<>> pq;

    for (const auto& node : graph) {
        distances[node.first] = std::numeric_limits<int>::max();
    }
    distances[start] = 0;
    pq.push(std::make_pair(0, start));

    while (!pq.empty()) {
        int dist = pq.top().first;
        int current = pq.top().second;
        pq.pop();

        if (current == goal) break;

        for (const auto& edge : graph[current]) {
            int newDist = dist + edge.distance;
            if (newDist < distances[edge.to]) {
                distances[edge.to] = newDist;
                previous[edge.to] = current;
                pq.push(std::make_pair(newDist, edge.to));
            }
        }
    }

    std::vector<int> path;
    int current = goal;
    if (distances[goal] == std::numeric_limits<int>::max()) {
        return { distances[goal], path };
    }

    while (current != start) {
        path.push_back(current);
        if (previous.find(current) == previous.end()) {
            return { distances[goal], {} };
        }
        current = previous[current];
    }
    path.push_back(start);
    std::reverse(path.begin(), path.end());

    return { distances[goal], path };
}
