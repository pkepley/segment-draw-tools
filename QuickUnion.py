class QuickUnion:
    def __init__(self, N):
        self.id = list(range(N))
    
    def root(self, i):
        while (i != self.id[i]):
            i = self.id[i]
        return i

    def unite(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j

    def find(self, p, q):
        return self.root(p) == self.root(q)

    def updateAll(self):
        for i in range(len(self.id)):
            self.id[i] = self.root(i)
