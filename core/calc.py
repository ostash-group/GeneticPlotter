import time
from multiprocessing import Process

class GenConst():
    def __init__(self):
        self.stop_codons = ['TAG','TGA','TAA']
        self.start_codons = ['ATG','GTG','ATT','TTG','ATA','ACG','CTG']
        self.genes = [];
                     
        #raw genome string
        self.gene_str = ''
        
        #nucleotides for combination
        self.nucl = 'ATGC'
        
        

        self.codons = self.get_cods()
        
    # lambda expression for checking gene for correctness
    def check(self,str): 
        return(len(str) % 3 == 0 \
               and any(map(str.startswith,self.start_codons)) \
                      and any(map(str.endswith,self.stop_codons)))


    def get_cods(self):
        '''@return - combination of nucleotides'''
        codons = []
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    codons.append(self.nucl[i]+self.nucl[j]+self.nucl[k])
                    
        return codons

    def genome_read(self,path):
        '''read genome file from my disk'''
    
        f = open(path,'r')
        for line in f:
            if line.startswith('>'):
                if self.gene_str and self.check(self.gene_str):
                    self.genes.append(self.gene_str)
                self.gene_str = ''
                continue
            else:
                self.gene_str += line.replace('\n','')
                
        f.close()
        
class GeneCalc:
    def __init__(self,subseq, genes):
        self.positions_in_gene = []
        self.to_plot = []
        self.subseq = subseq
        self.genes = genes
        
        
    def calcSubseqPos4Gene(self,gene):
        '''calculate positions_in_gene for one
           individual gene'''
        pos = 0
        positions = []
        length = len(gene)
        # incredible optimization
        appnd = positions.append
        while pos < length:
            pos = gene.find(self.subseq,pos)
            if pos == -1:
                break
            if pos%3==0:
                appnd(pos/length)
                 # is (pos=+2) so bad-looking 
            pos += 1
        self.positions_in_gene.extend(positions)
        
    def calcSubseqPos(self):
        # devil nanooptimization
        l = list(map(self.calcSubseqPos4Gene,self.genes))
           
        
        
        
class ChartCalc:
    def __init__(self,positions_in_gene):
        self.positions_in_gene = positions_in_gene
        self.data4plot = []
        
        #number of pointes for plot
        self.ran = None

    def setPointsCount(self,n):
        self.ran = n

    def subseqDensity(self):
        '''generete data for histograms and plots'''
        for i in range(self.ran):
            self.data4plot.append(
                len(list(filter(
                    lambda x: i/self.ran <= x < (i+1)/self.ran,
                    self.positions_in_gene))))
            


############


        
        
        
        
        
        
        
     