# coding: utf-8
# Your code here!
answers = list()

def rec(seq):
    if len(seq)==N:
        if (seq==P) or (seq==Q):
            answers.append(True)
        else:
            answers.append(False)
    for num in nums:
        if num in seq:
            continue
        rec(seq+num)

def main():
    global N
    N = int(input())
    global nums
    nums = [str(num) for num in range(1, N+1)]
    global P, Q
    P = input().replace(" ", "")
    Q = input().replace(" ", "")
    
    rec("")
    ans = [key for key, answer in enumerate(answers) if answer==True]
    print(abs(max(ans)-min(ans)))

if __name__ == "__main__":
    main()