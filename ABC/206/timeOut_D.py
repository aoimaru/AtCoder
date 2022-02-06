# coding: utf-8
# Your code here!


def main():
    N, Q = map(int, input().split())
    An = list(map(int, input().split()))
    Tr = [count for count in range(1, An[-1]+1) if not count in An]
    for _ in range(Q):
        K = int(input())
        if K <= len(Tr):
            print(Tr[K-1])
        else:
            print(max(An)+(K-len(Tr)))
    
if __name__ == "__main__":
    main()
