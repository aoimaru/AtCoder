# coding: utf-8
# Your code here!

def main():
    N = int(input())
    Map = {}
    for _ in range(N):
        S = input()
        if not S in Map:
            Map[S] = 0
        Map[S] += 1
    Answers = sorted(Map.items(), key=lambda x:x[1], reverse=True)
    Nums = []
    for Answer in Answers:
        Nums.append(Answer[1])
    maxNum = max(Nums)
    
    Cands = [Answer[0] for Answer in Answers if Answer[1] == maxNum]
    Cands.sort()
    print(Cands[0])
    
if __name__ == "__main__":
    main()
