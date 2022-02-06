# coding: utf-8
# Your code here!

def main():
    ABC = list(input())
    first = int(ABC[0]+ABC[1]+ABC[2])
    second = int(ABC[1]+ABC[2]+ABC[0])
    third = int(ABC[2]+ABC[0]+ABC[1])
    print(first+second+third)

if __name__ == "__main__":
    main()