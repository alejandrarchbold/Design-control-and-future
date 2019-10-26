print("Importando paquetes...")
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import seaborn as sns
#from sklearn.linear_model import LinearRegression

print("Leyendo .csv")
df_autos = pd.read_csv("C:\\Users\\acamp\\Desktop\\Design-control-and-future\\Analisis_estadistico_autos\\autos_csv.csv", sep=';')
print("Datos Listos")

df_autos.head()

# Nombres de las columnas: df_autos.columns

#Resumen de estadisticas de la base de datos
df_autos.describe()
#Count: numero de observaciones que no son NA/Null

#Marcas de carros
# el indice 1 es para acceder a los factors desde el nombre que tienen
marcas = pd.factorize(df_autos["make"])[1]
marcas

#Confirm es matriz de confirmaciones de marcas
confirm = []

for i in range(len(marcas)):
    confirm.append((df_autos['make'] == marcas[i]))

# data frames de cada una de las marcas
dfs = dict()
for i in range(len(marcas)):
    dfs[marcas[i]] = df_autos[confirm[i]] 

# Ahora se puede acceder al data frame de una marca con dfs["nombre_marca"]
# Ejemplos dfs["bmw"] retorna el dataframe de todos los carros de la marca bmw    

#==============================================================================
#Histograma de precios

#Histograma de todos los precios
price = df_autos["price"]
plt.hist(price, range=(min(price),max(price)), color=(0.2,0.4,0.6,0.6))
plt.title("Histograma de los precios en el sector automotriz")
plt.show()

#==============================================================================
# Diagrama de barras
# Media de precios de cada marca
medias = []
for k in dfs.keys():
    df = dfs[k]
    m = np.mean(df['price'])
    medias.append(m)
    
y_pos = np.arange(len(marcas))
#plt.figure(figsize=(15,3))
plt.bar(y_pos, medias, align='edge', width=0.5)

plt.xticks(y_pos, marcas, rotation="vertical")
plt.title("Media de los precios por marca de carro")
plt.show()

# Media de horsepower de cada marca
horsepowers = []
for ke in dfs.keys():
    df = dfs[ke]
    me = np.mean(df['horsepower'])
    horsepowers.append(me)

plt.bar(y_pos, horsepowers, align='edge', width=0.5)

plt.xticks(y_pos, marcas, rotation="vertical")
plt.title("Media de los horsepowers por marca de carro")
plt.show()

# Media de highway-mpg de cada marca
highway_mpg = []
for ki in dfs.keys():
    df = dfs[ki]
    mi = np.mean(df['highway-mpg'])
    highway_mpg.append(mi)

plt.bar(y_pos, highway_mpg, align='edge', width=0.5)

plt.xticks(y_pos, marcas, rotation="vertical")
plt.title("Media de los highway-mpg por marca de carro")
plt.show()

city_mpg = []
for ka in dfs.keys():
    df = dfs[ka]
    ma = np.mean(df['city-mpg'])
    city_mpg.append(ma)

plt.bar(y_pos, city_mpg, align='edge', width=0.5)

plt.xticks(y_pos, marcas, rotation="vertical")
plt.title("Media de los city-mpg por marca de carro")
plt.show()
#==============================================================================
#Variables importantes a analizar

#wheel-base, length, width, height,
# curb-weight: peso total con aceite de motor, de frenos, liquido refrigerante,y todas las funcionalidades del carro
# horsepower, peak-rpm, city-mpg, highway-mpg, price
#

#==============================================================================
#Scatter plots (puntos) , y = price

#x = wheel-base
plt.scatter(df_autos["wheel-base"],price)

#x = length
plt.scatter(df_autos["length"],price)

plt.scatter(df_autos["width"],price)

plt.scatter(df_autos["height"],price)

plt.scatter(df_autos["curb-weight"],price) # **

plt.scatter(df_autos["horsepower"],price) # *

plt.scatter(df_autos["peak-rpm"],price)

plt.scatter(df_autos["city-mpg"],price) # **

plt.scatter(df_autos["highway-mpg"],price) #**

# Las variables que influyen con respecto al precio son: curb-weight, horsepower,
# city-mpg y highway-mpg

#==============================================================================
#Regresiones lineales
"""
X1 = df_autos.iloc[:,8].values.reshape(-1,1)
Y1 = df_autos.iloc[:,24].values.reshape(-1,1)
linear_regressor = LinearRegression()
linear_regressor.fit(X1,Y1)
Y1_pred = linear_regressor.predict(X1)

plt.scatter(X1,Y1)
plt.plot(X1,Y1_pred, color='red')
plt.show()
"""
# Sin embargo, no se pudo trazar la linea de regresión en la nube de puntos debido
# a la cantidad de NA que hay en la base de datos

#==============================================================================
# Agrupamiento por paises
# https://towardsdatascience.com/data-science-with-python-intro-to-data-visualization-and-matplotlib-5f799b7c6d82
dic_paises = {
        "Italia":("alfa-romero"),
        "Alemania":("audi","bmw","mercedes-benz","porsche","volkswagen"),
        "Estados_Unidos":("chevrolet","dodge","mercury","plymouth"),
        "Japon":("honda","mazda","isuzu","mitsubishi","nissan","subaru","toyota"),
        "Francia":("peugot","renault"),
        "Suecia":("saab","volvo"),
        "Reino_Unido":("jaguar")
        }

dic_pais_col = {
        "Italia":"yellow",
        "Alemania":"red",
        "Estados_Unidos":"cyan",
        "Japon":"magenta",
        "Francia":"blue",
        "Suecia":"green",
        "Reino_Unido":"deepskyblue"
        }

colorDeMarca = []
for m in marcas:
    for p in dic_paises.keys():
        if m in dic_paises[p]:
           miPais = p
           colorDeMarca.append(dic_pais_col[miPais])

Paises = []
for c in colorDeMarca:
    for py in dic_pais_col.keys():
        if c in dic_pais_col[py]:
            Paises.append(py)
           

#Correlacion x = horsepower, y = highway-mpg

plt.scatter(x=horsepowers, y=highway_mpg, s = np.array(medias)**(0.5), c = colorDeMarca, alpha=0.8)
plt.title("Relación entre horsepowers y highway_mpg")
plt.show()


plt.scatter(x=horsepowers, y=city_mpg, s = np.array(medias)**(0.5), c = colorDeMarca, alpha=0.8)
plt.title("Relación entre horsepowers y city_mpg")
plt.show()
