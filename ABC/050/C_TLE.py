# coding: utf-8
# Your code here!
CONST = 10**9+7

def main():
    def BFS(comps, count):
        if not As:
            global RT
            RT = len(comps)
            return
        A = As.pop(0)
        args = []
        for comp in comps:
            for cnt in range(N):
                left = cnt; right = lgA-1-cnt
                if abs(left-right) == A:
                    # print(left, right)
                    if comp[cnt] == 0:
                        comp[cnt] = count
                        args.append(comp.copy())
                        comp[cnt] = 0
        count += 1
        # print(args)
        BFS(args, count)
                    
    N = int(input())
    As = list(map(int, input().split()))
    lgA = len(As)
    BFS([[0]*N], 1)
    print(RT%CONST)
    
if __name__ == "__main__":
    main()