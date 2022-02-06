# coding: utf-8
# Your code here!

def main():
    _, P = map(int, input().split())
    AN = list(map(int, input().split()))
    count = 0
    for A in AN:
        if A < P:
            count += 1
    print(count)
            
if __name__ == "__main__":
    main()
