# coding: utf-8
# Your code here!
# 配列のアクセスをマイナスですると通った

def main():
    S = input()
    while S:
        if S[-7:] == "dreamer":
            S = S[:-7]
            continue
        elif S[-6:] == "eraser":
            S = S[:-6]
            continue
        elif S[-5:] == "dream":
            S = S[:-5]
            continue
        elif S[-5:] == "erase":
            S = S[:-5]
            continue
        else:
            break
    if S:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()


# coding: utf-8
# Your code here!
#こっちは通らない

def main():
    S = input()
    while S:
        if S[:7] == "dreamer":
            S = S[7:]
            continue
        elif S[:6] == "eraser":
            S = S[6:]
            continue
        elif S[:5] == "dream":
            S = S[5:]
            continue
        elif S[:5] == "erase":
            S = S[5:]
            continue
        else:
            break
    if S:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()