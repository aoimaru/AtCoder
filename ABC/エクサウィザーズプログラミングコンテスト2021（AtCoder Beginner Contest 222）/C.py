# coding: utf-8
# Your code here!

def main():
    N, M = map(int, input().split())
    Rank = [cnt for cnt in range(N*2)]
    Hands = {}
    for cnt in range(N*2):
        Hands[cnt] = list(input())
    
    Results = {cnt: 0 for cnt in range(N*2)}

    for _ in range(M):
        for cnt in range(N):
            FmrKey = Rank[cnt*2]
            LtrKey = Rank[cnt*2+1]
            Fmr = Hands[FmrKey].pop(0)
            Ltr = Hands[LtrKey].pop(0)
            res = Fmr+Ltr
            if res == "GC":
                Results[FmrKey] += 1
            elif res == "GP":
                Results[LtrKey] += 1
            elif res == "CP":
                Results[FmrKey] += 1
            elif res == "CG":
                Results[LtrKey] += 1
            elif res == "PG":
                Results[FmrKey] += 1
            elif res == "PC":
                Results[LtrKey] += 1
            else:
                pass

        Results2 = sorted(Results.items(), key=lambda x:x[1], reverse=True)
        Rank = [cnt[0] for cnt in Results2]

    for ans in Rank:
        print(ans+1)
        
            
if __name__ == "__main__":
    main()
