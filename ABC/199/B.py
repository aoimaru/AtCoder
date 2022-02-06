# coding: utf-8
# Your code here!

def main():
    N = int(input())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    
    Ans = set([com for com in range(As[0], Bs[0]+1)])
    
    for A, B in zip(As, Bs):
        comp = set([com for com in range(A, B+1)])
        Ans = Ans&comp
        
    print(len(Ans))

if __name__ == "__main__":
    main()