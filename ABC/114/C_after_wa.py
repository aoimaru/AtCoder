# coding: utf-8
# Your code here!
Nums = ["3", "5", "7"]

def extract(comps=None):
    if not comps:
        comps = ["3", "5", "7"]
    else:
        if len(comps[0]) == Nlength:
            global Items
            Items = comps
            return
    Args = []
    for comp in comps:
        for Num in Nums:
            new_comp = comp + Num
            Args.append(new_comp)
    extract(Args)

def main():
    N = input()
    global Nlength
    Nlength = len(N)
    Nnumber = int(N)
    
    All = 0
    for cnt in range(3, Nlength):
        All += 3**cnt
    
    comp = 0
    for cnt in range(3, Nlength):
        comp += 3*(2**cnt)-3
        
    Ans = All-comp
    
    extract()
    
    for Item in Items:
        if int(Item) >= Nnumber:
            break
        if len(set(list(Item))) == 3:
            Ans += 1
    print(Ans)
            
    
    
if __name__ == "__main__":
    main()