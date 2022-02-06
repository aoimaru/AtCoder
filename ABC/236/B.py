# coding: utf-8
# Your code here!

def main():
    N = int(input())
    A4N = list(map(int, input().split()))
    Basic = N*(N+1)//2
    print(Basic*4-sum(A4N))
    
if __name__ == "__main__":
    main()
