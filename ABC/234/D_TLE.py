# coding: utf-8
# Your code here!
import bisect

def main():
    N, K = map(int, input().split())
    PN = list(map(int, input().split()))
    comp = []
    cnt = 0
    while cnt<K:
        bisect.insort(comp, PN.pop(0))
        cnt+= 1
    for P in PN:
        print(comp[0])
        if P < comp[0]:
            continue
        bisect.insort(comp, P)
        comp.pop(0)
    print(comp[0])
    
if __name__ == "__main__":
    main()