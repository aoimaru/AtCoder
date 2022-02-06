# coding: utf-8
# Your code here!
import copy

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    S = K//N
    T = K%N
    
    B = {cnt: val for cnt, val in enumerate(A)}
    B = sorted(B.items(), key=lambda x:x[1])
    
    C = [B[cnt][0] for cnt in range(T)]
    
    for a in A:
        if a in C:
            print(S+1)
        else:
            print(S)

if __name__ == "__main__":
    main()