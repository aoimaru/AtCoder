# coding: utf-8
# Your code here!

def main():
    N = int(input())
    PN = list(map(int, input().split()))
    
    QN0 = {suf+1: P for suf, P in enumerate(PN)}
    QN1 = sorted(QN0.items(), key=lambda x:x[1])
    Ans = ""
    for Q1 in QN1:
        Ans += " " + str(Q1[0])
    print(Ans[1:])
        
if __name__ == "__main__":
    main()