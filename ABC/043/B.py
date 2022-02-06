# coding: utf-8
# Your code here!

def main():
    Ss = list(input())
    Ans = []
    for S in Ss:
        if S == "0":
            Ans.append("0")
        elif S == "1":
            Ans.append("1")
        else:
            if not Ans:
                pass
            else:
                _ = Ans.pop(-1)
    answear = ""
    for An in Ans:
        answear += An
    print(answear)
    
if __name__ == "__main__":
    main()