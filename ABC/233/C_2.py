# coding: utf-8
# Your code here!

def DFS(comp, layer):
    if layer == N:
        if comp == X:
            return 1
        else:
            return 0
    ans = 0
    for cnt in LN[layer]:
        ans += DFS(comp*cnt, layer+1)
    return ans
        
def main():
    global N
    global X
    N, X = map(int, input().split())
    global LN
    LN = []
    for _ in range(N):
        LA = list(map(int, input().split()))
        L = LA.pop(0)
        LN.append(LA)
    Ans = DFS(1, 0)
    print(Ans)

if __name__ == "__main__":
    main()