# coding: utf-8
# Your code here!
VOWELS = [
        "a",
        "i",
        "u",
        "e",
        "o"
    ]

def main():
    C = input()
    if C in VOWELS:
        print("vowel")
    else:
        print("consonant")
    
if __name__ == "__main__":
    main()