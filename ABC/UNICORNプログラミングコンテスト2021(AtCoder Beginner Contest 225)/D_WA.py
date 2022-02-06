# coding: utf-8
# Your code here!


# memberメソッドが違う, 再帰的に辿っていく必要がある

class UnionFind(object):
    """
    ナイーブなUnionFind木
    - findメソッドで繋ぎかえる効率化を行なっていない
    """
    def __init__(self, n):
        self._n = n
        self._parents = [-1]*n
        
    def find(self, x):
        if self._parents[x] < 0:
            return x
        else:
            return self.find(self._parents[x])
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        self._parents[x] += self._parents[y]
        self._parents[y] = x
    
    def sepalate(self, y):
        self._parents[y] = -1
        
    def size(self, x):
        return -self._parents[self.find(x)]
    
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self._n) if self.find(i) == root]
    
    @property
    def parents(self):
        return self._parents


def main():
    N, Q = map(int, input().split())
    
    uf = UnionFind(N+1)
    for _ in range(Q):
        QR = list(map(int, input().split()))
        if QR[0] == 1:
            uf.union(QR[1], QR[2])
        elif QR[0] == 2:
            uf.sepalate(QR[2])
        else:
            members = uf.members(QR[1])
            mem0 = str(len(members))
            mem1 = " ".join(map(str, members))
            print("{} {}".format(mem0, mem1))
            
if __name__ == "__main__":
    main()
