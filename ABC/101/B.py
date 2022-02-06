# coding: utf-8
# Your code here!

def main():
    N = input()
    SN = 0
    for n in N:
        SN += int(n)
    N = int(N)
    if N%SN == 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
