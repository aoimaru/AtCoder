# coding: utf-8
# Your code here!
import pprint

def main():
    N, W = map(int, input().split())
    AN = []
    BN = []
    for _ in range(N):
        A, B = map(int, input().split())
        AN.append(A)
        BN.append(B)
    
    DP = [[0]*(W+1) for _ in range(N+1)]
    
    for hg in range(N):
        for wd in range(W+1):
            if wd >= BN[hg]:
                cnd = DP[hg][wd]
                for bc in range(BN[hg]+1):
                    cnd = max(DP[hg][wd-bc]+AN[hg]*bc, cnd)
                DP[hg+1][wd] = cnd
            else:
                DP[hg+1][wd] = max(DP[hg][wd], AN[hg]*wd)
            
    # pprint.pprint(DP)
    print(DP[-1][-1])
    
if __name__ == "__main__":
    main()
