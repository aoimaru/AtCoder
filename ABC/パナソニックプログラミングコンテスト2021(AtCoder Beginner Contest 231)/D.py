# coding: utf-8
# Your code here!
import sys
from collections import defaultdict

class UnionFind():
    """
    Union Find木クラス

    Attributes
    --------------------
    n : int
        要素数
    root : list
        木の要素数
        0未満であればそのノードが根であり、添字の値が要素数
    rank : list
        木の深さ
    """

    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.root[self.find(x)]

    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        return len(self.roots())

    def group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

def main():
    N, M = map(int, input().split())
    Graph = {}
    uf = UnionFind(N)
    for _ in range(M):
        uflag1 = 0
        uflag2 = 0
        A, B = map(int, input().split())
        if not A in Graph:
            Graph[A] = []
            uflag1 = 1
        if not B in Graph:
            Graph[B] = []
            uflag2 = 1
        Graph[A].append(B)
        if len(Graph[A])>2:
            print("No1")
            sys.exit()
        Graph[B].append(A)
        if len(Graph[B])>2:
            print("No2")
            sys.exit()
        if uflag1 == 0 and uflag2 == 0:
            if uf.find(A) == uf.find(B):
                print("No3")
                sys.exit()
        uf.unite(A, B)
    else:
        print("Yes")

if __name__ == "__main__":
    main()
