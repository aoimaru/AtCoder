# coding: utf-8
# Your code here!
import sys

def main():
    N = int(input())
    if N >= 5:
        print("Yes")
        sys.exit()
    if 2**N > N**2:
        print("Yes")
    else:
        print("No")
    
if __name__ == "__main__":
    main()
