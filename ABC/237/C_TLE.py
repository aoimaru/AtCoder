# coding: utf-8
# Your code here!

def main():
    S = list(input())
    while S:
        com = S.pop(-1)
        if com != "a":
            S.append(com)
            break
    while S:
        com = S.pop(0)
        if com != "a":
            S.insert(0, com)
            break
    while len(S)>2:
        first = S.pop(0)
        second = S.pop(-1)
        if first != second:
            print("No")
            break
    else:
        print("Yes")

if __name__ == "__main__":
    main()
