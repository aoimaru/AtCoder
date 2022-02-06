# coding: utf-8
# Your code here!

def main():
    X = input()
    XN = X.split(".")
    X = int(XN[0])
    Y = int(XN[1][0])
    if Y > 4:
        print(X+1)
    else:
        print(X)

if __name__ == "__main__":
    main()