# coding: utf-8
# Your code here!
import re
import sys

def main():
    S = input()
    if not re.search('[A-Z]', S):
        print("No")
        sys.exit()
    if not re.search('[a-z]', S):
        print("No")
        sys.exit()
    if len(list(set(list(S)))) != len(S):
        print("No")
        sys.exit()
    print("Yes")

if __name__ == "__main__":
    main()
