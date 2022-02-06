# coding: utf-8
# Your code here!
import sys

def main():
    N = int(input())
    if N == 1:
        print(1)
        sys.exit()
    Ans = 0
    Num = 0
    for cnt in range(2, N+1):
        comp = cnt
        if cnt%2 == 1:
            continue
        count = 0
        while True:
            if cnt%2 == 0:
                count += 1
                cnt = cnt//2
            else:
                break
        if count >= Ans:
            Ans = count
            Num = comp
    print(Num)

if __name__ == "__main__":
    main()
