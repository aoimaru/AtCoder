# coding: utf-8
# Your code here!
import sys

def main():
    X, Y = map(int, input().split())
    sub = Y-X if Y-X>0 else 0
    if sub == 0:
        print(0)
        sys.exit()
    ans = sub//10+1 if sub%10!=0 else sub//10
    print(ans)

if __name__ == "__main__":
    main()
