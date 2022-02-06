# coding: utf-8
# Your code here!
import sys
import pprint

def main():
    N = int(input())
    X, Y = map(int, input().split())
    scores = []
    AN = []
    BN = []
    for _ in range(N):
        A, B = map(int, input().split())
        AN.append(A)
        BN.append(B)
    
    DP = [[0]*(sum(AN)+1) for _ in range(N+1)]
    DP2 = [[list()]*(sum(AN)+1) for _ in range(N+1)]
    
    for hg in range(N):
        for wd in range(sum(AN)+1):
            if AN[hg] > wd:
                DP[hg+1][wd] = DP[hg][wd]
                DP2[hg+1][wd] = [hg]
            else:
                if DP[hg][wd] >= DP[hg][wd-AN[hg]]+AN[hg]:
                    DP[hg+1][wd] = DP[hg][wd]
                    DP2[hg+1][wd] = DP2[hg][wd]
                else:
                    DP[hg+1][wd] = DP[hg][wd-AN[hg]]+AN[hg]
                    DP2[hg+1][wd] = DP2[hg][wd-AN[hg]]+[hg]
                    
    if max(max(DP)) < X:
        print(-1)
        sys.exit()
    
    ans = []
    for hg in range(N):
        for wd in range(sum(AN)+1):
            if DP[hg][wd] >= X:
                an = 0
                for dp2 in DP2[hg][wd]:
                    an += BN[dp2]
                if an >= Y:
                    ans.append(len(DP2[hg][wd]))
    if not ans:
        print(-1)
        sys.exit()
    else:
        print(min(ans))
                    
  
 
                
            
if __name__ == "__main__":
    main()