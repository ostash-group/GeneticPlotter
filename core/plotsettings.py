

class PlotSettings:

    def __init__(self):

        self.n_points = None
        self.xy_list = None
        self.colors = None
        self.subseq_list = None

    def setSubseqList(self,l_str):
        self.subseq_list = l_str
    def getSubseqList(self):
        return(self.subseq_list)



    def setColorsList(self,colors):
        self.colors = colors
    def getColorsList(self):
        return(self.colors)
    
    

    def setPointsCount(self,n):
        self.n_points = n
    def getPointsCount(self):
        return(self.n_points)


    def setXYdataList(self,l):
        self.xy_list = l
    def getXYdataList(self):
        return(self.xy_list)