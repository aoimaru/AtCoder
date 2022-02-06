# coding: utf-8
# Your code here!

def main():
    N, W = map(int, input().split())
    Weights = []
    Values = []
    for _ in range(N):
        Value, Weight = map(int, input().split())
        Values.append(Value)
        Weights.append(Weight)
    
    DP = [[0]*(W+1) for _ in range(N+1)]
    
    for hg in range(N):
        for wd in range(W+1):
            if Weights[hg] <= wd:
                DP[hg+1][wd] = max(DP[hg][wd-Weights[hg]]+Values[hg], DP[hg][wd])
            else:
                DP[hg+1][wd] = DP[hg][wd]

    print(DP[-1][-1])            
    
if __name__ == "__main__":
    main()
