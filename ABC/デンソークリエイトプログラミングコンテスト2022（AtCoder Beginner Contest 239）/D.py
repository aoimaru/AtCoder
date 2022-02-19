# coding: utf-8
# Your code here!
import sys

def is_prime(num):
    if num == 1:
        return True
    for cnt in range(2, int(num**0.5)+1):
        if num%cnt == 0:
            return False
    return True

def main():
    A, B, C, D = map(int, input().split())
    Ans = 0
    for first in range(A, B+1):
        if Ans > 0:
            print("Takahashi")
            sys.exit()
        for second in range(C, D+1):
            if is_prime(first+second):
                break
        else:
            Ans += 1
            continue
    if Ans == 0:
        print("Aoki")
    else:
        print("Takahashi")
         
if __name__ == "__main__":
    main()
