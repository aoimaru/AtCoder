# coding: utf-8
# Your code here!

def main():
    P = int(input())
    
    A = [1]
    for cnt in range(2, 11):
        A += [A[-1]*cnt]

    Ans = 0
    for B in A[::-1]:
        while P >= B:
            Ans += 1
            P = P-B
    print(Ans)
            
if __name__ == "__main__":
    main()