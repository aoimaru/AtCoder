# coding: utf-8
# Your code here!

def main():
    N = int(input())
    As = list(map(int, input().split()))
    Ans = 0
    for A in As:
        if A > 10:
            B = A-10
            Ans += B
    print(Ans)
            
if __name__ == "__main__":
    main()