# coding: utf-8
# Your code here!

def main():
    X = list(input())
    alpha = [chr(cnt) for cnt in range(97, 97+26)]
    adic = {}
    for x, alp in zip(X, alpha):
        adic[x] = alp
    adic2 = {}
    for x, alp in zip(X, alpha):
        adic2[alp] = x
        
    N = int(input())
    SN = []
    for _ in range(N):
        S = list(map(lambda x: adic[x], list(input())))
        SN.append(S)
    SN.sort()
    for S in SN:
        ans = ""
        for an in [adic2[s] for s in S]:
            ans += an
        print(ans)
            
if __name__ == "__main__":
    main()