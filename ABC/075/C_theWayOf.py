# coding: utf-8
# Your code here!
def extract(comps):
    args = []
    flag = 0
    for comp in comps:
        for nx in Graph[comp[-1]]:
            if not nx in comp:
                args.append(comp+[nx])
                flag = 1
    if flag == 0:
        global RT
        RT = comps
        return
    extract(args)
    
def main():
    N, M = map(int, input().split())
    Edges = []
    for _ in range(M):
        Edges.append(list(map(int, input().split())))
    
    for idx in range(len(Edges)):
        Comps = [Edge for ids, Edge in enumerate(Edges) if not ids == idx]
        global Graph
        Graph = {}
        for Comp in Comps:
            A, B = Comp[0], Comp[1]
            if not A in Graph:
                Graph[A] = []
            Graph[A].append(B)
            if not B in Graph:
                Graph[B] = []
            Graph[B].append(A)
        print()
        for key, value in Graph.items():
            print(key, value)
        extract([[Comps[0][0]]])
        print()
        for rt in RT:
            print("rt", rt)
            
        
    
if __name__ == "__main__":
    main()
