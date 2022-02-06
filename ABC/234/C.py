# coding: utf-8
# Your code here!
import re

def main():
    K = int(input())
    BK = bin(K)
    BK = re.sub("1", "2", BK[2:])
    print(BK)
    
if __name__ == "__main__":
    main()