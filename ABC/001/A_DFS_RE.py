# coding: utf-8
# Your code here!

def DFS(S: int, T: int):
    if (S < 0 or S >= H or T < 0 or T >= W or Table[S][T] == "#"):
        return
    if Flag[S][T]:
        return

    Flag[S][T] = True
    DFS(S-1, T)
    DFS(S, T+1)
    DFS(S+1, T)
    DFS(S, T-1)

def main():
    global H, W
    H, W = map(int, input().split())
    global Table
    Table = []
    for _ in range(H):
        Table.append(list(input()))
    
    for hg in range(H):
        for wd in range(W):
            if Table[hg][wd] == "s":
                SY = hg; SX = wd
            if Table[hg][wd] == "g":
                GY = hg; GX = wd
    global Flag
    Flag = [[False]*W for _ in range(H)]
    
    DFS(SY, SX)

    if Flag[GY][GX]:
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()
