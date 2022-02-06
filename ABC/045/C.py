# coding: utf-8
# Your code here!

def main():
    S = list(input())
    lenS = len(S)-1
    comps = []
    for i in range(2**lenS):
        comp = [""]*lenS
        for j in range(lenS):
            if ((i>>j & 1)):
                comp[j] = "+"
        comps.append(comp)
    Ans = 0
    for comp in comps:
        formula = ""
        for s, com in zip(S, comp):
            formula += s+com
        formula += S[-1]
        Ans += eval(formula)
    print(Ans)
if __name__ == "__main__":
    main()