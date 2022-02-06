# coding: utf-8
# Your code here!

def main():
    N, K = map(int, input().split())
    # 一番左のボールは, K通り, そのあとは(K-1)通り, それが(N-1)個あるので
    # K*((K-1)**(N-1))通り
    if N == 1:
        print(K)
    else:
        Ans = K*(K-1)**(N-1)
        print(Ans)

if __name__ == "__main__":
    main()
