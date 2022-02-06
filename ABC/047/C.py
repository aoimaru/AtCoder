# coding: utf-8
# Your code here!

def main():
    Board = input()
    Ans = 0
    for cnt in range(1, len(Board)):
        if Board[cnt] != Board[cnt-1]:
            Ans += 1
    print(Ans)
    
if __name__ == "__main__":
    main()