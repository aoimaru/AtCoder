# coding: utf-8
# Your code here!
import sys

def DFS(cnt, comp):
    if cnt == N:
        if comp == X:
            return 1
        return 0
    ans = 0
    for ch in LN[cnt]:
        if comp*ch > X:
            continue
        ans += DFS(cnt+1, comp*ch)
    return ans

def main():
    global N
    global X
    N, X = map(int, input().split())
    global LN
    LN = []
    for _ in range(N):
        L = list(map(int, input().split()))
        L.pop(0)
        LN.append(L)
    ans = DFS(0, 1)
    print(ans)

if __name__ == "__main__":
    main()
