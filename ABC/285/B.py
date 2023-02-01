# coding: utf-8
# Your code here!

def main():
    N = int(input())
    SN = list(input())
    
    for RN in range(1, N):
        SS = list()
        for i in range(len(SN)-RN):
            if SN[i]==SN[i+RN]:
                break
            SS.append(i)
        if SS:
            print(max(SS)+1)
        else:
            print(0)
        
if __name__ == "__main__":
    main()