# coding: utf-8
# Your code here!
from itertools import permutations

def main():
    S = list(input())
    Ans = set()
    for cnt in permutations(S, 3):
        An = "".join(cnt)
        Ans.add(An)
    print(len(Ans))
        
if __name__ == "__main__":
    main()
