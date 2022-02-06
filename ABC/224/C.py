# coding: utf-8
# Your code here!
from itertools import combinations

def main():
    N = int(input())
    Maps = {}
    for cnt in range(N):
        Maps[cnt] = list(map(int, input().split()))
    
    Ans = 0
    for comp in combinations([cnt for cnt in range(N)], 3):
        X1, Y1 = Maps[comp[0]]
        X2, Y2 = Maps[comp[1]]
        X3, Y3 = Maps[comp[2]]
        # 平行移動
        X1 -= X3
        X2 -= X3
        Y1 -= Y3
        Y2 -= Y3
        if X1*Y2 != X2*Y1:
            Ans += 1
            
    print(Ans)
        
if __name__ == "__main__":
    main()
