# coding: utf-8
# Your code here!
def main():
    Q = int(input())
    QN = []
    for _ in range(Q):
        q = input()
        if q[0] == "1":
            QN.append(int(q[2]))
        elif q[0] == "2":
            pop = QN.pop(0)
            print(pop)
        elif q[0] == "3":
            QN.sort()
        
if __name__ == "__main__":
    main()