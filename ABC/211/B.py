# coding: utf-8
# Your code here!

def main():
    Ss = set()
    for _ in range(4):
        S = input()
        Ss.add(S)
    if len(Ss) == 4:
        print("Yes")
    else:
        print("No")
        
if __name__ == "__main__":
    main()