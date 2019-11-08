class nuevoEstadosporano:
    #Se crea una clase que permite crear objetos que contengan los 3 estados financieros básicos, preguntandole
    # al usuario el valor de cada elemento de los estados
    def __init__(self):
        self.ano = input('Año: ')

        print('Estado de resultados')
        self.ventas = float(input('Ingresos por actividades ordinarias: '))
        self.costodeventas = float(input('Costo de ventas: '))
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
        print('Estado de flujos de efectivo')
        self.ingresos = {}
        self.egresos = {}
        while True:
            i = input('Nombre de la cuentas de ingreso: ')
            if i == 'done':
                break
            self.ingresos[i] = float(input('Valor: '))
        while True:
            i = input('Nombre de la cuentas de egresos: ')
            if i == 'done':
                break
            self.egresos[i] = float(input('Valor: '))
        self.ing = 0
        self.egr = 0
        for c in self.ingresos.values():
            self.ing += c
        for n in self.egresos.values():
            self.egr += n
        self.efectivoyequivalentes = self.ing - self.egr

        print('Balance general')
        self.activo = {}
        self.pasivo = {}
        self.patrimonio = {}
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
        for n in self.activo.values():
            self.totalactivo += n
        self.totalpasivo = 0
        for n in self.pasivo.values():
            self.totalpasivo += n
        self.totalpatrimonio = 0
        for n in self.patrimonio.values():
            self.totalpatrimonio += n
        self.descuadre = self.totalactivo - self.totalpasivo-self.totalpatrimonio

    def __str__(self):
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
    #estad clase abre el archivo finanzas.txt y recupera los valores de cada año con sus respectivos estados,
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
            l = l.rstrip()
            l = l.split(': ')
            for i in l:
                if i == 'Anio':
                    nanios += 1

        for l in self.x:
            l = l.rstrip()
            l = l.split(': ')
            for i in l:
                if i == 'Anio':
                    self.fechas.append(l[c+1])


        c = 0
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
        s = ''
        for q in self.fechas:
            s += self.anios[q]
        return s


class Historiaestados:
    #Esta clase permite añadir varios años y guardarlos en un objeto.
    def __init__(self):
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
