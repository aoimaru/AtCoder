# coding: utf-8
# Your code here!
# 参りました

def main():
    N, M = map(int, input().split())
    As = list(map(lambda x: [int(x), "a"], input().split()))
    Bs = list(map(lambda x: [int(x), "b"], input().split()))
    work = sorted(As+Bs, key=lambda x: x[0])
    ans = 10 ** 10
    for i in range(0, len(work)-1):
        if work[i][1] != work[i+1][1]:
            ans = min(ans, abs(work[i][0] - work[i+1][0]))
    print(ans)
    
if __name__ == "__main__":
    main()