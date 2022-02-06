# coding: utf-8
# Your code here!
import math

def main():
    N = int(input())
    Scores = list(map(int, input().split()))
    Comps = [Score for Score in Scores if not Score == 0]
    print(math.ceil(sum(Comps)/len(Comps)))

if __name__ == "__main__":
    main()
