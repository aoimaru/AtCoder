# coding: utf-8
# Your code here!

def main():
    Sdict = {}
    Sdict["a"] = list(input())
    Sdict["b"] = list(input())
    Sdict["c"] = list(input())
    
    comp = "a"
    while True:
        if not Sdict[comp]:
            break
        comp = Sdict[comp].pop(0)
    if comp == "a":
        print("A")
    elif comp == "b":
        print("B")
    else:
        print("C")
    
if __name__ == "__main__":
    main()
