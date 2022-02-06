# coding: utf-8
# Your code here!
#AC
from itertools import permutations
def main():
    S, K = input().split()
    K = int(K)
    S = list(S)
    
    Perm = set()
    for s in permutations(S):
        word = "".join(s)
        Perm.add(word)
    Perm = list(Perm)
    Perm.sort()
    print(Perm[K-1])

if __name__ == "__main__":
    main()
