#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

const int MAX_N = 100;

int n, m;
char labyrinth[MAX_N][MAX_N];
int visited[MAX_N][MAX_N];
int longest_path = 0;

// Possible directions to move
const int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};

// Check if the given coordinates are inside the labyrinth and the cell is a hole.
bool is_valid(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m && labyrinth[x][y] == '.';
}

// DFS to explore all possible paths from (x,y)
void dfs(int x, int y, int length) {
    visited[x][y] = length;
    longest_path = max(longest_path, length);
    for (int i = 0; i < 8; i++) {
        int new_x = x + dx[i];
        int new_y = y + dy[i];
        if (is_valid(new_x, new_y) && visited[new_x][new_y] == 0) {
            dfs(new_x, new_y, length+1);
        }
    }
}

int main() {

    // Read input from file
    ifstream input("input.txt");
    input >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            input >> labyrinth[i][j];
        }
    }
    input.close();
    memcpy(labyrinth, input, sizeof(char) * MAX_N * MAX_N);

    // Find the longest path from the top to the bottom of the labyrinth
    for (int j = 0; j < m; j++) {
        if (labyrinth[0][j] == '.') {
            dfs(0, j, 1);
        }
    }

    // If no path to the bottom was found, return -1
    if (longest_path == 0) {
        cout << "-1" << endl;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cout << labyrinth[i][j];
            }
            cout << endl;
        }
        return 0;
    }

    // Mark the longest path in the labyrinth with the order in which the holes are visited
    int order = 0;
    for (int j = 0; j < m; j++) {
        if (visited[n-1][j] == longest_path) {
            int x = n-1;
            int y = j;
            while (visited[x][y] > 0) {
                labyrinth[x][y] = '0' + order++;
                for (int i = 0; i < 8; i++) {
                    int new_x = x + dx[i];
                    int new_y = y + dy[i];
                    if (is_valid(new_x, new_y) && visited[new_x][new_y] == visited[x][y]-1) {
                        x = new_x;
                        y = new_y;
                    }
            }
        }
    }
}
// Print the length of the longest path and the labyrinth with the marked path
cout << longest_path << endl;
for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
        cout << labyrinth[i][j];
    }
    cout << endl;
}

return 0;
}

