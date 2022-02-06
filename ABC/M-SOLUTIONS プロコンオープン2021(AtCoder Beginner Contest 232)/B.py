# coding: utf-8
# Your code here!
#途中　なんか解けてない

import string
import sys

def main():
    S = list(input())
    T = list(input())
    alpha = list(string.ascii_lowercase)
    Sd = []
    Td = []
    for s, t in zip(S, T):
        Sd.append(alpha.index(s))
        Td.append(alpha.index(t))
    
    sd = []
    td = []
    for cnt in range(len(Sd)-1):
        sd.append(Sd[cnt+1]-Sd[cnt])
        td.append(Td[cnt+1]-Td[cnt])
    
    cS = set(sd)
    cT = set(td)
    if len(cS)!=1:
        print("No")
        sys.exit()
    if len(sT)!=1:
        print("No")
        sys.exit()
    if cS[0] != cT[0]:
        print("No")
        sys.exit()

    for s, t in zip(sd, td):
        if s!=t:
            print("No")
            break
    else:
        print("Yes")

if __name__ == "__main__":
    main()
