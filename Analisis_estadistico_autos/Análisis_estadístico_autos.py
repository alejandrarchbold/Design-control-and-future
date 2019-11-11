print("Importando paquetes...")
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("Leyendo .csv")
#### Para comenzar, con la librería pandas, importamos la base de datos en formato csv.
df_autos = pd.read_csv("C:\\Users\\acamp\\Desktop\\Design-control-and-future\\Analisis_estadistico_autos\\autos_csv.csv", sep=';')
print("Datos Listos")

df_autos.head() #Esta función es para conocer las primeras 5 filas de las 26 columnas de la base.

df_autos.columns #Nombres de las columnas.

#### Resumen de estadisticas de la base de datos:

df_autos.describe()
#En las variables descriptivas está las siguientes:
#Count: numero de observaciones que no son NA/Null
#Media
#Desviación estándar
#El dato mínimo
#Percentil 25
#Percentil 50
#Percentil 75
#El dato máximo

#### Marcas de carros:

#El indice 1 es para acceder a los factors desde el nombre que tienen
marcas = pd.factorize(df_autos["make"])[1]
marcas #Existen 22 marcas registradas en la base de datos.

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
#### Histograma de precios:

#Histograma de todos los precios
price = df_autos["price"] #Obtener los precios de toda la base.
#Utilizamos de la librería matplotlib.pyplot las funciones para hist para que grafique el histograma.
plt.hist(price, range=(min(price),max(price)), color=(0.2,0.4,0.6,0.6))
plt.title("Histograma de los precios en el sector automotriz") #Titulo del gráfico
plt.xlabel("Precio") #Nombre del eje x
plt.ylabel("Cantidad de carros") #Nombre del eje y
plt.show()

#==============================================================================
#### Diagrama de barras
#### Media de precios de cada marca
medias = [] #Creamos una lista de las medias de los precios 
for k in dfs.keys():
    df = dfs[k]
    m = np.mean(df['price']) #Cálculo de la media
    medias.append(m) #Función para agregar la media de los precios
    
x_pos = np.arange(len(marcas)) #Posición de la marca
plt.bar(x_pos, medias, align='edge', width=0.5) #Gráfico de barras
plt.xticks(x_pos, marcas, rotation="vertical") #Configuración de la verticalidad del nombre de cada barra.
plt.title("Media de los precios por marca de carro") #Titulo del gráfico
plt.ylabel("Media de los precios") #Nombre del eje y
plt.show()

# Media de los caballos de fuerza de cada marca
horsepowers = [] #Creamos una lista de los caballos de fuerza de los autos.
for ke in dfs.keys():
    df = dfs[ke]
    me = np.mean(df['horsepower']) #Cálculo de la media de los caballos de fuerza
    horsepowers.append(me) #Función para agregar la media de los caballos de fuerza

plt.bar(x_pos, horsepowers, align='edge', width=0.5) #Gráfico de barras
plt.xticks(x_pos, marcas, rotation="vertical") #Configuración de la verticalidad del nombre de cada barra.
plt.title("Media de los caballos de fuerza por marca de carro") #Titulo del gráfico
plt.ylabel("Media de los precios") #Nombre del eje y
plt.show()

# Media de las millas por galón sobre carretera de cada marca
highway_mpg = [] #Creamos una lista de la media de las millas por galón sobre carretera de cada marca
for ki in dfs.keys():
    df = dfs[ki]
    mi = np.mean(df['highway-mpg']) #Cálculo de la media de las millas por galón sobre carretera
    highway_mpg.append(mi) #Función para agregar la media de las millas por galón sobre carretera

plt.bar(x_pos, highway_mpg, align='edge', width=0.5) #Gráfico de barras
plt.xticks(x_pos, marcas, rotation="vertical") #Configuración de la verticalidad del nombre de cada barra.
plt.title("Media de las millas por galón sobre carretera por marca") #Titulo del gráfico
plt.ylabel("Media de los precios") #Nombre del eje y
plt.show()


# Media de las millas por galón en ciudad de cada marca
city_mpg = [] #Creamos una lista de la media de las millas por galón en ciudad de cada marca
for ka in dfs.keys():
    df = dfs[ka]
    ma = np.mean(df['city-mpg']) #Cálculo de la media de las millas por galón en ciudad
    city_mpg.append(ma) #Función para agregar la media de las millas por galón en ciudad

plt.bar(x_pos, city_mpg, align='edge', width=0.5) #Gráfico de barras
plt.xticks(x_pos, marcas, rotation="vertical") #Configuración de la verticalidad del nombre de cada barra.
plt.title("Media de las millas por galón en ciudad por marca") #Titulo del gráfico
plt.ylabel("Media de los precios") #Nombre del eje y
plt.show()

#==============================================================================
#Variables importantes a analizar (Se leyó cada variable para determinar cuáles de esas características de los
# carros podría influir en el precio)

#wheel-base: ancho entre ruedas del carro
#length: Longitud del carro
#width: Ancho del carro
#height: Altura del carro
#curb-weight: peso total con aceite de motor, de frenos, liquido refrigerante,y todas las funcionalidades del carro
#horsepower: Caballos de fuerza
#peak-rpm: Revoluciones por minuto en el cilindraje
#city-mpg: Millas por galón en ciudad
#highway-mpg: Millas por galón sobre carretera
#price: precio por carro

#==============================================================================
#### Diagrama de dispersión de puntos entre el precio y las variables importantes a analizar
#### con el fin de conocer si existe una relación entre esas variables para luego analizarlas más a fondo.
#Scatter plots (puntos) , y = price


plt.scatter(df_autos["wheel-base"],price) #Diagrama de dispersión
plt.title("Diagrama de dispersión entre el precio y ancho entre ruedas del carro") 
plt.xlabel("Ancho entre ruedas del carro")
plt.ylabel("Precio")
plt.show()

plt.scatter(df_autos["length"],price) #Diagrama de dispersión
plt.title("Diagrama de dispersión entre el precio y la longitud del carro")
plt.xlabel("Longitud del carro")
plt.ylabel("Precio")
plt.show()

plt.scatter(df_autos["width"],price) #Diagrama de dispersión
plt.title("Diagrama de dispersión entre el precio y el ancho del carro")
plt.xlabel("Ancho del carro")
plt.ylabel("Precio")
plt.show()

plt.scatter(df_autos["height"],price) #Diagrama de dispersión
plt.title("Diagrama de dispersión entre el precio y la altura del carro")
plt.xlabel("Altura del carro")
plt.ylabel("Precio")
plt.show()

plt.scatter(df_autos["curb-weight"],price)#Diagrama de dispersión # **
plt.title("Diagrama de dispersión entre el precio y el peso total del carro")
plt.xlabel("Peso total del carro")
plt.ylabel("Precio")
plt.show()

plt.scatter(df_autos["horsepower"],price) #Diagrama de dispersión # *
plt.title("Diagrama de dispersión entre el precio y los caballos de fuerza")
plt.xlabel("Caballos de fuerza del carro")
plt.ylabel("Precio")
plt.show()

plt.scatter(df_autos["peak-rpm"],price) #Diagrama de dispersión
plt.title("Diagrama de dispersión entre el precio y las revoluciones por minuto")
plt.xlabel("Revoluciones por minuto del carro")
plt.ylabel("Precio")
plt.show()

plt.scatter(df_autos["city-mpg"],price) #Diagrama de dispersión # **
plt.title("Diagrama de dispersión entre el precio y las millas por galón en ciudad")
plt.xlabel("Millas por galón en ciudad del carro")
plt.ylabel("Precio")
plt.show()

plt.scatter(df_autos["highway-mpg"],price) #Diagrama de dispersión #**
plt.title("Diagrama de dispersión entre el precio y las millas por galón en carretera")
plt.xlabel("Millas por galón en carretera del carro")
plt.ylabel("Precio")
plt.show()

# Las variables que influyen con respecto al precio son: curb-weight, horsepower,
# city-mpg y highway-mpg

#==============================================================================
#### Agrupamiento por paises

# Creamos un diccionario para clasificar las marcas por el pais de origen (creador)
dic_paises = {
        "Italia":("alfa-romero"),
        "Alemania":("audi","bmw","mercedes-benz","porsche","volkswagen"),
        "Estados_Unidos":("chevrolet","dodge","mercury","plymouth"),
        "Japon":("honda","mazda","isuzu","mitsubishi","nissan","subaru","toyota"),
        "Francia":("peugot","renault"),
        "Suecia":("saab","volvo"),
        "Reino_Unido":("jaguar")
        }
        
# Creamos un diccionario de colores por cada país para identificar con mayor precisión
# cómo influyen las marcas por pais en las variables que influyen en el precio como horsepower,
# city-mpg y highway-mpg

dic_pais_col = {
        "Italia":"yellow",
        "Alemania":"red",
        "Estados_Unidos":"cyan",
        "Japon":"magenta",
        "Francia":"blue",
        "Suecia":"green",
        "Reino_Unido":"deepskyblue"}


colorDeMarca = [] #Creamos una lista de los colores para clasificar en las 22 marcas por color de acuerdo al pais
for m in marcas:
    for p in dic_paises.keys(): #Accediendo a las llave del diccionario (paises)
        if m in dic_paises[p]:
           miPais = p
           colorDeMarca.append(dic_pais_col[miPais]) #Agregar en la lista los colores de acuerdo al pais.


## Para crear una leyenda de los paises por color...
           
# Primero, hacemos una función para encontrar el indice por color de la lista colorDeMarca
def indiceDeColor(col):
    # Retorna los indices de los puntos que son del color col
    idx = []
    for d in range(len(colorDeMarca)):
        if colorDeMarca[d] == col:
            idx.append(d)           
    return idx

# Segundo, queremos crear funciones de acuerdo a la relación que queremos analizar por pais
# En este caso: los caballos de fuerza y las millas por galón sobre carretera
# Esta función busca encontrar las parejas de los puntos de las dos variables a considerar para
# asignar su respectivo color y así dibujar una gráfica de dispersión y tener en cuenta la leyenda de los colores por pais.

def horsepw_highway(col):
    # Funcion que retornar las parejas horsepower, hoighway_mpg cuyo color sea col
    idx = np.array(indiceDeColor(col))
    horsepw = []
    high_mpg = []
    for z in range(len(idx)):
        horsepw.append(horsepowers[z])
        high_mpg.append(highway_mpg[z])
        
    return horsepw, high_mpg
        

#Ahora, por cada punto, asignamos los colores antes expuestos en la lista colorDeMarca
# con el fin de especificar 
hpw_amarillo, hwy_amarillo = horsepw_highway("yellow")
hpw_red, hwy_red = horsepw_highway("red")
hpw_cyan, hwy_cyan = horsepw_highway("cyan")
hpw_magenta, hwy_magenta = horsepw_highway("magenta")
hpw_blue, hwy_blue = horsepw_highway("blue")
hpw_green, hwy_green = horsepw_highway("green")
hpw_dsb, hwy_dsb = horsepw_highway("deepskyblue")

#Realizamos un gráfico de dispersión por cada país de acuerdo al color asignado
amarillos = plt.scatter(hpw_amarillo,hwy_amarillo, color = "yellow") 
rojos = plt.scatter(hpw_red,hwy_red, color = "red") 
cyans = plt.scatter(hpw_cyan, hwy_cyan, color = "cyan")
magentas = plt.scatter(hpw_magenta, hwy_magenta, color = "magenta")
blues = plt.scatter(hpw_blue, hwy_blue, color = "blue") 
verdes = plt.scatter(hpw_green, hwy_green, color = "green")
dsbs = plt.scatter(hpw_dsb, hwy_dsb, color="deepskyblue") 
#Estos gráficos de los distintos colores por pais permite diferenciar las funcionalidades de los carros por pais.


############# 1
#Diagrama de puntos entre x = horsepower, y = highway-mpg
#Este diagrama de puntos también dibuja los tamaños de los puntos de acuerdo si el precio es alto o no
# Por ejemplo si el punto amarrillo del pais Italia es más grande con respecto a los demás paises,
# no solo nos dice la relación que está ubicado entre horsepower y highway-mpg sino que tan costoso es esa marca con respecto a los otros paises.
plt.scatter(x=horsepowers, y=highway_mpg, s = np.array(medias)**(0.5), c =colorDeMarca , alpha=0.8)
plt.title("Relación entre los caballos de fuerza y las millas por galón en carretera")
plt.xlabel("Caballos de fuerza")
plt.ylabel("Millas por galón en carretera")
plt.legend((amarillos, rojos, cyans, magentas, blues, verdes, dsbs),
           ("Italia", "Alemania", "Estados_Unidos", "Japon", "Francia", "Suecia", "Reino_Unido"),
           scatterpoints=1, ncol=3, fontsize=8)
plt.show()


# Definimos otra función pero ahora para obtener el punto entre horsepower y city-mpg
# En este caso: los caballos de fuerza y las millas por galón en ciudad
# Esta función busca encontrar las parejas de los puntos de las dos variables a considerar para
# asignar su respectivo color y así dibujar una gráfica de dispersión y tener en cuenta la leyenda de los colores por pais.

def horsepw_city(col):
    # Funcion que retornar las parejas horsepower, hoighway_mpg cuyo color sea col
    idx = np.array(indiceDeColor(col))
    horsepw1 = []
    c_mpg = []
    for zi in range(len(idx)):
        horsepw1.append(horsepowers[zi])
        c_mpg.append(city_mpg[zi])
        
    return horsepw1, c_mpg

#Por cada punto, asignamos los colores antes expuestos en la lista colorDeMarca
# con el fin de especificar 
hpw_amarillo, cy_amarillo = horsepw_city("yellow")
hpw_red, cy_red = horsepw_city("red")
hpw_cyan, cy_cyan = horsepw_city("cyan")
hpw_magenta, cy_magenta = horsepw_city("magenta")
hpw_blue, cy_blue = horsepw_city("blue")
hpw_green, cy_green = horsepw_city("green")
hpw_dsb, cy_dsb = horsepw_city("deepskyblue")


#Realizamos un gráfico de dispersión por cada país de acuerdo al color asignado
amarillos1 = plt.scatter(hpw_amarillo,cy_amarillo, color = "yellow")
rojos1 = plt.scatter(hpw_red,cy_red, color = "red") 
cyans1 = plt.scatter(hpw_cyan, cy_cyan, color = "cyan")
magentas1 = plt.scatter(hpw_magenta, cy_magenta, color = "magenta")
blues1 = plt.scatter(hpw_blue, cy_blue, color = "blue") 
verdes1 = plt.scatter(hpw_green, cy_green, color = "green")
dsbs1 = plt.scatter(hpw_dsb, cy_dsb, color="deepskyblue") 


############# 2
#Diagrama de puntos entre x = horsepower, y = city-mpg
#Este diagrama de puntos también dibuja los tamaños de los puntos de acuerdo si el precio es alto o no
# Por ejemplo si el punto amarrillo del pais Italia es más grande con respecto a los demás paises,
# no solo nos dice la relación que está ubicado entre horsepower y highway-mpg sino que tan costoso es esa marca con respecto a los otros paises.
plt.scatter(x=horsepowers, y=city_mpg, s = np.array(medias)**(0.5), c = colorDeMarca, alpha=0.8)
plt.title("Relación entre los caballos de fuerza y las millas por galón en ciudad")
plt.xlabel("Caballos de fuerza")
plt.ylabel("Millas por galón en ciudad")
plt.legend((amarillos1, rojos1, cyans1, magentas1, blues1, verdes1, dsbs1),
           ("Italia", "Alemania", "Estados_Unidos", "Japon", "Francia", "Suecia", "Reino_Unido"),
           scatterpoints=1, ncol=3, fontsize=8)
plt.show()

