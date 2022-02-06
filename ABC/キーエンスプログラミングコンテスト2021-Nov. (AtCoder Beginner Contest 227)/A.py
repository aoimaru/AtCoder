# coding: utf-8
# Your code here!

def main():
    N, K, A = map(int, input().split())
    Persons = [cnt for cnt in range(1, N+1)]
    Front = Persons[A-1:]
    Back = Persons[:A-1]
    New = Front+Back
    
    cnt = 0
    while True:
        cnt += 1
        comp = New.pop(0)
        New.append(comp)
        if cnt == K:
            break
    print(New[-1])
    
if __name__ == "__main__":
    main()
