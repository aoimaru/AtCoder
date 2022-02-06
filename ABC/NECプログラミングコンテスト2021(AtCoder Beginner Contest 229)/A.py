# coding: utf-8
# Your code here!
import sys

def main():
    S1 = input()
    S2 = input()
    if S1[0] == "." and S2[1] == ".":
        print("No")
        sys.exit()
    if S1[1] == "." and S2[0] == ".":
        print("No")
        sys.exit()
    print("Yes")

if __name__ == "__main__":
    main()
