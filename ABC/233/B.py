# coding: utf-8
# Your code here!
import sys

def main():
    L, R = map(int, input().split())
    S = list(input())
    fst = "".join(S[:L-1])
    sec = S[L-1:R]
    thd = "".join(S[R:])
    rev = ""
    while sec:
        rev += sec.pop(-1)
    print(fst+rev+thd)

if __name__ == "__main__":
    main()
