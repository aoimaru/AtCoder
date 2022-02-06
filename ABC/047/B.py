# coding: utf-8
# Your code here!

def main():
    W, H, N = map(int, input().split())
    Tables = [[0]*W for _ in range(H)]
    for _ in range(N):
        X, Y, A = map(int, input().split())
        if A == 1:
            for hg in range(H):
                for wd in range(X):
                    Tables[hg][wd] = 1
        elif A == 2:
            for hg in range(H):
                for wd in range(X, W):
                    Tables[hg][wd] = 1
        elif A == 3:
            for hg in range(Y):
                for wd in range(W):
                    Tables[hg][wd] = 1
        else:
            for hg in range(Y, H):
                for wd in range(W):
                    Tables[hg][wd] = 1
                    
    Ans = 0
    for Table in Tables:
        Ans += sum(Table)
    print((W*H)-Ans)
        
if __name__ == "__main__":
    main()