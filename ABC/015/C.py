# coding: utf-8
# Your code here!

def BFS(comps):
    if not Tables:
        global RT
        RT = comps
        return
    args = []
    adds = Tables.pop(0)
    for comp in comps:
        for add in adds:
            arg = comp + [add]
            args.append(arg)
    BFS(args)            
            
def main():
    N, K = map(int, input().split())
    global Tables
    Tables = []
    for _ in range(N):
        Tables.append(list(map(int, input().split())))

    start = [[num] for num in Tables.pop(0)]
    BFS(start)
    
    for rt in RT:
        cnt = 0
        for num in rt:
            cnt = cnt^num
        if cnt == 0:
            print("Found")
            break
    else:
        print("Nothing")
        
if __name__ == "__main__":
    main()