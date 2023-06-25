class Matrix:
    def __init__(self, m):
        self.m = m
        self.shape = (len(m),len(m[0]))
        self.indices = [(i,j)
                        for i in range(self.shape[0])
                        for j in range(self.shape[1])]
        self.tmp = m
    
    m = Matrix([[1,2,3,18],[0,3,4,7],[1,21,44,41],[1,0,1,22]])
    print(m)