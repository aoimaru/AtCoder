# coding: utf-8
# Your code here!
import string

alpha = list(string.ascii_uppercase)

def main():
    N = int(input())
    S = list(input())
    comps = [(alpha.index(s)+N)%26 for s in S]
    ans = [alpha[comp] for comp in comps]
    print("".join(ans))

if __name__ == "__main__":
    main()
