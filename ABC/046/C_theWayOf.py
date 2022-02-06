# coding: utf-8
# Your code here!
import math

def main():
    N = int(input())
    T_comp, A_comp = map(int, input().split())
    Ans = T_comp+A_comp
    print("first", Ans)
    for _ in range(N-1):
        T, A = map(int, input().split())
        if T >= T_comp and A >= A_comp:
            Ans = T+A
        else:
            if T <= A:
                A = A*(math.ceil(T_comp/T))
                T = T_comp
            else:
                T = T*(math.ceil(A_comp/A))
                A = A_comp
        Ans = T+A
        print(T, A, "->", Ans)
        T_comp = T; A_comp = A
        
        
            
        

if __name__ == "__main__":
    main()
