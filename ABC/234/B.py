# coding: utf-8
# Your code here!
import itertools
import math

def main():
    N = int(input())
    XYs = []
    for _ in range(N):
        XYs.append(list(map(int, input().split())))
    
    ans = 0
    for cnt in itertools.combinations(XYs, 2):
        com = (cnt[1][0]-cnt[0][0])**2+(cnt[1][1]-cnt[0][1])**2
        ans = max(ans, math.sqrt(com))
    print(ans)
    
if __name__ == "__main__":
    main()