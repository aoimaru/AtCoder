# coding: utf-8
# Your code here!

def main():
    K, S = map(int, input().split())
    count = 0
    minX = S-2*K if S-2*K >= 0 else 0
    # print("minX", minX)
    for X in range(minX, K+1):
        minY = S-X-K if S-X-K >= 0 else 0
        for Y in range(minY, K+1):
            if S-X-Y >= 0:
                # print("X", X, "Y", Y, "Z", S-X-Y)
                count += 1
    print(count)
            
if __name__ == "__main__":
    main()