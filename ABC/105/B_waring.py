# coding: utf-8
# Your code here!
#Cakes and Donuts

import sys

def main():
    N = int(input())
    if (N%4 == 0) or (N%7==0):
        print("Yes")
        sys.exit()
    if N < 4:
        print("No")
        sys.exit()
    flag = 0
    while True:
        N -= 7
        if N%4 == 0:
            break
        if N < 0:
            flag = 1
            break
    if flag == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
