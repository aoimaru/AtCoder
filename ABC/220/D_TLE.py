# coding: utf-8
# Your code here!
import copy
from collections import Counter

Ans = []

def BFS(comps):
    args = []
    flag = 0
    for comp in comps:
        A = comp.pop(0)
        try:
            B = comp.pop(0)
        except:
            Ans.append(A)
            flag = 1
        else:
            arg1 = copy.copy(comp)
            arg2 = copy.copy(comp)
            arg1.insert(0, (A+B)%10)
            arg2.insert(0, (A*B)%10)
            args.append(arg1)
            args.append(arg2)
    else:
        del comps
        if flag == 0:
            BFS(args)
        else:
            return
        
def main():
    N = int(input())
    AN = list(map(int, input().split()))
    BFS([AN])
    Am = Counter(Ans)
    for cnt in range(10):
        if cnt in Am:
            print(Am[cnt]%998244353)
        else:
            print(0)
        
    
if __name__ == "__main__":
    main()