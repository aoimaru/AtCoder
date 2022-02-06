# coding: utf-8
# Your code here!
import numpy as np

def main():
    H, W, N = map(int, input().split())
    Tables = []
    As = []; Bs = []
    ABs = {}
    Nums = {}
    for cnt in range(N):
        A, B = map(int, input().split())
        Nums[(A-1, B-1)] = cnt+1
        As.append(A-1); Bs.append(B-1)
        ABs[A-1] = B-1
    As.sort()
    for A in As:
        Table = []
        for B in Bs:
            if ABs[A] == B:
                Table.append(Nums[(A, B)])
            else:
                Table.append(0)
        Tables.append(Table)

    Ans = {}
    for hg, Table in enumerate(Tables):
        for wd, one in enumerate(Table):
            if not one == 0:
                Ans[(hg+1, wd+1)] = one
    
    newAns = sorted(Ans.items(), key=lambda x:x[1])
    for newAn in newAns:
        print(newAn[0][0], newAn[0][1])
        
if __name__ == "__main__":
    main()