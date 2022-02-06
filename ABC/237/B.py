# coding: utf-8
# Your code here!

def main():
    H, W = map(int, input().split())
    Table = []
    for _ in range(H):
        Table.append(list(map(int, input().split())))
    Table = list(zip(*Table))
    for tab in Table:
        ans = " ".join(map(str, tab))
        print(ans)

if __name__ == "__main__":
    main()
