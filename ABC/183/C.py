# coding: utf-8
# Your code here!
import copy

def rec(cost, visit):
    if len(visit) == N:
        cost += TN[visit[-1]][0]
        if cost == K:
            return 1
        return 0
    answer = 0
    for n in range(N):
        if not n in visit:
            visited = copy.copy(visit)
            visited.append(n)
            ans = rec(cost+TN[visit[-1]][n], visited)
            answer += ans
    return answer
        
def main():
    global N, K
    N, K = map(int, input().split())
    global TN
    TN = list()
    for _ in range(N):
        TN.append(list(map(int, input().split())))
    
    answer = rec(0, [0])
    print(answer)


if __name__ == "__main__":
    main()