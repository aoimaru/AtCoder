# coding: utf-8
# Your code here!

def main():
    N = int(input())
    if N>=42:
        N = N+1
    N = str(N)
    Ans = str(N).zfill(3)
    print("AGC{}".format(Ans))
    
if __name__ == "__main__":
    main()
