# coding: utf-8
# Your code here!
import sys

def main():
    N = int(input())
    TKAF = list(map(int, input().split()))
    IT = TKAF.pop(0)
    _ = TKAF.pop(0)
    Times = {}
    INIT = {}
    Times[1] = IT
    INIT[1] = IT
    for cnt in range(N-1):
        TKA = list(map(int, input().split()))
        T = TKA.pop(0)
        _ = TKA.pop(0)
        Times[cnt+2] = T
        INIT[cnt+2] = T 
        print(TKA)
        INITS = T
        for tka in TKA:
            Times[cnt+2] += Times[tka]
            INITS += INIT[tka]
        Times[cnt+2] = min(Times[cnt+2], INITS)
        
    
    for key, value in Times.items():
        print(key, value)
    
    print(Times[N])
    
if __name__ == "__main__":
    main()



# coding: utf-8
# Your code here!

def main():
    N = int(input())
    TKAF = list(map(int, input().split()))
    Ti = TKAF.pop(0)
    Times = {}
    Times[1] = Ti
    visited = set()
    # visited.add(1)
    for cnt in range(N-1):
        TKA = list(map(int, input().split()))
        T = TKA.pop(0)
        _ = TKA.pop(0)
        Times[cnt+2] = T
        for tka in TKA:
            if not tka in visited:
                visited.add(tka)
                Times[cnt+2] += Times[tka]
        # print("Time", Times[cnt+2])
        # print("visited", visited)
    print(Times[N])
    
if __name__ == "__main__":
    main()