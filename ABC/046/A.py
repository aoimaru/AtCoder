# coding: utf-8
# Your code here!

def main():
    color = list(map(int, input().split()))
    print(len(set(color)))

if __name__ == "__main__":
    main()