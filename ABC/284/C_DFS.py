# coding: utf-8
# Your code here!

def DFS(Cur):
    Nodes[Cur] = True
    if not Cur in Maps:
        return
    for Next in Maps[Cur]:
        if Nodes[Next]:
            continue
        DFS(Next)
        
def main():
    N, M = map(int, input().split())
    
    global Nodes
    Nodes = [False for _ in range(N+1)]
    
    global Maps
    Maps = dict()
    for _ in range(M):
        U, V = map(int, input().split())
        if not U in Maps:
            Maps[U] = list()
        Maps[U].append(V)
        if not V in Maps:
            Maps[V] = list()
        Maps[V].append(U)
    
    Answer = 0
    for Cur in range(1, N+1):
        if not Nodes[Cur]:
            DFS(Cur)
            Answer += 1
    
    print(Answer)

if __name__ == "__main__":
    main()
