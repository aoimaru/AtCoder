# coding: utf-8
# Your code here!

def extract(comp, visited=None, route=None, vis=None):
    print()
    if not visited:
        visited = set()
    visited.add(comp)
    print("visited", visited)
    
    if not vis:
        vis = []
    if not comp in vis:
        vis.append(comp)
    
    if not route:
        route = []
    route.append(comp)
    
    next_cnd = []
    for cnd in Graph[comp]:
        if not cnd in visited:
            next_cnd.append(cnd)
    print("next_cnd", next_cnd)
    print("comp", comp)
    print("route", route)
    print("vis", vis)
    if not next_cnd:
        if comp == 1:
            return
        else:
            com = 0
            for ids, vi in enumerate(vis):
                if vi == comp:
                    com = ids
            extract(vis[com-1],  visited, route, vis)
    else:
        next_comp = min(next_cnd)
        extract(next_comp, visited, route, vis)

def main():
    N = int(input())
    global Graph
    Graph = {}
    for _ in range(N-1):
        A, B = map(int, input().split())
        if not A in Graph:
            Graph[A] = []
        Graph[A].append(B)
        if not B in Graph:
            Graph[B] = []
        Graph[B].append(A)
    
    extract(1)
        
        
        
        
        
if __name__ == "__main__":
    main()