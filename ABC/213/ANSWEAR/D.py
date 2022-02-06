# coding: utf-8
# Your code here!
# おまじない
import sys
sys.setrecursionlimit(300000)

def main():
    Ans = []
    def DFS(crr, pre):
        Ans.append(crr)
        for nxt in Graph[crr]:
            if nxt != pre:
                DFS(nxt, crr)
                Ans.append(crr)
        
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
    
    for dep in Graph:
        Graph[dep].sort()
    
    DFS(1, -1)
    print(*Ans)
     
if __name__ == "__main__":
    main()