# coding: utf-8
# Your code here!

def main():
    A, B, C, D, E, F, X = map(int, input().split())
    print(A, B, C, D, E, F, X)
    Takahashi = 0
    Aoki = 0
    
    TA = (X//(A+C))*B
    AA = (X//(D+F))*E
    
    AC = (X%(A+C))
    DF = (X%(D+F))
    
    if AC > A:
        TA += A*B
    else:
        TA += AC*B
    
    if DF > D:
        AA += D*E
    else:
        AA += DF*E
    
    if TA > AA:
        print("Takahashi")
    elif TA < AA:
        print("Aoki")
    else:
        print("Draw")
    
    
        


if __name__ == "__main__":
    main()
