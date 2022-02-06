# coding: utf-8
# Your code here!
import sys

def main():
    A, B = map(int, input().split())
    if A > 0 and B == 0:
        print("Gold")
        sys.exit()
    if A == 0 and B > 0:
        print("Silver")
        sys.exit()
    if A > 0 and B > 0:
        print("Alloy")
        sys.exit()
    
if __name__ == "__main__":
    main()