# coding: utf-8
# Your code here!


def main():
    N = int(input())
    Ims = [0]*N
    for _ in range(N):
        A, B = map(int, input().split())
        Ims[A-1] += 1
        if B < N:
            Ims[B] -= 1
    for i in range(N-1):
        Ims[i+1] += Ims[i]
        Ims[i] %= 2
    Ims[N-1] %= 2    
        
    print(Ims)
    
if __name__ == "__main__":
    main()


# coding: utf-8
# Your code here!


def main():
    N = int(input())
    Ims = {}
    A, B = map(int, input().split())
    Ims[A-1] = 1
    Ims[B] = -1
    for _ in range(N-1):
        A, B = map(int, input().split())
        if not A-1 in Ims:
            Ims[A-1] = 0
        Ims[A-1] += 1
        if not B in Ims:
            Ims[B] = 0
        Ims[B] -= 0    
    print(Ims)
    
    com = sorted(Ims.items())
    
    Ims = list(map(lambda x: x[1], com))
    print(Ims)
    for i in range(len(com)-1):
        Ims[i+1] += Ims[i]
        Ims[i] %= 2
    Ims[len(com)-1] %= 2
    print(Ims)
    
if __name__ == "__main__":
    main()
