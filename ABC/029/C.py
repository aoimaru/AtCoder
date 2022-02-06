# coding: utf-8
# Your code here!

def extract(comps, count):
    if count >= N:
        global RT
        RT = comps
        return
    count += 1
    args = []
    for comp in comps:
        args.append(comp+"a")
        args.append(comp+"b")
        args.append(comp+"c")
    extract(args, count)
    
def main():
    global N
    N = int(input())
    extract(["a", "b", "c"], 1)
    for rt in RT:
        print(rt)

if __name__ == "__main__":
    main()