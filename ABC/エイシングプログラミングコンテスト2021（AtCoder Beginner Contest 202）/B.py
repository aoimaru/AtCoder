# coding: utf-8
# Your code here!

def main():
    S = list(map(int, input()))
    Ans = []
    for s in S:
        if s == 6:
            Ans.append("9")
        elif s == 9:
            Ans.append("6")
        else:
            Ans.append(str(s))
    
    print("".join(Ans[::-1]))
    
if __name__ == "__main__":
    main()