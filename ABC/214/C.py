# coding: utf-8
# Your code here!
import numpy as np
        
def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    
    ST = list(map(lambda x, y: x+y, S, T))

    first = ST.index(min(ST))
    
    S = np.array(S)
    T = np.array(T)
    S = np.roll(S, 0-first)
    T = np.roll(T, 0-first)
    
    Ans = []
    Ans.append(T[0])
    Min = min(T[1], S[0]+T[0])
    for cnt in range(1, N):
        Min = min(T[cnt], Min)
        Ans.append(Min)
        Min += S[cnt]
    
    Ans = np.array(Ans)
    Ans = np.roll(Ans, first)

    for An in Ans:
        print(An)
        
        
                
if __name__ == "__main__":
    main()
