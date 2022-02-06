# coding: utf-8
# Your code here!
    
def main():
    N = int(input())
    AN = list(map(int, input().split()))
    X = int(input())
    ch0 = X//sum(AN)
    ch1 = X%sum(AN)
    comp = 0
    ch2 = 0
    for cnt in range(N):
        comp += AN[cnt]
        if comp > ch1:
            ch2 = cnt+1
            break
    print(ch0*N+ch2)
    
if __name__ == "__main__":
    main()