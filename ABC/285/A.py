# coding: utf-8
# Your code here!

def main():
    A, B = map(int, input().split())
    if A==B*2:
        print("Yes")
    elif A==B*2+1:
        print("Yes")
    elif A*2==B:
        print("Yes")
    elif A*2+1==B:
        print("Yes")
    else:
        print("No")
        
if __name__ == "__main__":
    main()