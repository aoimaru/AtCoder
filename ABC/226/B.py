# coding: utf-8
# Your code here!

def main():
    N = int(input())
    LN = set()
    for _ in range(N):
        AL = list(map(int, input().split()))
        L = " ".join(map(str, AL))
        LN.add(L)

    print(len(LN))
        
if __name__ == "__main__":
    main()