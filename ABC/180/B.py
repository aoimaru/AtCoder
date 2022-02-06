# coding: utf-8
# Your code here!
import math

def Manhattan(Nums):
    return sum([abs(Num) for Num in Nums])

def Euclid(Nums):
    comp = sum([(Num)**2 for Num in Nums])
    return math.sqrt(comp)

def ChebyChef(Nums):
    return max([abs(Num) for Num in Nums])

def main():
    N = int(input())
    Nums = list(map(int, input().split()))
    print(Manhattan(Nums))
    print(Euclid(Nums))
    print(ChebyChef(Nums))


if __name__ == "__main__":
    main()
