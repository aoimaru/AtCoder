# coding: utf-8
# Your code here!

def gcd(l, m):
    """
        再帰関数: 分かりやすい例
    """
    cnt = l%m
    if cnt==0:
        return m
    else:
        # この部分: comを使用しているのがポイント
        com = gcd(m, cnt) 
        return com
        
def gcd2(l, m):
    """
        再帰関数: 分かりにくい例
    """
    cnt = l%m
    if cnt==0:
        return m
    else:
        return gcd(m, cnt)
        
def main():
    A, B = map(int, input().split())
    print(gcd(A, B))
    
    
if __name__ == "__main__":
    main()
