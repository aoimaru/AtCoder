# coding: utf-8
# Your code here!

def main():
    N = int(input())
    As = list(map(int, input().split()))
    Dic = {(ids+1): A for ids, A in enumerate(As)}
    newDic = sorted(Dic.items(), key=lambda x:x[1])
    print(newDic[-2][0])
    
if __name__ == "__main__":
    main()