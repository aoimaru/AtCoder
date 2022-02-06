# coding: utf-8
# Your code here!
import sys

def main():
    N = list(map(int, input()))
    if sum(N) == 0:
        print("Yes")
        sys.exit()
    while True:
        if N[-1] != 0:
            break
        N.pop(-1)

    Nlength = len(N)
    for cnt in range(int(Nlength//2)+1):
        if N[cnt] != N[Nlength-cnt-1]:
            print("No")
            break
    else:
        print("Yes")
if __name__ == "__main__":
    main()