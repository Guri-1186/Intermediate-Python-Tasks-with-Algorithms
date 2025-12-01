# write a OOP program to get number from user to display its table
class Table:
    def getNum(self):
        self.num = int(input("Enter Num :"))
        
    def showTable(self):
        for i in range(1,11):
            print(f"{i} * {self.num} = {i * self.num}")
            
                  
table = Table()
table.getNum()
table.showTable()
        
        
        
        
