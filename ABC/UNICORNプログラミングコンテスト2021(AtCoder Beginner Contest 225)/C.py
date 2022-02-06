# coding: utf-8
# Your code here!
import sys



def main():
    N, M = map(int, input().split())
    Rec = []
    for _ in range(N):
        Rec.append(list(map(int, input().split())))
    
    init = Rec[0][0]
    for hg in range(N):
        for wd in range(M):
            if Rec[hg][wd] != init+(7*hg)+wd:
                print("No")
                break
        else:
            continue
        break
    else:
        
        ch0 = Rec[0][0]%7
        if ch0+M-1 > 7:
            print("No")
        else:
            ch1 = Rec[0][-1]%7
            if ch1 == 0:
                ch1 = 7
            if ch1-M < 0:
                print("No")
            else:
                print("Yes")
        
if __name__ == "__main__":
    main()
