# coding: utf-8
# Your code here!

def main():
    S = list(map(int, list(input())))
    answer = [cnt for cnt in range(10) if cnt not in S]
    print(answer[0])

if __name__ == "__main__":
    main()
