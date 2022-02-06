# coding: utf-8
# Your code here!

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = set(A)
    if len(B) == N:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()