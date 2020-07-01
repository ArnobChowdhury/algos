class Graph(object):
    def __init__(self, size):
        self.size = size
        self.adj_matrix = []

        i = 0
        while (i < size):
            self.adj_matrix.append([0 for j in range(size)])
            i += 1

    def add_edge(self, v1, v2):
        if (v1 == v2):
            print ('%d and %d are same vertex' % (v1, v2))
            return
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if self.adj_matrix[v1][v2] != 1:
            print('%d and %d do not have an edge' % (v1, v2))
            return
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

g = Graph(5)
g.add_edge(0, 3)
g.add_edge(0, 0)
g.add_edge(1, 3)
print(g.adj_matrix)
g.remove_edge(2, 3)
g.remove_edge(1, 3)
print(g.adj_matrix)
