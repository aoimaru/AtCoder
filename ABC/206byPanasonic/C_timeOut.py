# coding: utf-8
# Your code here!
import math

def main():
    N = int(input())
    As = list(map(int, input().split()))
    Combs = math.factorial(N) // (math.factorial(N - 2) * math.factorial(2))
    count = 0
    for idA, A in enumerate(As):
        for idB in range(idA+1, N):
            if A == As[idB]:
                count += 1
    
    print(Combs-count)


if __name__ == "__main__":
    main()