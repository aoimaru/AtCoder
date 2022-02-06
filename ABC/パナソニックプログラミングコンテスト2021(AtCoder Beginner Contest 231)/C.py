# これが正解　正解になってくれ！！
# coding: utf-8
# Your code here!
import bisect

def main():
    N, Q = map(int, input().split())
    AN = list(map(int, input().split()))
    AN.sort()
    length = len(AN)
    for _ in range(Q):
        X = int(input())
        print(length-bisect.bisect_left(AN, X))
if __name__ == "__main__":
    main()
