# coding: utf-8
# Your code here!
import copy

def rec(used):
    if len(used) >= N:
        return Table[used[-1]][-1]
    cost = Table[used[-1]][len(used)-1]
    cds = list()
    for now in range(N):
        if now in used:
            continue
        if not used[-1] in Rel:
            c_used = copy.copy(used)
            c_used.append(now)
            cd = rec(c_used)
            cds.append(cd)
        else:
            if not now in Rel[used[-1]]:
                c_used = copy.copy(used)
                c_used.append(now)
                cd = rec(c_used)
                cds.append(cd)
    if not cds:
        return -1
    cds = [cd for cd in cds if cd >= 0]
    
    if not cds:
        return -1
    
    return cost+min(cds)
        
def main():
    global N
    N = int(input())
    global Table
    Table = list()
    for _ in range(N):
        Table.append(list(map(int, input().split())))
    
    M = int(input())
    global Rel
    Rel = dict()
    for _ in range(M):
        X, Y = map(lambda x:int(x)-1, input().split())
        if not X in Rel:
            Rel[X] = list()
        Rel[X].append(Y)
        if not Y in Rel:
            Rel[Y] = list()
        Rel[Y].append(X)
        
    ans = list()
    for cnt in range(N):
        an = rec([cnt])
        ans.append(an)
    ans = [an for an in ans if an >= 0]
    if not ans:
        print(-1)
    else:
        print(min(ans))
    

if __name__ == "__main__":
    main()