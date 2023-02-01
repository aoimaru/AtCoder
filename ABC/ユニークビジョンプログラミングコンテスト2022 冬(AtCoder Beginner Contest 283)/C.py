# coding: utf-8
# Your code here!

def main():
    S = input()
    
    count = 0
    while len(S)>0:
        if S.startswith("00"):
            S = S[2:]
        else:
            S = S[1:]
        count += 1
    
    print(count)
    
if __name__ == "__main__":
    main()