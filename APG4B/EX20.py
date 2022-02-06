# coding: utf-8
# Your code here!
# 漸化式のイメージを持つ！！
import copy

Ans = {}

def DFS(now):
    if not now in Graph:
        return 1
    time = 1
    for nxt in Graph[now]:
        com = DFS(nxt)
        time += com
        Ans[now] = time
    return time
        
def main():
    N = int(input())
    PN = list(map(int, input().split()))
    global Graph
    Graph = {}
    for cnt, num in enumerate(PN):
        if not num in Graph:
            Graph[num] = []
        Graph[num].append(cnt+1)
    ans = DFS(0)
    outs = copy.copy(Ans)
    nums = [cnt for cnt in range(N)]
    for num in nums:
        if num in outs:
            print(outs[num])
        else:
            print(1)
    
if __name__ == "__main__":
    main()