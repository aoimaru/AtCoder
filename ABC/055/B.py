# coding: utf-8
# Your code here!

CONST = 10**9+7

def main():
    N = int(input())
    power = 1
    for cnt in range(1,N+1):
        power = (power*cnt)%CONST
        
    print(power)
        
if __name__ == "__main__":
    main()