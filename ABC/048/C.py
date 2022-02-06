# coding: utf-8
# Your code here!
def main():
    N, X = map(int, input().split())
    As = list(map(int, input().split()))
    Ans = 0
    for cnt in range(N-1):
        if As[cnt]+As[cnt+1] > X:
            Ans += As[cnt]+As[cnt+1]-X
            if As[cnt] > As[cnt+1]:
                As[cnt] = X-As[cnt+1]
            else:
                As[cnt+1] = X-As[cnt]
    print(Ans)
if __name__ == "__main__":
    main()



# coding: utf-8
# Your code here!
# こっちが正解
def main():
    N, X = map(int, input().split())
    As = list(map(int, input().split()))
    Ans = 0
    if As[0] > X:
        Ans += As[0]-X
        As[0] = X
        
    for cnt in range(N-1):
        if As[cnt]+As[cnt+1] > X:
            Ans += As[cnt]+As[cnt+1]-X
            As[cnt+1] = X-As[cnt]
    print(Ans)
if __name__ == "__main__":
    main()