# coding: utf-8
# Your code here!
#全然わからん

CONST = 10**9+7

def main():
    N = int(input())
    As = list(map(int, input().split()))
    As.sort()
    if N%2 == 0:
        check_As = [(cnt)*2+1 for cnt in range(N//2)]*2
    else:
        check_As = [(cnt)*2 for cnt in range(N//2+1)]*2
        check_As.append(0)
    check_As.sort()
    print(check_As)
    if As != check_As:
        print(0)
    else:
        ans = 2**(N//2)
        ans = ans % (CONST)
        print(ans)
    
        
    
    
if __name__ == "__main__":
    main()
