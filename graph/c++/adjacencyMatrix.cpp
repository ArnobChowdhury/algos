#include <iostream>
using namespace std;

class Graph
{
private:
    bool **adjMatrix;
    int numVertices;

public:
    Graph(int numVertices)
    {
        this->numVertices = numVertices;
        adjMatrix = new bool *[numVertices];
        for (int i = 0; i < numVertices; i++)
        {
            adjMatrix[i] = new bool[numVertices];
            for (int j = 0; numVertices; j++)
                adjMatrix[i][j] = false;
        }
    }

    void addEdge(int i, int j)
    {
        adjMatrix[i][j] = true;
        adjMatrix[j][i] = true;
    }

    void removeEdge(int i, int j)
    {
        adjMatrix[j][i] = false;
        adjMatrix[i][j] = false;
    }
}