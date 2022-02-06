# coding: utf-8
# Your code here!

def extract(comps, count):
    if count >= NL:
        global RT
        RT = comps
        return
    count += 1
    args = []
    for comp in comps:
        for F in Fs:
            args.append(comp+F)
    extract(args, count)

def main():
    N, _ = map(int, input().split())
    NS = int(str(N)[0])
    global NL
    NL = len(str(N))
    Ds = list(map(int, input().split()))
    Es = [num for num in range(10) if not num in Ds]
    global Fs
    Fs = [str(num) for num in Es]
    if len(Es) == 1:
        Start = Es[0]
    else:
        Start = [num for num in Es if num>=NS][0]
    extract([str(Start)], 1)
    for rt in RT:
        if int(rt) >= N:
            print(rt)
            break

if __name__ == "__main__":
    main()