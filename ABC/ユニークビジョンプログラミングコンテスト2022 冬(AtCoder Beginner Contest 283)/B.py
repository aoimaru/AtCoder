# coding: utf-8
# Your code here!


def main():
    _ = input()
    AN = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0]==1:
            AN[query[1]-1]=query[2]
        else:
            print(AN[query[1]-1])

if __name__ == "__main__":
    main()
