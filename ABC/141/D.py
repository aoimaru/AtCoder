# coding: utf-8
# Your code here!
import heapq

def main():
    N, M = map(int, input().split())
    AN = list(map(lambda x: int(x)*(-1), input().split()))
    heapq.heapify(AN)
    for _ in range(M):
        comp = heapq.heappop(AN)
        comp = (-1)*((-1)*comp//2)
        heapq.heappush(AN, comp)
    
    print((-1)*sum(AN))

if __name__ == "__main__":
    main()