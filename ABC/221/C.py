# coding: utf-8
# Your code here!
import copy
from itertools import permutations

def main():
    N = list(input())
    lim = len(N)
    N.sort(reverse=True)
    
    ch = [i for i in range(lim)]
    
    Ans = 0
    for cnt in range(1, (lim//2)+1):
        for cov in permutations(ch, cnt):
            comp = copy.copy(N)
            M = []
            for pp in sorted(cov, reverse=True):
                M.append(comp.pop(pp))
            M.sort(reverse=True)
            m = "".join(M)
            n = "".join(comp)
            com = int(n)*int(m)
            if com >= Ans:
                Ans = com
            del comp
    
    print(Ans)
    
if __name__ == "__main__":
    main()
