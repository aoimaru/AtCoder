# coding: utf-8
# Your code here!
import sys

def main():
    _ = input()
    LN = list(map(int, input().split()))
    LN.sort()
    maxL = LN.pop(-1)
    if maxL >= sum(LN):
        print("No")
    else:
        print("Yes")
    
if __name__ == "__main__":
    main()