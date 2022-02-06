# coding: utf-8
# Your code here!
# 半分くらいwarning

def main():
    X, Y, A, B = map(int, input().split())
    number = X
    score = 0
    flag = 0
    while True:
        number = min(number*A, number+B)
        if number >= Y:
            break
        if number*A >= B:
            flag = 1
            break
        score += 1
    if flag == 0:
        print(score)
    else:
        score += Y//number
        print(score)
        
if __name__ == "__main__":
    main()
