# coding: utf-8
# Your code here!
import heapq

def main():
    N, K = map(int, input().split())
    PN = list(map(int, input().split()))
    comp = []
    heapq.heapify(comp)
    cnt = 0
    while cnt<K:
        heapq.heappush(comp, PN.pop(0))
        cnt+= 1
    heapq.heapify(comp)
    for P in PN:
        print(comp[0])
        if P <= comp[0]:
            continue
        heapq.heappush(comp, P)
        heapq.heappop(comp)
    print(comp[0])
    
if __name__ == "__main__":
    main()