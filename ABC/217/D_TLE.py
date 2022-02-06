# coding: utf-8
# Your code here!
def main():
    L, Q = map(int, input().split())
    LN = [0, L]
    for _ in range(Q):
        C, X = map(int, input().split())
        if C == 1:
            LN.append(X)
        else:
            LN.sort()
            Min = [L for L in LN if L < X][-1]
            Max = [L for L in LN if L > X][0]
            print(Max-Min)
        
if __name__ == "__main__":
    main()