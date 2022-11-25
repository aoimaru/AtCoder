# coding: utf-8
# Your code here!

def rec(depth, memo, flag):
    if depth == N:
        return len([tk for tk in memo.values() if tk == K])
    c_memo = memo.copy()
    if flag == 1:
        for tk in SN[depth]:
            if tk in c_memo:
                c_memo[tk] += 1
            else:
                c_memo[tk] = 1
    return max(rec(depth+1, c_memo, 1), rec(depth+1, c_memo, 0))
        
def main():
    global N, K
    N, K = map(int, input().split())
    global SN
    SN = list()
    for _ in range(N):
        SN.append(input())
    
    ans = max(rec(0, dict(), 1), rec(0, dict(), 0))
    print(ans)


if __name__ == "__main__":
    main()