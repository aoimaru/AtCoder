# coding: utf-8
# Your code here!


def main():
    N = int(input())
    Lows, Ups = set(), set()
    cnt = 1
    while cnt*cnt <= N:
        if N%cnt == 0:
            Lows.add(cnt)
            Ups.add(N//cnt)
        cnt += 1
    items = list(Lows|Ups)
    items.sort()
    for item in items:
        print(item)

if __name__ == "__main__":
    main()
