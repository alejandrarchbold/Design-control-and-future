############################ definicion de funciones y clases #################################
# por estética los nombres de los riesgos se pusieron con un espacio, pero se creo la funcion
#nombreE que quita esos espacios a la hora de comparar con el nombre que ingresa el usuario
#cuando quiere cambiar un valor en el metodo editInf de la clase Etapa
def nombreE(n):
    dat=n.find("  ")
    if dat==-1:
        return n
    else:
        return n[0:dat]

class Riesgo:

    def __init__(self,prob,impac,nombre):

        self.nombre=nombre
        self.probabilidad=prob
        self.impacto=impac
     # este metodo permite cambiar el valor del atributo probabilidad
    def setProbabilidad(self,prob1):
        self.probabilidad=prob1
    # este metodo retorna el valor del atributo probabilidad actual
    def getProbabilidad(self):
        return self.probabilidad
    # este metodo permite cambiar el valor del atributo impacto medido de 1 a 3
    def setImpacto(self,impac1):
        self.impacto=impac1
    # este metodo retorna el valor del atributo impacto actual
    def getImpacto(self):
        return self.impacto
    #este metodo permite retornar el atributo nombre del riesgo
    def getNombre(self):
        return self.nombre

    def __str__(self):

        return ("{0}\tProbabilidad:{1}\tImpacto:{2}").format(self.nombre,self.probabilidad,self.impacto)

class Etapa:

    def __init__(self,riesG=0):
        self.Lriesgos=[]
        self.riesgo_global=riesG
    # este metodo permite agregar riesgos a la clase etapa, que se crea inicialmente sin ningun riesgo
    def addriesgo(self,riesgo):
        self.Lriesgos.append(riesgo)
    # con los riesgos agregados previamente, este metodo calcula un promedio ponderado de acuerdo con
    # la probabilidad y el impacto de cada riesgo, se retorna ese promedio para esa etapa en particular
    def GlobalRiesgo(self):

        pro=0
        for i in self.Lriesgos:
            pro=pro+(i.getProbabilidad()*i.getImpacto())

        ind=pro/len(self.Lriesgos)
        return ind
    # este metodo permite modificar probabilidad o impacto, de un riesgo que se encuentre en esa etapa
    #en particular, donde nombre1 es el nombre del riesgo a buscar, inf1 es el parametro a cambiar ya sea
    #probabilidad o impacto y par es un parametro, si par=P entonces se entiende que el dato a modificar
    # es probabilidad y si par=I entonces el dato a cambiar es impacto.
    def editInf(self,nombre1,inf1,par):

        if par=="P":
            for i in self.Lriesgos:
                if nombreE(i.getNombre())==nombre1:
                    i.setProbabilidad(inf1)

        else:
            for i in self.Lriesgos:
                if nombreE(i.getNombre())==nombre1:
                    i.setImpacto(inf1)


    def __str__(self):
        s = ""
        for i in range(len(self.Lriesgos)):
            s = s + str(self.Lriesgos[i]) + "\n"
        return s


def printt():
    nombres=[materias_primas,produccion,transporte,almacenamiento,ventas]
    for i in nombres:
        print(i)


# para importar las siguientes librerias es importante instalarlas primero desde
# el terminal usando el comando pip3  asi (ejemplo):
        # sudo pip3 install seaborn

import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
################################# cuerpo del codigo#########################################

## se creo la clase riesgo y los objetos MT. Tambien se crea la clase etapa que
#esta compuesta de varios objetos de tipo riesgo, para este caso, la clase
# etapa es la de materias primas
MT1=Riesgo(1.2,3,"retraso proveedores              ")
MT2=Riesgo(2.0,3,"insumos de mala calidad           ")
MT3=Riesgo(5.5,1,"aumento precio materias primas   ")
materias_primas=Etapa()
list_m=[MT1,MT2,MT3]
for j in range(0,len(list_m)):
    materias_primas.addriesgo(list_m[j])

## se crean los riesgos de la etapa de produccion
PR1=Riesgo(2.1,2,"producto defectuoso             ")
PR2=Riesgo(1.7,2,"daño maquinaria                 ")
PR3=Riesgo(0.02,3,"desastres naturales              ")
produccion=Etapa()
list_p=[PR1,PR2,PR3]
for j in range(0,len(list_p)):
    produccion.addriesgo(list_p[j])

## se crean los riesgos de la etapa de transporte y logística
TL1=Riesgo(2.5,2,"cambio en politicas             ")
TL2=Riesgo(0.9,2,"accidente de transito           ")
TL3=Riesgo(0.07,3,"desastre natural                  ")

transporte=Etapa()
list_t=[TL1,TL2,TL3]
for j in range(0,len(list_t)):
    transporte.addriesgo(list_t[j])

## se crean los riesgos de la etapa de almacenamiento
AB1=Riesgo(2.8,1,"daño productos por almacenamiento")
AB2=Riesgo(0.8,2,"accidente en bodega              ")
AB3=Riesgo(1.0,2,"robos                             ")
almacenamiento=Etapa()
list_a=[AB1,AB2,AB3]
for j in range(0,len(list_a)):
    almacenamiento.addriesgo(list_a[j])

## se crean los riesgos de la etapa de ventas
VE1=Riesgo(3.1,2,"reduccion en ventas               ")
VE2=Riesgo(1.5,2,"cambio politicas economicas      ")
VE3=Riesgo(3.0,2,"fluctuacion en tasas de cambio    ")
ventas=Etapa()
lista_v=[VE1,VE2,VE3]
for j in range(0,len(lista_v)):
    ventas.addriesgo(lista_v[j])

# se imprime los riesgos y datos por defecto que tiene el codigo
printt()

# ahora se da la oportunidad al usuario de modificar algun valor de impacto o probabilidad
Q1=input("¿desea cambiar algun valor?: ")
if Q1=="si":
    Q2=input("Para cambiar algun valor ingrese la informacion asi:\n \nNOMBRE DEL RIESGO,DATO(probabilidad o impacto),TIPO(I para impacto, P para probabilidad)\n \nEJEMPLO\nretraso proveedores,0.32,P\n \nDiga nombre, dato a cambiar y tipo: ")
    inf=Q2.split(sep=",")
    nombres=[materias_primas,produccion,transporte,almacenamiento,ventas]
    for g in nombres:
            g.editInf(inf[0],eval(inf[1]),inf[2])
            print(g)
    while True:
        Q3=input("¿Desea cambiar otro valor?: ")
        if Q3=="no":
            break
        Q4=input("Diga nombre, dato a cambiar y tipo: ")
        inf1=Q4.split(sep=",")
        nombres=[materias_primas,produccion,transporte,almacenamiento,ventas]
        for g in nombres:
            g.editInf(inf1[0],eval(inf1[1]),inf1[2])
            print(g)

    ## imprimir grafico de calor con los valores de riesgo
    newA=np.zeros(shape=(5,3))
    # se crea un ciclo que calcula el reisgo( prob* impacto) y se ingresa
    #a un arreglo que se usará para construir el mapa de calor
    for i in range(0,len(nombres)):
        for j in range(0,len(nombres[i].Lriesgos)):
            newA[i][j]=(nombres[i].Lriesgos[j].getProbabilidad())*(nombres[i].Lriesgos[j].getImpacto())

    # se crea el mapa de calor con la libreria seaborn y se imprime con matplotlib
    y=["M.Primas","Produccion","Transporte","Almacenamiento","Ventas"]
    heat_map=sb.heatmap(newA,cmap="YlOrBr",yticklabels=y)
    plt.ylabel('Etapas en la cadena de produccion')
    plt.xlabel("Riesgos asociados")
    plt.show()
    
else:
    ##imprimir grafico de calor con valores de riesgo
    newA=np.zeros(shape=(5,3))
    # se crea un ciclo que calcula el reisgo( prob* impacto) y se ingresa
    #a un arreglo que se usará para construir el mapa de calor
    nombres=[materias_primas,produccion,transporte,almacenamiento,ventas]
    for i in range(0,len(nombres)):
        for j in range(0,len(nombres[i].Lriesgos)):
            newA[i][j]=(nombres[i].Lriesgos[j].getProbabilidad())*(nombres[i].Lriesgos[j].getImpacto())

    # se crea el mapa de calor con la libreria seaborn y se imprime con matplotlib
    y=["M.Primas","Produccion","Transporte","Almacenamiento","Ventas"]
    heat_map=sb.heatmap(newA,cmap="YlOrBr",yticklabels=y)
    plt.ylabel('Etapas en la cadena de produccion')
    plt.xlabel("Riesgos asociados")
    plt.show()
    
