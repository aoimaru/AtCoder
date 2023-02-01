# coding: utf-8
# Your code here!

def main():
    _ = input()
    SN = list(input())
    Flag = False
    
    Ans = ""
    for S in SN:
        if not Flag:
            if S==",":
                S="."
            if S=='"':
                Flag=True
            Ans += S
        else:
            if S =='"':
                Flag=False
            Ans += S
    
    print(Ans)
                
if __name__ == "__main__":
    main()