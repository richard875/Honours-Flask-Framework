import time
import random

def prim(ver, gra, sel, noEdge, INF):
    while (noEdge < ver - 1):
        minimum = INF
        x = 0
        y = 0
        for i in range(ver):
            if sel[i]:
                for j in range(ver):
                    if ((not sel[j]) and gra[i][j]):  
                        if minimum > gra[i][j]:
                            minimum = gra[i][j]
                            x = i
                            y = j
        # print(str(x) + "-" + str(y) + ":" + str(gra[x][y]))
        sel[y] = True
        noEdge += 1

def prim_test():
    toRet = []
    INF = 9999999
    sides = [400, 550, 680]
    for side in sides:
        G = []
        selected = [0 for i in range(side)]
        no_edge = 0
        selected[0] = True

        for i in range(side):
            temp = []
            for j in range(side):
                if random.randint(0, 1) == 0:
                    temp.append(0)
                else:
                    temp.append(random.randint(1, 99))
            
            G.append(temp)
        
        # print(G)
        start = time.time()
        prim(side, G, selected, no_edge, INF)
        end = time.time()
        print(f"Time for {side}: " + str(round(end - start, 3)) + "s")
        toRet.append(f"Time for {side}: " + str(round(end - start, 3)) + "s")
    
    return toRet

if __name__ == "__main__":
    prim_test()