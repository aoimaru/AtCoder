# coding: utf-8
# Your code here!

def main():
    N = int(input())
    AN = list(map(int, input().split()))
    AN.insert(0, 0)
    Ans = []
    for A in AN:
        Ans = [An+A for An in Ans]
        Ans.append(A)
        Ans = [An%360 for An in Ans]
    Ans.sort()
    Ans.insert(0, 0)
    Ans.append(360)
    answer = 0
    for cnt in range(1 ,len(Ans)):
        answer = max(Ans[cnt]-Ans[cnt-1], answer)
    print(answer)
        
if __name__ == "__main__":
    main()
