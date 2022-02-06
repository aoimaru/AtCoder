# coding: utf-8
# Your code here!

def AB(sub):
    count = 0
    for cnt in range(1, sub+1):
        if sub%cnt == 0:
            count += 1
    return count

def main():
    N = int(input())
    ans = 0
    for C in range(1, N):
        ans += AB(N-C)
    
    print(ans)
            
if __name__ == "__main__":
    main()
