# coding: utf-8
# Your code here!

def extract(deps):
    for dep in deps:
        for dp in Deps[dep]:
            if not dp in deps:
                deps.append(dp)
        else:
            global Logs
            Logs = deps
            return 
    extract(deps)


def main():
    N = int(input())
    global Deps
    Deps = {}
    Times = {} 
    for cnt in range(N-1):
        TKA = list(map(int, input().split()))
        T = TKA.pop(0)
        _ = TKA.pop(0)
        Times[cnt+1] = T
        Deps[cnt+1] = TKA
        
    TKAN = list(map(int, input().split()))
    NTime = TKAN.pop(0)
    _ = TKAN.pop(0)
    extract(TKAN)
    
    Time = NTime
    for Log in Logs:
        Time += Times[Log]
    print(Time)
        
if __name__ == "__main__":
    main()