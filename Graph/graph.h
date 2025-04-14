
#ifndef GRAPH_H
#define GRAPH_H

#include <string>
#include <vector>

struct City {
    int id;
    std::string name;
    int population;
    int elevation;
};

struct Edge {
    int to;
    int distance;
};

#endif
