# coding: utf-8
# Your code here!
import math

def main():
    N, D = map(int, input().split())
    cnt = 0
    for _ in range(N):
        X, Y = map(int, input().split())
        if math.sqrt(X**2+Y**2) <= D:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()
