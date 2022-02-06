# coding: utf-8
# Your code here!
import math

def main():
    N, M = map(int, input().split())
    
    Primes = [2, 3]
    for cnt in range(5, M+1):
        for num in range(2, int(math.sqrt(cnt))+1):
            if cnt%num == 0:
                break
        else:
            Primes.append(cnt)
        
    As = list(map(int, input().split()))
    As.sort()
    Lows = set(); Highs = set()
    for A in As:
        cnt = 1
        while cnt*cnt <= A:
            if A%cnt == 0:
                Lows.add(cnt)
                if cnt != A//cnt:
                    Highs.add(A//cnt)
            cnt += 1
            
    Div = list(Lows)+list(Highs)
    
    Ans = []
    for Prime in Primes:
        if not Prime in Div:
            Ans.append(Prime)
            
    print(len(Ans)+1)
    print(1)
    for An in Ans:
        print(An)
            
            
if __name__ == "__main__":
    main()



# coding: utf-8
# Your code here!
import math

def main():
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    As.sort()
    Lows = set(); Highs = set()
    for A in As:
        cnt = 1
        while cnt*cnt <= A:
            if A%cnt == 0:
                Lows.add(cnt)
                if cnt != A//cnt:
                    Highs.add(A//cnt)
            cnt += 1
            
    Div = list(Lows)+list(Highs)
    
    Primes = [2, 3]
    for cnt in range(5, M+1):
        for num in range(2, int(math.sqrt(cnt))+1):
            if cnt%num == 0:
                break
        else:
            if not cnt in Div:
                Primes.append(cnt)
    
    if 2 in Div:
        Primes.remove(2)
    if 3 in Div:
        Primes.remove(3)
    
    print(len(Primes)+1)
    print(1)
    for Prime in Primes:
        print(Prime)
            
            
if __name__ == "__main__":
    main()

