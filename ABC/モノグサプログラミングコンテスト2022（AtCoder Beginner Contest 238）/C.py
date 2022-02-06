# coding: utf-8
# Your code here!
import sys

def col(N):
    return N*(N+1)//2

def fig(N):
    nine = int("9"*(length-1))
    N = N-nine
    return N

def main():
    N = int(input())
    if N < 10:
        print(N*(N+1)//2)
        sys.exit()
    
    global length
    length = len(str(N))
    coms = []
    for cnt in range(length-1):
        com = 9*(10**cnt)
        coms.append(col(com))
    N = fig(N)
    coms.append(col(N))
    print(sum(coms)%998244353)
    
if __name__ == "__main__":
    main()
