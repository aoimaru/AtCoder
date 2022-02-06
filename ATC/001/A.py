# coding: utf-8
# Your code here!
#AtCoderだとRE起こす... Paiza.ioなら問題ない, Pythonだから?

def extract(hg, wd):
    """DFS"""
    if (hg < 0) or (hg >= H) or (wd < 0) or (wd >= W) or (Tables[hg][wd] == "#"):
        return
    if (hg, wd) in visited:
        return
    visited.add((hg, wd))
    
    extract(hg-1, wd)
    extract(hg, wd+1)
    extract(hg+1, wd)
    extract(hg, wd-1)

def main():
    global Tables
    global H, W
    global visited
    Tables = []
    H, W = map(int, input().split())
    for _ in range(H):
        Tables.append(list(input()))
    
    # for Table in Tables:
    #     print(Table)
    
    st_hg = 0
    st_wd = 0
    ed_hg = 0
    ed_wd = 0
    for hi, comps in enumerate(Tables):
        for wi, comp in enumerate(comps):
            if comp == "s":
                st_hg = hi
                st_wd = wi
                break
            if comp == "g":
                ed_hg = hi
                ed_wd = wi
                
    visited = set()
    extract(st_hg, st_wd)
    
    # print(visited)
    if (ed_hg, ed_wd) in visited:
        print("Yes")
    else:
        print("No")
    
if __name__ == "__main__":
    main()