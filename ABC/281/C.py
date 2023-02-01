# coding: utf-8
# Your code here!
import bisect

def main():
    N, T = map(int, input().split())
    AN = list(map(int, input().split()))
    
    BN = list()
    C = 0
    for A in AN:
        C += A
        BN.append(C)
    
    Rem = T%sum(AN)
    Rep = bisect.bisect(BN, Rem)
    BN.insert(0, 0)
    print(Rep+1, Rem-BN[Rep])
    
if __name__ == "__main__":
    main()