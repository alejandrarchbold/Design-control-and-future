"""
Trabajar con la cadena de produccion divida en 5 etapas:
    - Materia primas
        *retraso de proveedores
        *insumos en mala calidad
        *aumento precio de materias primas
        *adquision de nuevos materiales
    -Produccion(elaboracion de autos)
        *elaboracion de un carro con un sistema defectuoso
        *daño de alguna maquina
        *accidente laboral (trabajadores)
        * accidentes provocados en la fabira (ej. incendios)
        *desastres naturales
    - Transporte y logistica
        *cambio en politicas
        *accidentes de transito
        *desastre natural (cierre de vias)
        *ataques ciberneticos (logistica)
        *robos de productos
    - Alamcenamiento y bodegaje
        *daño de productos por mal almacenamiento
        *deterioro de los productos
        *accidentes en el sitio de almacenamiento
        *robos
    - Ventas
        *reduccion en las ventas (compran menos)
        *cambio en politicas economicas
        *flutuacion en tasa de cambio
        
"""
#se creara un indice que va ponderar un riesgo de acuerdo al impacto del riesgo y la probabilidad que ocurra (ya se asumen unas probabilidades)
#pero  los impactos se piden al usuario, si es bajo el impacto toma un valor de 1, si es medio es 2 y si es alto se da un valor de 3

intensidad={"alto":3,"medio":2,"bajo":1}
#las siguientes listas contienen las probabilidades de que ocurra los riesgos mencionados arriba en el mismo orden
materias_primas=[0.9,0.9,0.9,0.7]
produccion=[0.04,0.03,0.09,0.08,0.002]
transporte_log=[0.15,0.09,0.002,0.1,0.1]
almacenamiento=[0.18,0.05,0.08,0.1]
ventas=[0.25,0.15,0.3]
MT=["retraso de proveedores","insumos en mala calidad","aumento precio de materias primas","adquision de nuevos materiales"]
PR=["elaboracion de un carro con un sistema defectuoso","daño de alguna maquina","accidente laboral (trabajadores)","accidentes provocados en la fabira (ej. incendios)","desastres naturales"]
TL=["cambio en politicas","accidentes de transito","desastre natural (cierre de vias)","ataques ciberneticos (logistica)","robos de productos"]
AB=["daño de productos por mal almacenamiento","deterioro de los productos","accidentes en el sitio de almacenamiento","robos"]
VE=["reduccion en las ventas (compran menos)","cambio en politicas economicas","flutuacion en tasa de cambio"]
impacto=[]
listt=[MT,PR,TL,AB,VE]
# se crea un ciclo para que pregunte al usuario cuales son los impactos de todos los riesgos especificados arriba, el usario debe escribir (alto,medio,bajo) segun corresponda
for j in listt:
    for i in range(0,len(j)):
        impac=input("defina el impacto de "+str(j[i])+": ")
        impacto.append(impac)

"indice de riesgo"
# el indice es un promedio ponderado, entonces por cada etapa de la cadena, se recibe el impacto que dio el usario, toma el valor que se establecio arriba, y se multiplica con la probabilidad
#Esta lista guardará los indices de riesgo por cada etapa de la cadena
inde=[]
"materias primas:"
suma=0
for k in range(0,len(MT)):
    suma=suma+(intensidad[impacto[k]]*materias_primas[k])
        
in_MT=suma/len(MT)
inde.append(in_MT)        
"produccion"
suma1=0
for j in range(0,len(PR)):
    suma1=suma1+(intensidad[impacto[j+len(MT)]]*produccion[k])
        
in_PR=suma1/len(PR)
inde.append(in_PR)
"transporte y logística:"
suma2=0
for n in range(0,len(TL)):
    suma2=suma2+(intensidad[impacto[n+(len(MT)+len(PR))]]*transporte_log[n])
        
in_TL=suma2/len(TL)
inde.append(in_TL)
"almacenamiento"
suma3=0
for u in range(0,len(AB)):
    suma3=suma3+(intensidad[impacto[u+(len(MT)+len(PR)+len(TL))]]*almacenamiento[u])
       
in_AB=suma3/len(AB)
inde.append(in_AB)
"ventas"
suma4=0
for t in range(0,len(VE)):
    suma4=suma4+(intensidad[impacto[t+(len(impacto)-len(VE))]]*ventas[t])

in_VE=suma4/len(VE)
inde.append(in_VE)
    
       
#ahora con los indices calculados, se hara el analisis de importancia o preocupacion, si:
#      0<i<1 precupacion baja
#      1<i<2 preocupacion medio
#      2<i<3 preocupacion alta  

etapas=["Materias primas","Producción","Transporte y logística","Almacenamiento y bodegaje","Ventas"]

for i in range(0,len(inde)):
    if inde[i]>=2:
        print("Preocupación alta en etapa de "+str(etapas[i]))
    elif inde[i]>=1:
        print("Preocupación media en etapa de "+str(etapas[i]))
    else:
        print("Preocupación baja en etapa de "+str(etapas[i]))
        
            

