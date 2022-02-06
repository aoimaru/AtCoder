# coding: utf-8
# Your code here!
import copy

def main():
    ST = list(input().split())
    ST0 = copy.copy(ST)
    ST.sort()
    if ST == ST0:
        print("Yes")
    else:
        print("No")
    
if __name__ == "__main__":
    main()