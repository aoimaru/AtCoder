# coding: utf-8
# Your code here!
import heapq
from heapq import heappush, heappop
from collections import deque


def main():
    Q = int(input())
    hq = []
    heapq.heapify(hq)
    dq = deque()
    
    for _ in range(Q):
        C = list(map(int, input().split()))
        if C[0] == 1:
            dq.append(C[1])
        elif C[0] == 2:
            if hq:
                A = heapq.heappop(hq)
            else:
                A = dq.popleft()
            print(A)
        elif C[0] == 3:
            while dq:
                B = dq.popleft()
                heapq.heappush(hq, B)
    
if __name__ == "__main__":
    main()
    