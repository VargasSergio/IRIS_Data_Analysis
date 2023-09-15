import pandas as pd

# Leemos el csv

df = pd.read_csv("Iris.csv")

        ##3.2##

df.describe ()

        ## 3.3 ##

variables = df.columns
print (variables)
for i in variables:
    print (i)
    
        ## 3.4 ##
        

SepalLengthCm = df["SepalLengthCm"]
SepalWidthCm = df["SepalWidthCm"]
PetalWidthCm = df["PetalWidthCm"]
PetalLengthCm = df["PetalLengthCm"]
Species = df["Species"]
    
nombre_variable= str(input("Ingrese el nombre de la variable de la cual quiere conocer sus estadísticas: "))

def estadísticas (nombre_variable:str)->float:
        nombre_variable_media = df [nombre_variable].median()
        nombre_variable_mediana = df [nombre_variable].mean ()
        nombre_variable_desviacion = df [nombre_variable].std ()
        nombre_variable_percentiles =  df[nombre_variable].quantile(q = [0.25, 0.5, 0.75 ])
        import matplotlib.pyplot as plt
        df_group = df.groupby ("Species")["SepalLengthCm"].mean () # En este caso estoy agrupando las "species" y calculando la media de sus "SepalLengthCm" o tallos
        df_group.name = "Media_alto_tallo"
        df_join = df.join(df_group,on=["Species"],how ="inner")
        nombre_variable_histograma =  df_join [nombre_variable].plot(kind = "bar")
        plt.suptitle (nombre_variable)
        resultado = ("Estadisticas de:", nombre_variable,"Media:",nombre_variable_media, "Mediana:", nombre_variable_mediana, "Desviación:", nombre_variable_desviacion, "Percentiles:", nombre_variable_percentiles)
        return resultado

print (estadísticas(nombre_variable))