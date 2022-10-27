import time
import random

def floyd_warshall(G, nV, INF):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    # print_solution(distance, nV, INF)


# Printing the solution
def print_solution(distance, nV, INF):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

def floyd_test():
    toRet = []
    INF = 999
    sides = [180, 250, 310]

    for side in sides:
        edges = []
        for i in range(side):
            temp = []
            for j in range(side):
                if random.randint(0, 1) == 0:
                    temp.append(random.randint(0, 20))
                else:
                    temp.append(INF)
            
            edges.append(temp)
        
        # print(edges)
            
        start = time.time()
        floyd_warshall(edges, side, INF)
        end = time.time()
        print(f"Time for {side}: " + str(round(end - start, 3)) + "s")
        toRet.append(f"Time for {side}: " + str(round(end - start, 3)) + "s")
    
    return toRet

if __name__ == "__main__":
    floyd_test()