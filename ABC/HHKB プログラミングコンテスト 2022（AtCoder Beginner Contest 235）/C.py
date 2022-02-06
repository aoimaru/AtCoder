# coding: utf-8
# Your code here!

def main():
    N, Q = map(int, input().split())
    AN = list(map(int, input().split()))
    info = dict()
    for idx, A in enumerate(AN):
        if not A in info:
            info[A] = list()
        info[A].append(idx+1)
        
    for _ in range(Q):
        X, K = map(int, input().split())
        try:
            print(info[X][K-1])
        except:
            print(-1)
    
if __name__ == "__main__":
    main()