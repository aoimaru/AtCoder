# coding: utf-8
# Your code here!

#順序維持のパッケージ
from bisect import bisect_left

def main():
    H, W, N = map(int, input().split())
    As = []; Bs = []
    for _ in range(N):
        A, B = map(int, input().split())
        As.append(A); Bs.append(B)
    
    A_s = list(set(As.copy()))
    B_s = list(set(Bs.copy()))
    
    A_s.sort(); B_s.sort()
    
    # bisect_left 使い方
    # index = bisect_left(
    #         a: ソート済みのリスト,
    #         x: 挿入したい値, 
    #         lo: 探索範囲の下限,
    #         hi: 探索範囲の上限
    #     )
    # index: 挿入された後での挿入した値のインデックスが帰ってくる
    
    for cnt in range(N):
        print(bisect_left(A_s, As[cnt])+1, bisect_left(B_s, Bs[cnt])+1)
    
if __name__ == "__main__":
    main()