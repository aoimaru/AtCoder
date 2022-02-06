# coding: utf-8
# Your code here!

def main():
    P26 = list(map(lambda x: int(x)-1, input().split()))
    alphabets = [chr(cnt) for cnt in range(97, 97+26)]
    Ans = ""
    for P in P26:
        Ans += alphabets[P]
    print(Ans)

if __name__ == "__main__":
    main()