# coding: utf-8
# Your code here!
from collections import Counter
CONST = 10**9+7
def main():
    N = int(input())
    comps = []
    for Number in range(2, N+1):
        comp = []
        for cnt in range(2, Number+1):
            while Number%cnt == 0:
                Number = Number//cnt
                comp.append(cnt)
        comps.extend(comp)
    Dict = Counter(comps)
    Ans = 1
    for val in Dict.values():
        Ans = Ans*(val+1)
    print(Ans%CONST)

if __name__ == "__main__":
    main()