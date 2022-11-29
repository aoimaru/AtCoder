# coding: utf-8
# Your code here!

def rec(seq):
    if len(seq)>=N:
        print(seq)
        return
    for nt in ["a", "b", "c"]:
        rec(seq+nt)

def main():
    global N
    N = int(input())
    rec("")

if __name__ == "__main__":
    main()
