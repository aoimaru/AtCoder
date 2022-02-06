# coding: utf-8
# Your code here!
import sys

def check(first, second, third):
    if first+second == third:
        return True
    else:
        return False

def main():
    A, B, C = map(int, input().split())
    if check(A, B, C):
        print("Yes")
        sys.exit()
    if check(C, A, B):
        print("Yes")
        sys.exit()
    if check(B, C, A):
        print("Yes")
        sys.exit()
    print("No")

if __name__ == "__main__":
    main()