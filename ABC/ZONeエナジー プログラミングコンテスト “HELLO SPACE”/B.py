# coding: utf-8
# Your code here!

def main():
    N, D, H = map(int, input().split())
    print(D, H)
    Graph = {}
    tilts = []
    for _ in range(N):
        d, h = map(int, input().split())
        d_n = D-d; h_n = H-h
        Graph[(d, h)] = h_n/d_n
        tilts.append(h_n/d_n)
    
    for key, value in Graph.items():
        print(key, value)
    
    Coor = [key for key, value in Graph.items() if value == min(tilts)][0]
    print(Coor)
    print(H-Coor[1], D-Coor[0])
    A = (H-Coor[1])/(D-Coor[0])
    print(A)
    B = D-A*H
    if B <= 0:
        print(float(0))
    else:
        print(B)
    
         


if __name__ == "__main__":
    main()