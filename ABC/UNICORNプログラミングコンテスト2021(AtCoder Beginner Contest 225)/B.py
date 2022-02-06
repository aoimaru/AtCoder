# coding: utf-8
# Your code here!

def main():
    N = int(input())
    Stars = {}
    for _ in range(N-1):
        A, B = map(int, input().split())
        if not A in Stars:
            Stars[A] = set()
        Stars[A].add(B)
        if not B in Stars:
            Stars[B] = set()
        Stars[B].add(A)
        
    for value in Stars.values():
        if len(value) == N-1:
            print("Yes")
            break
    else:
        print("No")
        
if __name__ == "__main__":
    main()
