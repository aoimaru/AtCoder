# coding: utf-8
# Your code here!

def exe(comp):
    comp = comp[::-1]
    ans = 0
    for cnt in range(len(comp)):
        ans += int(comp[cnt])*(K**cnt)
    return ans
    
def main():
    global K
    K = int(input())
    A, B = input().split()
    Ans = exe(A)*exe(B)
    print(Ans)
    
if __name__ == "__main__":
    main()