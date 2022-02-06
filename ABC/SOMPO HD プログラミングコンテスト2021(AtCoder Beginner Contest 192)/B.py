# coding: utf-8
# Your code here!

def main():
    S = input()
    lowers = [cnt for idx, cnt in enumerate(S) if idx%2 == 0]
    uppers = [cnt for idx, cnt in enumerate(S) if idx%2 == 1]
    
    lower = "".join(lowers)
    upper = "".join(uppers)
    
    if len(S) == 1:
        if lower.islower():
            print("Yes")
        else:
            print("No")
    else:
        if lower.islower() and upper.isupper():
            print("Yes")
        else:
            print("No")
            
if __name__ == "__main__":
    main()
