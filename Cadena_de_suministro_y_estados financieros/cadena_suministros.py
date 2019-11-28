## La cadena de suministros se divide en cinco etapas:
#1. Materias Primas
#2. Produccion 
#3. Transporte
#4. Almacenamiento
#5. Ventas

# En cada etapa de la cadena de suministros la idea es que contenga los costos y el tiempo que incurre cada
# parte de la cadena. El tiempo está condicionado a lo que el usuario (la empresa) considera.

# Los costos en términos generales se divide en costo fijos y variables.
# Donde los costos fijos son por ejemplo, el arriendo que incurre la empresa de los puntos de ventas,
# el alquiler de las máquinas para construir el carro, entre otros.
# Los costos variables pueden ser esos costos que son imprevistos a lo largo de la cadena o esos costos que depeden por ejemplo de la tasa de cambio.
# La tasa de cambio cambia diriamente y puede afectar en términos comerciales a la hora de entrar a negociar por ejemplo con paises exportadore.



# Cálculo de las variables del tiempo de acuerdo a lo que el usuario ingrese en cada parte de la cadena:
materias_primas_tiempo = float(input("Tiempo del proceso de las materias primas (meses): ")) 
produccion_tiempo = float(input("Tiempo del proceso de la producción del carro (meses): "))
transporte_tiempo = float(input("Tiempo del proceso del transporte del vehículo (meses): "))
almacenamiento_tiempo = float(input("Tiempo del proceso de almacenamiento (meses): "))
ventas_tiempo = float(input("Tiempo en pasar a los puntos de ventas (meses): "))

# Cálculo del total de los costos donde Costo Total = Costos Fijos + Costos Variables.

# Preguntar al usuario los costos fijos y los costos variables que incurre en cada etapa.

materias_primas_cf = float(input("Costos fijos en el proceso de las materias primas ($): "))
materias_primas_cv = float(input("Costos variables en el proceso de las materias primas ($): "))

produccion_cf = float(input("Costos fijos en la etapa de produccion ($): "))
produccion_cv = float(input("Costos variables en la etapa de produccion ($): "))

transporte_cf = float(input("Costos fijos en el proceso de transporte ($): "))
transporte_cv = float(input("Costos variables en el proceso de transporte ($): "))

almacenamiento_cf = float(input("Costos fijos en el proceso de almacenamiento ($): "))
almacenamiento_cv = float(input("Costos variables en el proceso de almacenamiento ($): "))

ventas_cf = float(input("Costos fijos en los puntos de ventas ($): "))
ventas_cv = float(input("Costos variables en los puntos de ventas ($): "))

# Costos totales en cada punto de la cadena
materias_primas_CT = materias_primas_cf + materias_primas_cv
produccion_CT = produccion_cf + produccion_cv
transporte_CT = transporte_cf + transporte_cv
almacenamiento_CT = almacenamiento_cf + almacenamiento_cv
ventas_CT = ventas_cf + ventas_cv

# Tiempo total de la cadena
Tiempo_del_proceso = materias_primas_tiempo + produccion_tiempo + transporte_tiempo + almacenamiento_tiempo + ventas_tiempo

# Total de los costos incurridos en el proceso de la cadena de producción en el sector automotriz.
Total_costo_cadena = materias_primas_CT + produccion_CT + transporte_CT + almacenamiento_CT + ventas_CT


# Para representar la cadena de produccion, se utilizará la librería tkinter para hacer un interfaz con
# los bloques del proceso
# con estos bloques, queremos incluir en cada etapa su tiempo y costo total donde al final se sepa cuánto tiempo tarda
# la empresa para sacar al mercado el carro y los costos que afectan en sus beneficios totales


import tkinter as tk #importanto el paquete tkinter
from PIL import Image, ImageTk #Para cargar imágenes

wn = tk.Tk() #Objeto ventana 
wn.title("Cadena de producción del sector automostriz") #Titulo de la ventana

Wb = 20 #Ancho del boton
Hb = 5 # alto del boton
Wf = 40 #Ancho de la imagen
y0 = 20 #posicion Y de los botones
A = 80 #Espacio ente boton y flecha
c = 50 #Contador inicial

load_image = Image.open("C:/Users/acamp/Documents/Design-control-and-future/Cadena_de_suministro_y_estados financieros/flecha.png") #Cargando la imagen flecha.png para representar el proceso
load_image = load_image.resize((Wf,40)) #Configurar el tamaño de la imagen
image = ImageTk.PhotoImage(load_image) #Pasarlo al Tk la imagen para cargarlo.


names_chain = ["Materias Primas","Produccion","Transporte","Almacenamiento","Ventas"] #Lista de los nombres de la cadena
colours = ['orchid2','DarkOliveGreen1','cyan','white','yellow2'] #Colores de cada punto de la cadena


#Funcion que me permite colocar un label por cada punto de la cadena de acuerdo a las coordenadas correspondientes.
def printing(texto,xt,yt):
    # xt: posicion x del texto
    # yt: posicion y del texto
    if texto == "Materias Primas":
        tk.Label(wn, text = "Tiempo Materias Primas: {0} meses".format(materias_primas_tiempo)).place(x = xt, y = yt)
        tk.Label(wn, text = "Costo Total Materias Primas: {0}".format(materias_primas_CT)).place(x = xt, y = yt + 30)
    elif texto == "Produccion":
        tk.Label(wn, text = "Tiempo Produccion: {0} meses".format(produccion_tiempo)).place(x = xt, y = yt)
        tk.Label(wn, text = "Costo Total Produccion: {0}".format(produccion_CT)).place(x = xt, y = yt + 30)
    elif texto == "Transporte":
        tk.Label(wn, text = "Tiempo Transporte: {0} meses".format(transporte_tiempo)).place(x = xt, y = yt)
        tk.Label(wn, text = "Costo Total Transporte: {0}".format(transporte_CT)).place(x = xt, y = yt + 30)
    elif texto == "Almacenamiento":
        tk.Label(wn, text = "Tiempo Almacenamiento: {0} meses".format(almacenamiento_tiempo)).place(x = xt, y = yt)
        tk.Label(wn, text = "Costo Total Almacenamiento: {0}".format(almacenamiento_CT)).place(x = xt, y = yt + 30)
    elif texto == "Ventas":
        tk.Label(wn, text = "Tiempo Ventas: {0} meses".format(ventas_tiempo)).place(x = xt, y = yt)
        tk.Label(wn, text = "Costo Total Ventas: {0}".format(ventas_CT)).place(x = xt, y = yt + 30)
    
#Iteracion para cada uno de los nombres de la cadena de acuerdo a la lista planteada anteriormente
for i in range(len(names_chain)):
    if i == 0: #En la primera iteración colocar el tiempo total y costos totales de la cadena
        label_tiempo = tk.Label(text = "Tiempo total de la cadena {0} meses".format(Tiempo_del_proceso), bg = "SeaGreen1") #label del tiempo
        label_tiempo.place(x = c, y = y0+ Hb + 100 + 200) #Coordenadas
        label_tiempo.config(font=("Courier", 12)) #Fuente
        label_costos = tk.Label(text = "Costos totales de la cadena {0} ($)".format(Total_costo_cadena), bg = "SkyBlue1") #Label de los costos
        label_costos.place(x = c, y = y0+ Hb + 100 + 200 + 30) #Coordenadas
        label_costos.config(font=("Courier", 12)) # Fuente
        
    bt = tk.Button(text = names_chain[i], bg = colours[i], command = printing(names_chain[i], c, y0+ Hb + 100 ), width = Wb, height = Hb) #Crear el boton para cada nombre de la cadena
    bt.pack(side=tk.LEFT) #Organizar el botón hacia la izquierda
    bt.place(x = c, y = y0) #Coordenadas
    c = c + Wb + A #Contador que me permite tener una distancia exacta
    bt.config(font=("Courier", 10)) #Fuente 
    if i < len(names_chain)-1: #Para colocar las flechas entre los botones
        img = tk.Label(wn, image = image) #Label imagen
        img.pack(side=tk.LEFT) #Organizar la imagen hacia la izquierda
        img.place(x = c + 80, y = y0 + 20) #Coordenadas
        c = c + Wf + A + 50 #Contador para organizar las fechas iterando

tk.mainloop() #Abrir la ventana 
