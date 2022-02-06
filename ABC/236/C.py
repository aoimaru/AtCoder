# coding: utf-8
# Your code here!
import sys

def main():
    N, M = map(int, input().split())
    if N == M:
        for _ in range(N):
            print("Yes")
        sys.exit()
        
    SN = list(input().split())
    TN = list(input().split())
    

    while SN:
        S = SN.pop(0)
        if S == TN[0]:
            TN.pop(0)
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
