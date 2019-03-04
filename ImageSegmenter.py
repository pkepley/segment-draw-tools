import QuickUnion

class ImageSegmenter:
    def __init__(self, img):        
        self.img = img
        #self.flat_img = self.img.flatten()
        self.nx = self.img.shape[0]
        self.ny = self.img.shape[1]
        self.np = self.nx * self.ny
        self.qu = QuickUnion.QuickUnion(self.np)

    def __ij_to_k__(self, i, j):
        return i * self.ny + j
        
    def __k_to_ij__(self, k):
        i = int(k / self.ny)
        j = k % self.ny
    
    def constructComps(self):
        for i in range(1, self.nx-1):
            for j in range(1, self.ny-1):
                if self.img[i,j] == 1:
                    k = self.__ij_to_k__(i,j)
                    nbrs  =  self.img[i-1:i+2, j-1:j+2].flatten()
                    for l in [0,1,2,3,5,6,7,8]:
                        if nbrs[l] == 1:
                            ii = int((i - 1) + (l / 3))
                            jj = int((j - 1) + (l % 3))
                            kk = self.__ij_to_k__(ii,jj)
                            if not self.qu.find(k, kk):
                                self.qu.unite(k, kk)
        self.qu.updateAll()
