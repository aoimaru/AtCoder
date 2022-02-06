# coding: utf-8
# Your code here!

def BFS(comps, count):
    if count >= N:
        global RT
        RT = comps
        return
    count += 1
    args = []
    for comp in comps:
        for nx in Graph[comp[-1]]:
            if not nx in comp:
                args.append(comp + [nx])
    BFS(args, count)

def main():
    global N
    N, M = map(int, input().split())
    global Graph
    Graph = {}
    for _ in range(M):
        A, B = map(int, input().split())
        if not A in Graph:
            Graph[A] = []
        Graph[A].append(B)
        if not B in Graph:
            Graph[B] = []
        Graph[B].append(A)
    
    BFS([[1]], 1)
    
    ans = 0
    for rt in RT:
        if len(rt) == N:
            ans += 1
    print(ans)
    
if __name__ == "__main__":
    main()