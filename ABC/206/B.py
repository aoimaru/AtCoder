# coding: utf-8
# Your code here!

def main():
    N = int(input())
    A = [count for count in range(1, N+1)]
    B = list(map(int, input().split()))
    B.sort()
    if str(A) == str(B):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
