# coding: utf-8
# Your code here!

def main():
    N, K = map(int, input().split())
    
    for _ in range(K):
        if N%200 == 0:
            N = N//200
        else:
            N = N*1000+200
    print(N)
    
    
if __name__ == "__main__":
    main()