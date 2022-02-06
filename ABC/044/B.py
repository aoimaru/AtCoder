# coding: utf-8
# Your code here!
from collections import Counter

def main():
    W = list(input())
    Wdict = Counter(W)
    for w in Wdict.values():
        if w%2 == 1:
            print("No")
            break
    else:
        print("Yes")
    
if __name__ == "__main__":
    main()