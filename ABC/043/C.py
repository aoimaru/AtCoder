# coding: utf-8
# Your code here!
import sys

def main():
    N = int(input())
    As = list(map(int, input().split()))
    if set(As) == 1:
        print(0)
        sys.exit()
    y_1 = sum(As)//len(As)
    y_2 = (sum(As)//len(As))+1
    
    ans_1 = sum([(x-y_1)**2 for x in As])
    ans_2 = sum([(x-y_2)**2 for x in As])
    print(min(ans_1, ans_2))
    
if __name__ == "__main__":
    main()