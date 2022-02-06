# coding: utf-8
# Your code here!

CONST = 10**9+7

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    
    Ans = C[0]
    for cnt in range(1, N):
        Ans = Ans*(C[cnt]-cnt)%CONST
        
    print(Ans)
    
if __name__ == "__main__":
    main()