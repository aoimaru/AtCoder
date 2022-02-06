# coding: utf-8
# Your code here!
def main():
    L, Q = map(int, input().split())
    LN = [0, L]
    for _ in range(Q):
        C, X = map(int, input().split())
        LN.append(X)
        if C == 2:
            LN.sort()
            SUF = LN.index(X)
            print(LN[SUF+1]-LN[SUF-1])
            LN.remove(X)
        
if __name__ == "__main__":
    main()