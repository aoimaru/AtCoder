# coding: utf-8
# Your code here!

import itertools

def DFS(F, cnt, visited=None):
    if F == G:
        global RT
        RT = cnt
        return
    if visited is None:
        visited = set()
    visited.add(F)
    for T in Graph[F]:
        if T in visited:
            continue
        cnt += Edge[(F, T)]
        DFS(T, cnt, visited)

def BFS(comps):
    flag = 0
    for comp in comps:
        if comp[-1] == G:
            flag = 1
    if flag == 1:
        global RT
        RT = comps
        return
    args = []
    for comp in comps:
        S = comp[-1]
        # print(comp)
        # print("S", S)
        for T in Graph[S]:
            if not T in comp:
                arg = comp+[T]
                args.append(arg)
    BFS(args)        
    
        
def main():
    N = int(input())
    global Graph
    Graph = {}
    global Edge
    Edge = {}
    for _ in range(N-1):
        U, V, W = map(int, input().split())
        print(U, V, W)
        if not U in Graph:
            Graph[U] = []
        Graph[U].append(V)
        if not V in Graph:
            Graph[V] = []
        Graph[V].append(U)
        Edge[(U, V)] = W
        Edge[(V, U)] = W
    
    Ns = [num for num in range(1, N+1)]
    combs = itertools.combinations(Ns, 2)

    
    Ans = 0
    for comb in combs:
        if (comb[0], comb[1]) in Edge:
            print(Edge[(comb[0], comb[1])])
            Ans += Edge[(comb[0], comb[1])]
        else:
            global G
            G = comb[1]
            BFS([[comb[0]]])
            # print("RT", RT)
            ans = []
            for rt in RT:
                print(rt)
                Len = len(rt)
                an = 0
                for cnt in range(Len-1):
                    an += Edge[(rt[cnt], rt[cnt+1])]
                ans.append(an)
            Ans += max(ans)
    
    print(Ans)    
                
if __name__ == "__main__":
    main()
