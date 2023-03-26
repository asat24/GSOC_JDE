#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include "anees.h"

using namespace std;

int main(int argc, char *argv[])
{
    if (argc != 2) {
        cout << "Usage: ./longest_path <input_file>" << endl;
        return 1;
    }

    ifstream file(argv[1]);
    if (!file.is_open()) {
        cout << "Error: could not open file" << endl;
        return 1;
    }

    anees graph;
    graph.readGraph(file);

    file.close();

    pair<int, vector<int>> result = graph.longestPath();
    int longestPathLength = result.first;
    vector<int> longestPath = result.second;

    cout << "Length of longest path: " << longestPathLength << endl;

    cout << "Vertices in longest path: ";
    for (int i = 0; i < longestPath.size(); i++) {
        cout << longestPath[i] << " ";
    }
    cout << endl;

    return 0;
}
