# coding: utf-8
# Your code here!

def main():
    H, W = map(int, input().split())
    HD = dict()
    WD = dict()
    Table = list()
    for h in range(H):
        AW = list(map(int, input().split()))
        HD[h] = sum(AW)
        for ida, A in enumerate(AW):
            if not ida in WD:
                WD[ida] = 0
            WD[ida] += A
        Table.append(AW)
    
    for hg in range(H):
        Tab = list()
        for wd in range(W):
            Tab.append(str(HD[hg]+WD[wd]-Table[hg][wd]))
        print(" ".join(Tab))
            
if __name__ == "__main__":
    main()