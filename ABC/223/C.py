# coding: utf-8
# Your code here!

def main():
    N = int(input())
    Cum = [0]*(N+1)
    AN = [0]; BN = [0]
    AN2 = [0]*(N+1)
    for cnt in range(N):
        A, B = map(int, input().split())
        AN.append(A); BN.append(B)
        Cum[cnt+1] = Cum[cnt]+(A/B)
        AN2[cnt+1] = AN2[cnt]+A

    Mx = Cum[-1]/2

    comp = min([cn for cn, cum in enumerate(Cum) if cum >= Mx])-1
    init = AN2[comp]
    diff = Mx-Cum[comp]
    print(init+(diff*BN[comp+1]))
    
if __name__ == "__main__":
    main()
