import sys
import time
import random

def dijkstra(vt, ed):
    visited_and_distance = None
    
    def to_be_visited():
        v = -10
        for index in range(num_of_vertices):
            if visited_and_distance[index][0] == 0 \
                and (v < 0 or visited_and_distance[index][1] <=
                    visited_and_distance[v][1]):
                v = index
        return v
        
    num_of_vertices = len(vt[0])

    visited_and_distance = [[0, 0]]
    for i in range(num_of_vertices-1):
        visited_and_distance.append([0, sys.maxsize])

    for vertex in range(num_of_vertices):

        # Find next vertex to be visited
        to_visit = to_be_visited()
        for neighbor_index in range(num_of_vertices):

            # Updating new distances
            if vt[to_visit][neighbor_index] == 1 and \
                    visited_and_distance[neighbor_index][0] == 0:
                new_distance = visited_and_distance[to_visit][1] \
                    + ed[to_visit][neighbor_index]
                if visited_and_distance[neighbor_index][1] > new_distance:
                    visited_and_distance[neighbor_index][1] = new_distance
            
            visited_and_distance[to_visit][0] = 1

    i = 0
    # Printing the distance
    for distance in visited_and_distance:
        # print("Distance of ", i ," from source vertex: ", distance[1])
        i = i + 1

def dijkstra_test():
    toRet = []
    sides = [2500, 4000, 5800]
    for side in sides:
        vertices = []
        edges = []

        for i in range(side):
            temp1 = []
            temp2 = []
            for j in range(side):
                temp1.append(random.randint(0, 1))
                temp2.append(random.randint(0, 20))
            vertices.append(temp1)
            edges.append(temp2)
        
        start = time.time()
        dijkstra(vertices, edges)
        end = time.time()
        print(f"Time for {side}: " + str(round(end - start, 3)) + "s")
        toRet.append(f"Time for {side}: " + str(round(end - start, 3)) + "s")
    
    return toRet

if __name__ == "__main__":
    dijkstra_test()