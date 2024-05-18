from datetime import date

class PozoPetrolero:
    def __init__(self):
        self.__capacidad_tanque = []
        self.__cantidad_tanques = []
        self.__horas_trabajadas = []
        
    def set_capacidad_tanque(self, cap_tanque):
        self.__capacidad_tanque.append(cap_tanque)
        
    def get_capacidad_tanque(self):
        return self.__capacidad_tanque
        
    def informe_capacidad_tanque(self):
        archivo = open("Datos.txt", "a")
        archivo.writelines(f"DATOS:\n- Limite de los tanques: {self.get_capacidad_tanque()}")
        print(f"- Capacidad del tanque: {self.get_capacidad_tanque()}")
        
    def set_cantidad_tanques(self, can_tanques):
        self.__cantidad_tanques.append(can_tanques)
        
    def get_cantidad_tanques(self):
        return self.__cantidad_tanques   
    
    def informe_cantidad_tanques(self):
        archivo = open("Datos.txt", "a")
        archivo.writelines(f"\n- Cantidad de los tanques: {self.get_cantidad_tanques()}")
        print(f"- Cantidad tanques: {self.get_cantidad_tanques()}")
        
    def set_horas_trabajadas(self, hrs_trabajadas):
        self.__horas_trabajadas.append(hrs_trabajadas)
        
    def get_horas_trabajadas(self):
        return self.__horas_trabajadas
        
    def informe_horas_trabajadas(self):
        archivo = open("Datos.txt", "a")
        archivo.writelines(f"\n- Cantidad de los tanques: {self.get_horas_trabajadas()}")
        print(f"- Horas trabajadas: {self.get_horas_trabajadas()}")
        
class Produccion:
    def __init__(self, pozo):
        self.pozo = pozo
        self.__fecha_produccion_diaria = []
        
    def set_fecha_produccion_diaria(self, fecha_pd):
        self.__fecha_produccion_diaria.append(fecha_pd)
        
    def get_fecha_produccion_diaria(self):
        return self.__fecha_produccion_diaria
        
    def informe_fecha_produccion_diaria(self):
        archivo = open("Datos.txt", "a")
        archivo.writelines(f"\n- Fecha: {self.get_fecha_produccion_diaria()[0]}")
        print(f"- Fecha: {self.get_fecha_produccion_diaria()[0]}")
    
    def c_produccion_diaria(self):
        produccion_diaria = round(self.pozo.get_capacidad_tanque()[0] * self.pozo.get_cantidad_tanques()[0] / self.pozo.get_horas_trabajadas()[0] / 159, 3)
        return produccion_diaria
    
    def informe_produccion_diaria(self):
        archivo = open("Datos.txt", "a")
        archivo.writelines(f"\n- Producción diaria: {self.c_produccion_diaria()}")
        print(f"- Producción diaria: {self.c_produccion_diaria()}")
        
class Valor:
    def __init__(self):
        self.__fecha_actual = []
        self.__precio_actual_barril = []
        
    def set_fecha_actual(self, fecha_actual):
        self.__fecha_actual.append(fecha_actual)
        
    def get_fecha_actual(self):
        return self.__fecha_actual
        
    def informe_fecha_actual(self):
        archivo = open("Datos.txt", "a")
        archivo.writelines(f"\n- Fecha actual: {self.get_fecha_actual()[0]}")
        print(f"- Fecha actual: {self.get_fecha_actual()[0]}")
        
    def set_precio_actual_barril(self, precio_actual):
        self.__precio_actual_barril.append(precio_actual)
        
    def get_precio_actual_barril(self):
        return self.__precio_actual_barril
        
    def informe_precio_barril_actual(self):
        archivo = open("Datos.txt", "a")
        archivo.writelines(f"\n- Precio barril actual: {self.get_precio_actual_barril()[0]}")
        print(f"- Precio barril actual: {self.get_precio_actual_barril()[0]}")
    
class Operaciones:
    def __init__(self, produccion, valor):
        self.__manten_diario = []
        self.__suminis_diario = []
        self.__personal_diario = []
        self.produccion = produccion
        self.valor = valor
    
    def set_manten_diario(self, manten_diarios):
        self.__manten_diario.append(manten_diarios)
        
    def get_manten_diario(self):
        return self.__manten_diario
    
    def set_suminis_diario(self, suminis_diario):
        self.__suminis_diario.append(suminis_diario)
        
    def get_suminis_diario(self):
        return self.__suminis_diario
    
    def set_personal_diario(self, personal_diario):
        self.__personal_diario.append(personal_diario)
        
    def get_personal_diario(self):
        return self.__personal_diario
    
    def c_costo_total_diario(self):
        costo_total_diario = self.__manten_diario[0] + self.__suminis_diario[0] + self.__personal_diario[0]
        return costo_total_diario
        
    def informe_costo_total_diario(self):
        archivo = open("Datos.txt", "a")
        archivo.writelines(f"\n- Costo total diario: {self.c_costo_total_diario()}")
        print(f"- Costo total diario: {self.c_costo_total_diario()}")
        
    def c_precio_venta_diario_barril(self):
        precio_venta_diario_barril = round((self.c_costo_total_diario() / self.produccion.c_produccion_diaria()) + self.valor.get_precio_actual_barril()[0], 3)
        return precio_venta_diario_barril
    
    def informe_precio_venta_diario_barril(self):
        archivo = open("Datos.txt", "a")
        archivo.writelines(f"\n- Precio venta diario del barril: {self.c_precio_venta_diario_barril()}")
        print(f"- Precio venta diario del barril: {self.c_precio_venta_diario_barril()}")

class Ventas:
    def __init__(self, op, prod):
        self.op = op
        self.prod = prod
        
    def c_ingreso_diario(self):
        ingreso_diario = round(self.prod.c_produccion_diaria() * self.op.c_precio_venta_diario_barril(), 3)
        return ingreso_diario
    
    def informe_ingreso_diario(self):
        archivo = open("Datos.txt", "a")
        archivo.writelines(f"\n- Ingreso diario: {self.c_ingreso_diario()}\n\n")
        print(f"- Ingreso diario: {self.c_ingreso_diario()}")

class UtilidadNeta:
    def __init__(self, ven, op):
        self.ven = ven
        self.op = op

print("----------- MENÚ -------------")
print("1) Ingresar trabajo del dÍa")
print("2) Ver resultado total semanal")
print("3) Salir")
print("------------------------------")
opcion = int(input("Opción: "))

Pozo = PozoPetrolero()
Prod = Produccion(Pozo)
Val = Valor()
Op = Operaciones(Prod, Val)
Ven = Ventas(Op, Prod)
UN = UtilidadNeta(Ven, Op)

if opcion == 1:
    
    print("-------------------------")
    print(" DATOS - POZO PETROLERO ")
    print("-------------------------")
    cap_tanque = float(input("Ingrese el limite de los tanques: "))
    Pozo.set_capacidad_tanque(cap_tanque)
    can_tanques = int(input("Ingrese la cantidad de los tanques: "))
    Pozo.set_cantidad_tanques(can_tanques)
    hrs_trabajadas = int(input("Ingrese las horas trabajadas: "))
    Pozo.set_horas_trabajadas(hrs_trabajadas)
    
    print("-------------------------")
    print("DATOS - DÍA DE PRODUCCIÓN")
    print("-------------------------")
    ano = int(input("Ingrese el año: "))
    mes = int(input("Ingrese el mes: "))
    dia = int(input("Ingrese el día: "))
    fecha_produccion_diaria = date(ano, mes, dia)
    Prod.set_fecha_produccion_diaria(fecha_produccion_diaria)
    
    print("-------------------------")
    print("      DATOS - VALOR")
    print("-------------------------")
    ano = int(input("Ingrese el año: "))
    mes = int(input("Ingrese el mes: "))
    dia = int(input("Ingrese el día: "))
    fecha_valor_actual = date(ano, mes, dia)
    Val.set_fecha_actual(fecha_valor_actual)
    precio_actual_barril = float(input("Ingrese el precio actual del barril: "))
    Val.set_precio_actual_barril(precio_actual_barril)
    
    print("-------------------------")
    print("   DATOS - OPERACIONES")
    print("-------------------------")
    manten = float(input("Ingrese el costo del mantenimiento diario: "))
    suminis = float(input("Ingrese el costo de los suministros diarios: "))
    personal = float(input("Ingrese el costo personal diario: "))
    Op.set_manten_diario(manten)
    Op.set_suminis_diario(suminis)
    Op.set_personal_diario(personal)
    
    print("-------------------------")
    print("       RESULTADOS")
    print("-------------------------")
    
    Pozo.informe_capacidad_tanque()
    Pozo.informe_cantidad_tanques()
    Pozo.informe_horas_trabajadas()
    
    Prod.informe_fecha_produccion_diaria()
    Prod.informe_produccion_diaria()
    
    Val.informe_fecha_actual()
    Val.informe_precio_barril_actual()
    
    Op.informe_costo_total_diario()
    Op.informe_precio_venta_diario_barril()
    
    Ven.informe_ingreso_diario()
    
elif opcion == 2:
    print("Hola")
    
else:
    print("Finalizando programa...")
    