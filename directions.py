import numpy as np

class Directions:

    LEFT = 0
    UP = 1
    DIAG = 2

    def __init__(self, shape):
        self.directions = np.zeros( (shape[0], shape[1], 3 ))
        for i in range(1, shape[1]):
            self.set_directions(0, i, left=True)
        
        for i in range(1, shape[0]):
            self.set_directions(i, 0, up=True)
        self.shape = shape

    def set_directions(self, x, y, left=False, up=False, diag=False):
        self.directions[x][y][self.LEFT] = left
        self.directions[x][y][self.UP] = up
        self.directions[x][y][self.DIAG] = diag

    def is_left(self, x, y):
        return self.directions[x][y][self.LEFT]
    
    def is_up(self, x, y):
       return self.directions[x][y][self.UP]

    def is_diag(self, x, y):
        return self.directions[x][y][self.DIAG]
    