# coding: utf-8
# Your code here!

def main():
    S = list(input())
    for ids, s in enumerate(S):
        if s == "A":
            first = ids
            break
    
    for ids, s in enumerate(S[::-1]):
        if s == "Z":
            second = ids
            break
    second = len(S)-second
    
    print(second-first)
    
if __name__ == "__main__":
    main()