# coding: utf-8
# Your code here!

def main():
    A, B = input().split()
    A = list(A)
    A.reverse()
    B = list(B)
    B.reverse()
    for a, b in zip(A, B):
        if int(a)+int(b) >= 10:
            print("Hard")
            break
    else:
        print("Easy")
    
if __name__ == "__main__":
    main()
