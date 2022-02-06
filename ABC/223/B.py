# coding: utf-8
# Your code here!

def main():
    S = list(input())
    Res = []
    init = "".join(S)
    Res.append(init)
    for _ in range(len(S)):
        comp = S.pop(0)
        S.append(comp)
        Res.append("".join(S))
    
    Res.sort()
    print(min(Res))
    print(max(Res))

if __name__ == "__main__":
    main()
