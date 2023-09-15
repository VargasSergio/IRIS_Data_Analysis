import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Iris.csv")

class Iris_stadistics:
    def __init__(self, df):
        self.df = df
        
    def estadisticas (self, nombre_variable):
        if nombre_variable in self.df.columns:
            datos_variable = self.df [nombre_variable]
            datos_estadisticos = datos_variable.describe ()
            return datos_estadisticos
        else:
            return print ("Variable name not found")
        
    def histogram (self, nombre_variable):
        if nombre_variable in self.df.columns:
            datos_variable = self.df [nombre_variable]
            plt.hist(nombre_variable)
            plt.suptitle(nombre_variable)
            plt.show ()
        else:
            print ("Variable name not found")