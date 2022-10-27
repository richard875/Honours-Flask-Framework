import time
import random

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
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
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        # for u, v, weight in result:
            # print("%d - %d: %d" % (u, v, weight))

def kruskal_test():
    toRet = []
    sides = [400000, 1000000, 2100000]
    for side in sides:
        g = Graph(side)
        for i in range(side):
            g.add_edge(i-1, i, random.randint(0, 20))
        
        start = time.time()
        g.kruskal_algo()
        end = time.time()
        print(f"Time for {side}: " + str(round(end - start, 3)) + "s")
        toRet.append(f"Time for {side}: " + str(round(end - start, 3)) + "s")
    
    return toRet

if __name__ == "__main__":
    kruskal_test()