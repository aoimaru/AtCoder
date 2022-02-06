# coding: utf-8
# Your code here!

def main():
    N, K = map(int, input().split())
    Cs = list(map(int, input().split()))
    Ans = 0
    for idc in range(len(Cs)):
        if idc > len(Cs)-K:
            continue
        if len(set(Cs[idc:idc+K])) > Ans:
            Ans = len(set(Cs[idc:idc+K]))
        if Ans == K:
            break
    print(Ans)
if __name__ == "__main__":
    main()
