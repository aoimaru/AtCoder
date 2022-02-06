# coding: utf-8
# Your code here!

def main():
    N = int(input())
    Ts = list(map(int, input().split()))
    sumT = sum(Ts)
    M = int(input())
    for _ in range(M):
        P, X = map(int, input().split())
        ans = sumT-Ts[P-1]+X
        print(ans)
        
if __name__ == "__main__":
    main()