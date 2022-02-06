# coding: utf-8
# Your code here!

# 深さ優先探索を実践, 結果RE

import sys

Memo = set()

def DFS(S, T, visited=None):
    if not visited:
        visited = set()
    if S in visited:
        return 0
    visited.add(S)
    if S == T:
        return 1
    if not Graph[S]:
        return 0
    comp = 0
    for nt in Graph[S]:
        Memo.add((S, nt))
        comp += DFS(nt, T, visited)
    
    return comp
        
def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        sys.exit()
    for cnt in range(1, N+1):
        Memo.add((cnt, cnt))
    global Graph
    Graph = {}
    for _ in range(M):
        A, B = map(int, input().split())
        if not A in Graph:
            Graph[A] = []
        Graph[A].append(B)
        Memo.add((A, B))
        
    init = len(Memo)
    Ans = 0
    for S in range(1, N+1):
        for T in range(1, N+1):
            if (S, T) in Memo:
                continue
            ans = DFS(S, T)
            if ans == 1:
                Ans += 1
    ans = DFS(1, 4)
    print(Ans+init)
    
        
        
            
if __name__ == "__main__":
    main()