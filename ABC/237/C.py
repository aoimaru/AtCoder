# coding: utf-8
# Your code here!

def main():
    S = list(input())
    first = len(S)
    second = len(S)
    for cnt in range(len(S)):
        if S[cnt] != "a":
            first = cnt
            break
    for cnt in range(len(S)):
        if S[-(cnt+1)] != "a":
            second = cnt
            break
    
    if second > first:
        S = S[:len(S)-(second-first)]
        
    for cnt in range(len(S)//2):
        if S[cnt] != S[-(cnt+1)]:
            print("No")
            break
    else:
        print("Yes")
if __name__ == "__main__":
    main()
