# coding: utf-8
# Your code here!

def main():
    N = int(input())
    SN = list(map(int, input().split()))
    Smax = max(SN)
    Map = set()
    for A in range(1, (Smax//4)+1):
        for B in range(1, (Smax//4)+1):
            result = (4*A*B)+(3*A)+(3*B)
            Map.add(result)
    Ans = 0
    for S in SN:
        if not S in Map:
            Ans += 1
    print(Ans)
    
if __name__ == "__main__":
    main()