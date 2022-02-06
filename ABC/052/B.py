# coding: utf-8
# Your code here!

def main():
    X = 0
    N = int(input())
    S = input()
    Xs = []
    for s in S:
        if s == "I":
            X += 1
        else:
            X -= 1
        Xs.append(X)
    ans = max(Xs) if max(Xs) >= 0 else 0
    print(ans)    

if __name__ == "__main__":
    main()
