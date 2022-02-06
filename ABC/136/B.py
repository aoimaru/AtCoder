# coding: utf-8
# Your code here!

def main():
    N = int(input())
    Ans = 0
    for count in range(1, N+1):
        if len(str(count))%2 == 1:
            Ans += 1
    print(Ans)

if __name__ == "__main__":
    main()
