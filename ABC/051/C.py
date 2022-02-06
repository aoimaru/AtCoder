# coding: utf-8
# Your code here!
"""
    ^------>~
    |  ^--->Y->
    |  |    | |
    |  |    | |
    |  |    | |
    |<-X<---~ |
       ^------~
"""

def main():

    SX, SY, TX, TY = map(int, input().split())
    DIF_X = TX-SX; DIF_Y = TY-SY
    mv1 = "U"*(DIF_Y)+"R"*(DIF_X)
    mv2 = "D"*(DIF_Y)+"L"*(DIF_X)
    mv3 = "L"+"U"*(DIF_Y+1)+"R"*(DIF_X+1)+"D"
    mv4 = "R"+"D"*(DIF_Y+1)+"L"*(DIF_X+1)+"U"
    print(mv1+mv2+mv3+mv4)
            
if __name__ == "__main__":
    main()