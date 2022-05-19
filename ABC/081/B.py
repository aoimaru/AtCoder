# coding: utf-8
# Your code here!

def main():
    _ = input()
    AN = list(map(int, input().split()))
    ans = 0
    for A in AN:
        ans |= A
    ans = bin(ans)[::-1]
    print(ans.index("1"))
    
if __name__ == "__main__":
    main()
