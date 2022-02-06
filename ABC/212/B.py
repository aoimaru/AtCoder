# coding: utf-8
# Your code here!
import sys

def main():
    Xs = list(map(int, input()))
    if len(set(Xs)) == 1:
        print("Weak")
        sys.exit()
    count = 0
    for ids in range(len(Xs)-1):
        if Xs[ids+1]-Xs[ids] == 1 or Xs[ids+1]-Xs[ids] == -9:
            count += 1
    if count == 3:
        print("Weak")
    else:
        print("Strong")

if __name__ == "__main__":
    main()