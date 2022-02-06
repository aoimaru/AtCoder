# coding: utf-8
# Your code here!

def main():
    H, W = map(int, input().split())
    Table = []
    for _ in range(H):
        Table.append(list(map(int, input().split())))
    
    Flag = 0
    for hg in range(H):
        I1 = hg
        for hg2 in range(hg, H):
            I2 = hg2
            for wd in range(W):
                J1 = wd
                for wd2 in range(wd, W):
                    J2 = wd2
                    if Table[I1][J1]+Table[I2][J2] > Table[I2][J1]+Table[I1][J2]:
                        Flag = 1
                        break
    if Flag == 1:
        print("No")
    else:
        print("Yes")
        
if __name__ == "__main__":
    main()
