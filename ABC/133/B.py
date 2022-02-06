# coding: utf-8
# Your code here!
import math

def main():
    N, D = map(int, input().split())
    tables = []
    for _ in range(N):
        tables.append(list(map(int, input().split())))
    
    Ans = 0
    for n in range(N-1):
        for d in range(n+1, N):
            ans = math.sqrt(sum(list(map(lambda y,z: (y-z)**2, tables[n], tables[d]))))
            if ans.is_integer():
                Ans += 1
    print(Ans)
        
if __name__ == "__main__":
    main()