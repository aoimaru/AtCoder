# coding: utf-8
# Your code here!
import sys

def main():
    S = list(input())
    T = list(input())
    if S == T:
        print("Yes")
        sys.exit()
    for i in range(len(S)-1):
        S[i], S[i+1] = S[i+1], S[i]
        if S == T:
            print("Yes")
            break
        S[i], S[i+1] = S[i+1], S[i]
    else:
        print("No")
    
if __name__ == "__main__":
    main()
