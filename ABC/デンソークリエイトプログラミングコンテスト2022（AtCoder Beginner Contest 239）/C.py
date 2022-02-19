# coding: utf-8
# Your code here!
import math
import sys

def main():
    cnds = [
        [2, 1],
        [1, 2],
        [-1, 2],
        [-2, 1],
        [-1, -2],
        [-2, -1],
        [1, -2],
        [2, -1]
        ]
    X1, Y1, X2, Y2 = map(int, input().split())
    comps = []
    for cnd in cnds:
        comp = [X1+cnd[0], Y1+cnd[1]]
        comps.append(comp)
    
    for comp in comps:
        cal = (X2-comp[0])**2+(Y2-comp[1])**2
        if cal == 5:
            print("Yes")
            sys.exit()
    else:
        print("No")
        
if __name__ == "__main__":
    main()
