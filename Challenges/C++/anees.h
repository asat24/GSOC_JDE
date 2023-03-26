#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

char counter = '0';

struct Path {
    int x, y;
    int length;

    static bool compare(const Path& first, const Path& second) {
        return first.length < second.length;
    }
};

const vector<int> dirX = {0, -1, 0, 1, 0};
const vector<int> dirY = {0, 0, -1, 0, 1};

bool outOfBounds(const vector<string>& map, const int i, const int j) {
    return i < 0 || j < 0 || i >= static_cast<int>(map.size()) || j >= static_cast<int>(map[0].length());
}

void DFS(const int x, const int y, vector<string>& map, vector<vector<bool>>& visited) {
    for (int i = 0; i < static_cast<int>(dirX.size()); i++) {
        int tempX = x + dirX[i], tempY = y + dirY[i];
        if (outOfBounds(map, tempX, tempY)) {
            continue;
        }

        if (map[tempX][tempY] == '.' && !visited[tempX][tempY]) {
            visited[tempX][tempY] = true;
            map[tempX][tempY] = counter;
            counter++;
            DFS(tempX, tempY, map, visited);
        }
    }
}

void BFS(const vector<string>& map, vector<Path>& paths) {
    int rows = static_cast<int>(map.size()), cols = static_cast<int>(map[0].length());
    vector<vector<bool>> visited(map.size(), vector<bool>(cols, false));

    queue<pair<int,int>> queue;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (map[i][j] == '#' || visited[i][j]) {
                continue;
            }

            queue.push(make_pair(i, j));
            visited[i][j] = true;
            int length = 0;

            while (!queue.empty()) {
                pair<int,int> top = queue.front();
                queue.pop();
                length++;

                for (int k = 0; k < static_cast<int>(dirX.size()); k++) {
                    int tempX = top.first + dirX[k], tempY = top.second + dirY[k];
                    if (outOfBounds(map, tempX, tempY)) {
                        continue;
                    }

                    if (map[tempX][tempY] == '#' || visited[tempX][tempY]) {
                        continue;
                    }

                    visited[tempX][tempY] = true;
                    queue.push(make_pair(tempX, tempY));
                }
            }

            paths.push_back(Path({i, j, length}));
        }
    }
}

Path getLongestPath(const vector<string>& matrix) {
    vector<Path> paths;
    BFS(matrix, paths);
    sort(paths.begin(), paths.end(), Path::compare);
    return paths.back();
}
