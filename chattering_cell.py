import izhikevich_cells as izh


class cCell(izh.izhCell):
    #default cell with paramters updated for chattering
     def __init__(self,stimVal):
        super().__init__(stimVal)
        self.celltype='Chattering' 
        self.C=50
        self.vr=-60
        self.vt= -40
        self.k=1.5
        self.a=0.03
        self.b=1
        self.c=-40
        self.d=150
        self.vpeak=25
        self.stimVal = stimVal   
        
myCell = cCell(4000)
myCell.simulate()

if __name__=='__main__':
    #validates for grading?
    izh.plotMyData(myCell)