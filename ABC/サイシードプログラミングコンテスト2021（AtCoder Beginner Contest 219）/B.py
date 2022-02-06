# coding: utf-8
# Your code here!
def main():
    SN = {}
    SN[1] = input()
    SN[2] = input()
    SN[3] = input()
    T = list(map(int, list(input())))
    Ans = ""
    for t in T:
        Ans += SN[t]
    print(Ans)
        
if __name__ == "__main__":
    main()