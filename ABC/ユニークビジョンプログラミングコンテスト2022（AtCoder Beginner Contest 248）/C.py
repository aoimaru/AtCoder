# DP問題
# coding: utf-8
# Your code here!
import pprint

MOD = 998244353

def main():
    N, M, K = map(int, input().split())
    DP = [[0]*(K+1) for _ in range(N+1)]
    DP[0][0] = 1
    for hg in range(N):
        for wd in range(K+1):
            for add in range(1, M+1):
                if wd+add <= K:
                    DP[hg+1][wd+add] += DP[hg][wd]
    
    print(sum(DP[-1])%MOD)
    
if __name__ == "__main__":
    main()
