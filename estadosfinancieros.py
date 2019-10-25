#En este programa hacemos estados financieros básicos basados en las NIIF como el estado de resultados, estado de flujos de efectivo y balance general. 
#Que posteriormente serán alimentados de datos más detallados de la empresa como inventarios, compras de materias primas, ventas, etc.

class Estadoresultados:
    #Esta clase crea el estados de resultados con sus respectivas cuentas
    def __init__(self):
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

    def __str__(self):
        return 'Ingresos por actividades ordinarias: {0} \nCosto de ventas: {1} \nUtilidad bruta: {2} \nGastos operacionales: {3} \nUtilidad operacional: {4} \nOtros ingresos: {5} \nOtros egresos: {6} \nUtilidad antes de impuestos: {7} \nProvisión imporrenta: {8} \nUtilidad neta: {9} \n'.format(self.ventas,self.costodeventas,self.utilidadbruta,self.gastosoperacionales,self.utilidadoperacional,self.otrosingresos,self.otrosegresos,self.utilidadantesdeimpuestos,self.provisicionimporrenta,self.utilidadneta)

class Estadoflujosdeefectivo:
    #Esta clase crea el estado de flujos de efectivo
    def __init__(self):
        #Los ingresos y los egresos son las dos grandes categorias de este estado
        #Con el fin de poder organizar cada cuenta según la categoria, creamos diccionarios que contienen el nombre de la cuenta y el valor
        self.ingresos = {}
        self.egresos = {}
        #Pedimos el nombre de cada entrada o salida de dinero en efectivo y la anexamos al respectivo diccionario
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
        
        #Creamos dos atributos que contengan el valor numérico de los ingresos y egresos
        self.ing = 0
        self.egr = 0
        for c in self.ingresos.values():
            self.ing += c
        for n in self.egresos.values():
            self.egr += n
        self.efectivoyequivalentes = self.ing - self.egr

    def __str__(self):
        return 'Ingresos en efectivo: {0} \nEgresos en efectivo: {1} \nEfectivo y equivales al efectivo: {2} \n'.format(self.ing,self.egr,self.efectivoyequivalentes)

class Balancegeneral:
    #En esta clase creamos el balance general
    def __init__(self):
        #Creamos las categorias pricipales que son activo, pasivo y patrimonio.
        self.activo = {}
        self.pasivo = {}
        self.patrimonio = {}
        #Pedimos el nombre de cada cuenta para cada categoria, y la anexamos al diccionario
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
        
        #Sacamos el valor numérico de cada categoria
        self.totalactivo = 0
        for n in self.activo.values():
            self.totalactivo += n
        self.totalpasivo = 0
        for n in self.pasivo.values():
            self.totalpasivo += n
        self.totalpatrimonio = 0
        for n in self.patrimonio.values():
            self.totalpatrimonio += n
        #El activo debería ser igual al pasivo más el patrimonio, si no los es, se dice que hay un descuadre
        #Calculamos el posible descuadre
        self.descuadre = self.totalactivo - self.totalpasivo-self.totalpatrimonio

    def __str__(self):
        s = ''
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
        return s


class Estadosporano:
    #Creamos una clase que almacena los 3 estados financieros por cada año
    def __init__(self,ano,resultados,flujos,balance):
        self.ano = ano
        self.estados = {}
        self.estados['Estado de resultados'] = resultados
        self.estados['Estado de flujos de efectivo'] = flujos
        self.estados['Balance general'] = balance
    def __str__(self):
        return '\nAño: {0} \n'.format(self.ano) +'\n'+ 'Estado de resultados: \n' + str(self.estados['Estado de resultados']) + '\nEstado de flujos de efectivo: \n' + str(self.estados['Estado de flujos de efectivo']) + '\nBalance general: \n' + str(self.estados['Balance general'])

class Historiaestados:
    #Creamos una clase que almacena los estados financieros de varios años
    def __init__(self):
        self.anos = {}
    def anadirestados(self,estado):
        self.anos[estado.ano] = estado
    def __str__(self):
        c = 0
        s = ''
        for i in len(self.anos.keys()):
            s += list(self.anos.keys())[c] +'\n'+ str(list(self.anos.values())[c])
        return s



x = Estadoresultados()
y = Estadoflujosdeefectivo()
z = Balancegeneral()
w = Estadosporano(2019,x,y,z)
h = Historiaestados()
h.anadirestados(w)
print(w)
