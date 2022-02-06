# coding: utf-8
# Your code here!
import math
import sys

def main():
    N = int(input())
    Ans = 0
    for _ in range(N):
        A, B = map(int, input().split())
        Ans += int((B-A+1)*(A+B)/2)
    print(Ans)

            
if __name__ == "__main__":
    main()
