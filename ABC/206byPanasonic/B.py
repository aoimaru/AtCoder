import math

def main():
    Number = int(input())
    NP1 = int(math.sqrt(Number*2))
    if NP1*(NP1+1) >= Number*2:
        print(NP1)
    else:
        print(NP1+1)

if __name__ == "__main__":
    main()
