# coding: utf-8
# Your code here!
import copy
import math

X_KEY = 0
Y_KEY = 1
costs = list()

def rec(visited, cost):
    if len(visited) == N:
        costs.append(cost)
    for nxt in range(N):
        if nxt in visited:
            continue
        x_cost = abs(
            Table[visited[-1]][X_KEY]-Table[nxt][X_KEY]
            )
        y_cost = abs(
            Table[visited[-1]][Y_KEY]-Table[nxt][Y_KEY]
            )
        n_visited = copy.copy(visited)
        n_visited.append(nxt)
        rec(n_visited, cost+math.sqrt(x_cost**2+y_cost**2))
    
def main():
    global N
    N = int(input())
    global Table
    Table = list()
    for _ in range(N):
        X, Y = map(int, input().split())
        Table.append([X, Y])
    for start in range(N):
        rec([start], 0)
    
    print(sum(costs)/len(costs))

if __name__ == "__main__":
    main()