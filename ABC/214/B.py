# coding: utf-8
# Your code here!
        
def main():
    S, T = map(int, input().split())
    Ans = 0
    for a in range(S+1):
        for b in range(S+1-a):
            for c in range(S+1-(a+b)):
                if a*b*c <= T:
                    Ans += 1
    print(Ans)
                
if __name__ == "__main__":
    main()