# coding: utf-8
# Your code here!

def main():
    A, B, C = map(int, input().split())
    for cnt in range(A, B+1):
        if cnt%C == 0:
            print(cnt)
            break
    else:
        print(-1)

if __name__ == "__main__":
    main()