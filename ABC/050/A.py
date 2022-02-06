# coding: utf-8
# Your code here!

def main():
    A, OP, B = input().split()
    if OP == "+":
        print(int(A)+int(B))
    else:
        print(int(A)-int(B))

if __name__ == "__main__":
    main()