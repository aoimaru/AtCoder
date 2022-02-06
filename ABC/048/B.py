# coding: utf-8
# Your code here!
import sys

def main():
    A, B, X = map(int, input().split())
    if A == 0:
        Ans = (B//X)+1
    else:
        Ans = (B//X)-((A-1)//X)
    print(Ans)
if __name__ == "__main__":
    main()