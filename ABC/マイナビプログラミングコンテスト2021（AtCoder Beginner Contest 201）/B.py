# coding: utf-8
# Your code here!

def main():
    N = int(input())
    Mt = {}
    for _ in range(N):
        S, T = input().split()
        T = int(T)
        Mt[S] = T
    
    Mt = [
        mt for mt in sorted(Mt.items(), key=lambda x:x[1], reverse=True)
        ]
    
    print(Mt[1][0])
    
if __name__ == "__main__":
    main()