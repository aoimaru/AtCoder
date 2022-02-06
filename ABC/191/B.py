# coding: utf-8
# Your code here!


def main():
    N, X = map(int, input().split())
    AN = list(map(int, input().split()))
    Ans = ""
    for A in AN:
        if A != X:
            Ans += str(A) + " "
    print(Ans[:-1])

if __name__ == "__main__":
    main()