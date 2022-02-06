# coding: utf-8
# Your code here!
import math

def main():
    N = int(input())
    comp = int(math.sqrt(N))
    
    Ans = 0
    for com in range(comp, N):
        if N%com == 0:
            Ans = len(str(com))
            break
    else:
        Ans = len(str(N))
    
    print(Ans)
    
if __name__ == "__main__":
    main()