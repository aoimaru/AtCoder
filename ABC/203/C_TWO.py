# coding: utf-8
# Your code here!

def main():
    N, K = map(int, input().split())
    Data = {}
    for _ in range(N):
        A, B = map(int, input().split())
        Data[A] = B
    
    Data = {
            data[0]: data[1] for data in sorted(Data.items())
        }
    
    print(Data)
    
     
    
if __name__ == "__main__":
    main()