import numpy as np
import matplotlib.tri as mtri
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

class RegularImageTriangulator:
    def __init__(self, img, ncol=0, nrow=0):
        self.img = img
        self.nx = self.img.shape[1]
        self.ny = self.img.shape[0]
        self.np = self.nx * self.ny

        if ncol == 0 and nrow == 0:
            self.ncol = 20
            self.nrow = int((self.ny * self.ncol) /  self.nx)

        elif ncol == 0 and nrow != 0:
            self.nrow = nrow
            self.ncol = int((self.nx * self.nrow) /  self.ny)

        elif ncol != 0 and nrow == 0:
            self.ncol = ncol
            self.nrow = int((self.ny * self.ncol) /  self.nx)

        else:
            self.ncol = ncol
            self.nrow = nrow

        self.htri = self.ny / self.nrow
        self.wtri = self.nx / self.ncol

        self.ps = np.array([(self.htri * i, self.wtri * j) 
                            for i in range(0, self.nrow)
                            for j in range(0, self.ncol) ], dtype=int)
        self.xs = self.ps[:,1]
        self.ys = -self.ps[:,0]
        self.tri = mtri.Triangulation(self.xs, self.ys)

    def plotLinTriang(self, cmap = "Greys_r"):
        if self.img.ndim > 2:
            img = rgb2gray(self.img)
            img2 = img[-self.ys, self.xs]
        else:
            img2 = self.img[-self.ys, self.xs]
        lin_interp = mtri.LinearTriInterpolator(self.tri, img2.flatten())
        zs_lin = lin_interp(self.xs, self.ys)
        
        fig, ax = plt.subplots()

        ax.contourf(self.xs.reshape(self.nrow,self.ncol), 
                    self.ys.reshape(self.nrow,self.ncol), 
                    zs_lin.reshape(self.nrow,self.ncol),
                    cmap = cmap)
        ax.axis('off')
        ax.set_aspect('equal')
        return fig, ax
