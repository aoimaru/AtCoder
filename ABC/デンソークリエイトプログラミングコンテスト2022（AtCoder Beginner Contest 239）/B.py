# coding: utf-8
# Your code here!

def main():
    X = int(input())
    comp = X/10
    if X >= 0:
        print(X//10)
    else:
        X = X*(-1)
        if X%10 == 0:
            X = X//10
            print(X*(-1))
        else:
            X = X//10
            print((X+1)*(-1))
    
if __name__ == "__main__":
    main()
