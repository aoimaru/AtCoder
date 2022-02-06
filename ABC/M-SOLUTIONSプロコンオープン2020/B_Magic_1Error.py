# coding: utf-8
# Your code here!
import sys

def main():
    A, B, C = map(int, input().split())
    K = int(input())
    flag = 0
    if A < B < C:
        print("Yes")
        sys.exit()
    while True:
        if K <= 0:
            flag = 1
            break
        B = B*2
        K -= 1
        if B > A:
            break
    if flag == 1:
        print("No")
        sys.exit()
    flag = 0
    while True:
        if K <= 0:
            flag = 1
            break
        C = C*2
        K -= 1
        if C > B:
            break
    if flag == 1:
        print("No")
        sys.exit()
    else:
        print("Yes")
        
if __name__ == "__main__":
    main()
