def kruskal_algo(n, l1):    # n=no. of vertex   l1=edge list
    class Graph:
        def __init__(self, vertex):
            self.V = vertex
            self.graph = []

        def add_edge(self, u, v, w):
            self.graph.append([u, v, w])

        def search(self, parent, i):
            if parent[i] == i:
                return i
            return self.search(parent, parent[i])

        def apply_union(self, parent, rank, x, y):
            xroot = self.search(parent, x)
            yroot = self.search(parent, y)
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            else:
                parent[yroot] = xroot
                rank[xroot] += 1

        def kruskal(self):
            result = []
            i, e = 0, 0
            self.graph = sorted(self.graph, key=lambda item: item[2])
            parent = []
            rank = []
            for node in range(self.V):
                parent.append(node)
                rank.append(0)
            while e < self.V - 1:
                u, v, w = self.graph[i]
                i = i + 1
                x = self.search(parent, u)
                y = self.search(parent, v)
                if x != y:
                    e = e + 1
                    result.append([u, v, w])
                    self.apply_union(parent, rank, x, y)
            minimumCost = 0
            for u, v, weight in result:
                minimumCost += weight
            c = minimumCost
            return result, c

    g = Graph(n)
    for u, v, w in l1:
        g.add_edge(u, v, w)
    edge, s = g.kruskal()
    print("Minimum Cost Spanning Tree:-", s)
    return edge