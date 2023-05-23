#include <iostream>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

// function for BFS
void BFS(vector<vector<int>>& graph, int start) {
    vector<bool> visited(graph.size(), false);
    queue<int> q;
    visited[start] = true;
    q.push(start);
    cout << "BFS Traversal: ";
    while (!q.empty()) {
        int curr = q.front();
        q.pop();
        cout << curr << " ";
        for (int i = 0; i < graph[curr].size(); i++) {
            int next = graph[curr][i];
            if (!visited[next]) {
                visited[next] = true;
                q.push(next);
            }
        }
    }
    cout << endl;
}

// function for DFS
void DFS(vector<vector<int>>& graph, int start) {
    vector<bool> visited(graph.size(), false);
    stack<int> s;
    visited[start] = true;
    s.push(start);
    cout << "DFS Traversal: ";
    while (!s.empty()) {
        int curr = s.top();
        s.pop();
        cout << curr << " ";
        for (int i = 0; i < graph[curr].size(); i++) {
            int next = graph[curr][i];
            if (!visited[next]) {
                visited[next] = true;
                s.push(next);
            }
        }
    }
    cout << endl;
}

int main() {
    int n, m;
    cout << "Enter the number of vertices and edges: ";
    cin >> n >> m;

    vector<vector<int>> graph(n);
    int u, v;
    cout << "Enter the edges: ";
    for (int i = 0; i < m; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int start;
    cout << "Enter the starting vertex: ";
    cin >> start;

    BFS(graph, start);
    DFS(graph, start);

    return 0;
}
