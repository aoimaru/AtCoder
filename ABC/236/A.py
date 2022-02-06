# coding: utf-8
# Your code here!

def main():
    S = list(input())
    A, B = map(lambda x: int(x)-1, input().split())
    S[A], S[B] = S[B], S[A]
    print("".join(S))
    
if __name__ == "__main__":
    main()
