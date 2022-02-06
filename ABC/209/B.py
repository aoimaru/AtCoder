# coding: utf-8
# Your code here!

def main():
    N, X = map(int, input().split())
    As = list(map(int, input().split()))
    first = sum([A-1 for ida, A in enumerate(As) if ida%2==1])
    second = sum([A for ida, A in enumerate(As) if ida%2==0])
    if first+second <= X:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()