# coding: utf-8
# Your code here!

def main():
    N = list(input())
    lim = len(N)
    N.sort(reverse=True)
    M = str()
    # print(N, M)
    Ans = 0
    for _ in range(lim-1):
        M += N.pop(0)
        m = int(M)
        n = "".join(N)
        print(m, n)
        if int(m)*int(n) >= Ans:
            Ans = int(m)*int(n)
    
    print(Ans)
    
if __name__ == "__main__":
    main()
