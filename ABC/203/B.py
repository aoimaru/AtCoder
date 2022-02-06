# coding: utf-8
# Your code here!

def main():
    N, K = map(int, input().split())
    Hnd = (1/2)*N*(N+1)*100*K
    One = (1/2)*K*(K+1)*N
    print(int(Hnd)+int(One))
    
if __name__ == "__main__":
    main()