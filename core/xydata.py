
from core.calc import GenConst,GeneCalc,ChartCalc



class XYdata:

    def __init__(self):

        self.file = None
        self.n_points = None
        self.subseqList = None

        

    def setSubseqList(self, l_str):
        self.subseqList = l_str
        
    def setPointsCount(self,n):
        self.n_points = n

    def setFileName(self, str):
        self.file = str

    
    
    
    def readGenomeFile(self):
        self.seq = GenConst()
        self.seq.genome_read(self.file)

    def getXYdata(self,subseq):

        
        

        genObj = GeneCalc(subseq,self.seq.genes)
        genObj.calcSubseqPos()
        


        calcObj = ChartCalc(genObj.positions_in_gene)
        calcObj.setPointsCount(self.n_points)
        calcObj.subseqDensity()
        self.Ydata = calcObj.data4plot
        self.Xdata = []
        for i in range(self.n_points): self.Xdata.append(i/self.n_points + 1/(2*self.n_points))
        return([self.Xdata, self.Ydata])

    def getXYdataList(self):
        self.readGenomeFile()
        self.xy_data_list = []
        for subseq in self.subseqList:
            self.xy_data_list.append(self.getXYdata(subseq))
        return(self.xy_data_list)