# coding: utf-8
# Your code here!

def main():
    A, B, K = map(int, input().split())
    answer = 0
    while A*K**answer < B:
        answer += 1
    print(answer)

if __name__ == "__main__":
    main()
