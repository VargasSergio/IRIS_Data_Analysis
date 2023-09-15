import pandas as pd
df = pd.read_csv("Iris.csv")

class Iris_iterator:
    def __init__(self, df):
        self.df = df
        self.contador = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len (self.df):
            datos = self.df.iloc [self.contador : self.contador + 2]
            self.contador += 2
            return datos
        else:
            if self.index >= 151:
                print ("error")
            
            
            

            