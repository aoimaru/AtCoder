# coding: utf-8
# Your code here!

def rec(visited):
    if len(visited)>=N:
        return 1
    answer = 0
    for nt in Table[visited[-1]]:
        if not nt in visited:
            answer += rec(visited+nt)
    return answer
        
def main():
    global N, M
    N, M = map(int, input().split())
    global Table
    Table = dict()
    for _ in range(M):
        A, B = input().split()
        if not A in Table:
            Table[A] = list()
        Table[A].append(B)
        if not B in Table:
            Table[B] = list()
        Table[B].append(A)
    
    answer = rec("1")
    print(answer)

if __name__ == "__main__":
    main()