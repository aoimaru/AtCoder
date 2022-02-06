# coding: utf-8
# Your code here!

def main():
    N = int(input())
    HN = list(map(int, input().split()))
    while HN:
        com = HN.pop(0)
        if not HN:
            break
        if com >= HN[0]:
            break
    
    print(com)
            
if __name__ == "__main__":
    main()