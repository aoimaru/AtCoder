# coding: utf-8
# Your code here!
import sys

def main():
    N = int(input())
    if N < 100:
        print("No")
        sys.exit()
    if N%100 != 0:
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    main()
