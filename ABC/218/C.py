# coding: utf-8
# Your code here!
import numpy as np
import copy
import sys

def check(UN):
    snc = []
    tnc = []
    for idu, un in enumerate(UN):
        if "#" in un:
            snc.append(idu)
            for sus, s in enumerate(un):
                if s == "#":
                    tnc.append(sus)
    miny = min(snc)
    maxy = max(snc)
    minx = min(tnc)
    maxx = max(tnc)
    
    Ret = copy.copy(UN[miny: maxy+1, minx: maxx+1,])

    return Ret
        

def main():
    N = int(input())
    SN = []
    for _ in range(N):
        SN.append(list(input()))
    TN = []
    for _ in range(N):
        TN.append(list(input()))
        
    SN = np.array(SN)
    TN = np.array(TN)
    
    SN1 = np.rot90(SN).copy()
    SN2 = np.rot90(SN1).copy()
    SN3 = np.rot90(SN2).copy()
    
    TN1 = np.rot90(TN).copy()
    TN2 = np.rot90(TN1).copy()
    TN3 = np.rot90(TN2).copy()
    
    SNN = [SN, SN1, SN2, SN3]
    TNN = [TN, TN1, TN2, TN3]
    
    for sn in SNN:
        coms = check(sn)
        for tn in TNN:
            comt = check(tn)
            if coms.shape == comt.shape:
                if (coms == comt).all():
                    print("Yes")
                    sys.exit()
    print("No")
            
            
    

if __name__ == "__main__":
    main()