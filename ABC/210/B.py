# coding: utf-8
# Your code here!
import math

def main():
    N = int(input())
    S = list(map(int, input()))
    ans = 0
    for ids, s in enumerate(S):
        if s == 1:
            ans = ids
            break
    if ans%2 == 0:
        print("Takahashi")
    else:
        print("Aoki")
    
if __name__ == "__main__":
    main()
