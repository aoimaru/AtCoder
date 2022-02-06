# coding: utf-8
# Your code here!
#貪欲法

def main():
    N = int(input())
    K = int(input())
    Ans = 1
    for cnt in range(N):
        Ans = min(Ans+K, Ans*2)
    print(Ans)
        
if __name__ == "__main__":
    main()