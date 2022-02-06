# coding: utf-8
# Your code here!
import copy
import sys

HIGH = 10
WIDE = 10

def DFS(high, wide):
    if high < 0 or high >= HIGH or wide < 0 or wide >= WIDE or Comps[high][wide] == "x":
        return
    Comps[high][wide] = "x"
    
    DFS(high-1, wide)
    DFS(high, wide+1)
    DFS(high+1, wide)
    DFS(high, wide-1)

def check(Tables):
    checked = set()
    for Table in Tables:
        for one in Table:
            checked.add(one)
    return len(checked)

def main():
    Maps = []
    for _ in range(HIGH):
        Maps.append(list(input()))
    for idh, wides in enumerate(Maps):
        for idw, wide in enumerate(wides):
            if wide == "x":
                global Comps
                Comps = copy.deepcopy(Maps)
                Comps[idh][idw] = "o"
                DFS(idh, idw)
                if check(Comps) == 1:
                    print("YES")
                    sys.exit()
    print("NO")

if __name__ == "__main__":
    main()
