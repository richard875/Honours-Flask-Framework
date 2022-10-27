from src.others.dijkstra import dijkstra_test
from src.others.floyd import floyd_test
from src.others.kruskal import kruskal_test
from src.others.prim import prim_test

def main_other():
    dijkstra = dijkstra_test()
    floyd = floyd_test()
    kruskal = kruskal_test()
    prim = prim_test()

    return dijkstra, floyd, kruskal, prim

if __name__ == "__main__":
    main_other()