# coding: utf-8
# Your code here!

CTS = [
        "ABC",
        "ARC",
        "AGC",
        "AHC"
    ]

def main():
    S1 = input()
    CTS.remove(S1)
    S2 = input()
    CTS.remove(S2)
    S3 = input()
    CTS.remove(S3)
    print(CTS[0])
    
if __name__ == "__main__":
    main()