#El siguiente código permite llevar la contabilidad de una empresa. 
#Los 3 estados que se tomarán son el estado de resultados, el estado de flujos de efectivo y el balance general.
#Para esto, se utilizaran 3 clases: una para crear nuevos estados por un año, otra para tomar los estados anteriores 
# y la última para guardar los estados por año y combinar los estados de los años anteriores con los nuevos


class nuevoEstadosporano:
    #Se crea una clase que permite crear objetos que contengan los 3 estados financieros básicos, preguntandole
    # al usuario el valor de cada elemento de los estados
    def __init__(self):
        self.ano = input('Año: ')

        print('Estado de resultados')
        #A través del input se le pide al usuario ingresar el valor de cada cuenta
        self.ventas = float(input('Ingresos por actividades ordinarias: '))
        self.costodeventas = float(input('Costo de ventas: '))
        #Se hace el cálculo de las utilidades sin tener que pedirselo al usuario
        self.utilidadbruta = self.ventas - self.costodeventas
        self.gastosoperacionales = float(input('Gastos operacionales: '))
        self.utilidadoperacional = self.utilidadbruta - self.gastosoperacionales
        self.otrosingresos = float(input('Otros ingresos: '))
        self.otrosegresos = float(input('Otros egresos: '))
        self.utilidadantesdeimpuestos = self.utilidadoperacional +self.otrosingresos- self.otrosegresos
        self.tasatributaria = float(input('Tasa tributaria: '))
        self.provisicionimporrenta = self.utilidadantesdeimpuestos*self.tasatributaria
        self.utilidadneta = self.utilidadantesdeimpuestos - self.provisicionimporrenta

        #en el estado de flujos de efectivo y el balance general pueden haber más cuentas de las esperadas, por lo que se le pregunta
        #el nombre de cada cuenta y el valor de la misma al usuario
        print('A continuación ingrese el nombre de la cuenta y su valor. Una vez haya terminado, escriba \"done\"'
        print('Estado de flujos de efectivo')
        self.ingresos = {}
        self.egresos = {}
        while True:
            # Se le pide al usuario el nombre de cada cuenta de ingresos, el nombre es asignado como la llave del diccionario ingresos con su respectivo valor.
            i = input('Nombre de la cuentas de ingreso: ')
            if i == 'done':
                #cuendo el usuario termina de agregar las cuentas de ingresos, escribe done y pasa a egresos.
                break
            self.ingresos[i] = float(input('Valor: '))
        while True:
            # Se le pide al usuario el nombre de cada cuenta de egresos, el nombre es asignado como la llave del diccionario de egresos con su respectivo valor.
            i = input('Nombre de la cuentas de egresos: ')
            if i == 'done':
                #cuendo el usuario termina de agregar las cuentas de egresos, escribe done y pasa a balance general.
                break
            self.egresos[i] = float(input('Valor: '))
        self.ing = 0
        self.egr = 0
        for c in self.ingresos.values():
            #se suman todos los valores del diccionario ingresos para saber el valor total de los ingresos
            self.ing += c
        for n in self.egresos.values():
            #se suman todos los valores del diccionario egresos para saber el valor total de los egresos
            self.egr += n
        #Se calcula el efectivo con el que cuenta la compañia para el período
        self.efectivoyequivalentes = self.ing - self.egr

        print('Balance general')
        #Se crean diccionarios para el pasivo, el activo y el patrimonio
        self.activo = {}
        self.pasivo = {}
        self.patrimonio = {}
        #Se pregunta por el nombre de cada item y su valor y se agrega al respectivo diccionario
        while True:
            i = input('Nombre de la cuenta activo: ')
            if i == 'done':
                break
            self.activo[i] = float(input('Valor: '))
        while True:
            i = input('Nombre de la cuenta pasivo: ')
            if i == 'done':
                break
            self.pasivo[i] = float(input('Valor: '))
        while True:
            i = input('Nombre de la cuenta patrimonio: ')
            if i == 'done':
                break
            self.patrimonio[i] = float(input('Valor: '))
        self.totalactivo = 0
        #Se suman los valores de las cuentas en el diccionario activo para calcular el valor total del activo
        for n in self.activo.values():
            self.totalactivo += n
        self.totalpasivo = 0
        #Se suman los valores de las cuentas en el diccionario pasivo para calcular el valor total del pasivo      
        for n in self.pasivo.values():
            self.totalpasivo += n
        self.totalpatrimonio = 0
        #Se suman los valores de las cuentas en el diccionario patrimonio para calcular el valor total del patrimonio       
        for n in self.patrimonio.values():
            self.totalpatrimonio += n
        self.descuadre = self.totalactivo - self.totalpasivo-self.totalpatrimonio

    def __str__(self):
        #Se retornan los items y valores anteriores en forma de string sumándolos a una variable s
        s = 'Anio: {0}\n'.format(self.ano)
        s+='\n'
        s+= 'Estado de resultados\n'
        s += 'Ingresos por actividades ordinarias: {0} \nCosto de ventas: {1} \nUtilidad bruta: {2} \nGastos operacionales: {3} \nUtilidad operacional: {4} \nOtros ingresos: {5} \nOtros egresos: {6} \nUtilidad antes de impuestos: {7} \nProvision imporrenta: {8} \nUtilidad neta: {9} \n'.format(self.ventas,self.costodeventas,self.utilidadbruta,self.gastosoperacionales,self.utilidadoperacional,self.otrosingresos,self.otrosegresos,self.utilidadantesdeimpuestos,self.provisicionimporrenta,self.utilidadneta)
        s+='\n'
        s += 'Estado de flujos de efectivo\n'
        s += 'Ingresos en efectivo: {0} \nEgresos en efectivo: {1} \nEfectivo y equivales al efectivo: {2} \n'.format(self.ing,self.egr,self.efectivoyequivalentes)
        s+='\n'
        s += 'Balance general\n'
        c = 0
        for n in range(len(self.activo.keys())):
            s += list(self.activo.keys())[c] +': '+ str(list(self.activo.values())[c]) + '\n'
            c +=1
        c = 0
        s+= 'Total activo: {0}\n'.format(self.totalactivo)
        for n in range(len(self.pasivo.keys())):
            s += list(self.pasivo.keys())[c] +': '+ str(list(self.pasivo.values())[c]) + '\n'
            c +=1
        c=0
        s+= 'Total pasivo: {0}\n'.format(self.totalpasivo)
        for n in range(len(self.patrimonio.keys())):
            s += list(self.patrimonio.keys())[c] +': '+ str(list(self.patrimonio.values())[c]) + '\n'
            c +=1
        s+= 'Total patrimonio: {0} \n'.format(self.totalpatrimonio)
        s+= 'Descuadre: {0}\n'.format(self.descuadre)
        s+='\n'
        return s

class viejoEstadosporano:
    #esta clase abre el archivo finanzas.txt y recupera los valores de cada año con sus respectivos estados,
    #y los guarda todos en un diccionario con el año como llave y los items como valores
    def __init__(self):
        self.miarchivo = open('finanzas.txt', 'r')
        self.x = self.miarchivo.readlines()
        self.s = ''
        p = 0
        p2 = 0
        c = 0
        self.x2 = []
        nanios = 0
        self.fechas = []
        self.anios = {}
        for l in self.x:
            #Se cuenta el número de años guardados en el archivo txt
            l = l.rstrip()
            l = l.split(': ')
            for i in l:
                if i == 'Anio':
                    nanios += 1

        for l in self.x:
            #Se toma el valor de los años que hay en el archivo, ejemplo: 2019, 2018. Y se agregan a una lista
            l = l.rstrip()
            l = l.split(': ')
            for i in l:
                if i == 'Anio':
                    self.fechas.append(l[c+1])


        c = 0
        #Por cada año se toma la porción del texto correspondiente a ese año y se extraen los valores y se agregan a un diccionario con el valor del año como llave 
        for j in range(nanios):
            for i in self.x:
                i = i.rstrip()
                if i =='Anio: {0}'.format(self.fechas[j]):
                    p = c
                c+=1
            c =0
            self.x2 = self.x[p:p+28]
            for line in self.x2:
                self.s += line
            self.anios[self.fechas[j]] = self.s
            self.s=''
        self.miarchivo.close()
    def __str__(self):
        #Se retornan todos los valores del diccionario en forma de string
        s = ''
        for q in self.fechas:
            s += self.anios[q]
        return s


class Historiaestados:
    #Esta clase permite añadir varios años y guardarlos en un objeto.
    def __init__(self):
        #Se crea el diccionario self.anos donde posteriormente se almacenará la información según el año
        self.anos = {}
        self.viejo = None
    def anadirviejosestados(self,clase):
        #Se añaden los datos de los años que estuvieran en el archivo finanzas.txt
        k = clase.anios.keys()
        for ke in k:
            self.anos[ke] = clase.anios[ke]

    def anadirestados(self,estado):
        #Se añaden el estado que se creó nuevo
        self.anos[estado.ano] = estado
    def __str__(self):
        #se retorna los valores de todos los años con sus respectivos datos en forma de string
        c = 0
        s = ''
        for i in range(len(self.anos.keys())):
            s += '\n'+ str(list(self.anos.values())[c])
            c += 1
        return s




viejo = viejoEstadosporano()
todo = Historiaestados()
nuevo = nuevoEstadosporano()
todo.anadirviejosestados(viejo)
todo.anadirestados(nuevo)

miarchivo = open('finanzas.txt', 'w')
#Se reescribe el archivo actualizandolo con los nuevos estados 
miarchivo.write(str(todo))
miarchivo.close()
print("Pueden ver los estados por año en el archivo finanzas.txt"
