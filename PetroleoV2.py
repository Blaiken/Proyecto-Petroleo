from datetime import date

class PozoPetrolero:
    def __init__(self):
        # Variables privadas
        self.__capacidad_tanque = []
        self.__cantidad_tanques = []
        self.__horas_trabajadas = []
        
    def set_capacidad_tanque(self, cap_tanque):
        self.__capacidad_tanque.append(cap_tanque)
        
    def get_capacidad_tanque(self):
        return self.__capacidad_tanque
        
    def informe_capacidad_tanque(self):
        print(f"- Capacidad tanque: {self.get_capacidad_tanque()}")
        
    def set_cantidad_tanques(self, can_tanques):
        self.__cantidad_tanques.append(can_tanques)
        
    def get_cantidad_tanques(self):
        return self.__cantidad_tanques   
    
    def informe_cantidad_tanques(self):
        print(f"- Cantidad tanques: {self.get_cantidad_tanques()}")
        
    def set_horas_trabajadas(self, hrs_trabajadas):
        self.__horas_trabajadas.append(hrs_trabajadas)
        
    def get_horas_trabajadas(self):
        return self.__horas_trabajadas
        
    def informe_horas_trabajadas(self):
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
        print(f"- Fechas: {self.get_fecha_produccion_diaria()[0]}, {self.get_fecha_produccion_diaria()[1]}")
    
    def c_produccion_diaria(self):
        produccion_diaria = round(self.pozo.get_capacidad_tanque()[0] * self.pozo.get_cantidad_tanques()[0] / self.pozo.get_horas_trabajadas()[0] / 159, 3)
        return produccion_diaria
    
    def informe_produccion_diaria(self):
        print(f"- Producción diaria: {self.c_produccion_diaria()}")
    
    def c_produccion_semanal(self):
        resultado = round((sum(self.pozo.get_capacidad_tanque())) * (sum(self.pozo.get_cantidad_tanques())) / (sum(self.pozo.get_horas_trabajadas())) / 159, 3)
        return resultado
        
    def informe_produccion_semanal(self):
        print(f"- Producción semanal: {self.c_produccion_semanal()}") 
        
class Valor:
    def __init__(self):
        self.__fecha_actual = []
        self.__precio_actual_barril = []
        
    def set_fecha_actual(self, fecha_actual):
        self.__fecha_actual.append(fecha_actual)
        
    def get_fecha_actual(self):
        return self.__fecha_actual
        
    def informe_fecha_actual(self):
        print(f"- Fecha actual: {self.get_fecha_actual()[0]}")
        
    def set_precio_actual_barril(self, precio_actual):
        self.__precio_actual_barril.append(precio_actual)
        
    def get_precio_actual_barril(self):
        return self.__precio_actual_barril
        
    def informe_precio_barril_actual(self):
        print(f"- Precio barril actual: {self.get_precio_actual_barril()[0]}")
        
    def set_precio_total_semanal(self):
        datos = round(sum(self.get_precio_actual_barril()), 3)
        return datos
    
    def get_precio_total_semanal(self):
        resultado = self.set_precio_total_semanal()
        return resultado
        
    def informe_precio_total_semanal(self):
        print(f"- Precio total semanal: {self.get_precio_total_semanal()}")
        
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
        print(f"- Costo total diario: {self.c_costo_total_diario()}")
        
    def c_costo_total_semanal(self):
        costo_total_semanal = sum(self.__manten_diario + self.__suminis_diario + self.__personal_diario)
        return costo_total_semanal
    
    def informe_costo_semanal(self):
        print(f"- Costo total semanal: {self.c_costo_total_semanal()}")
        
    def c_precio_venta_diario_barril(self):
        precio_venta_diario_barril = round((self.c_costo_total_diario() / self.produccion.c_produccion_diaria()) + self.valor.get_precio_actual_barril()[0], 3)
        return precio_venta_diario_barril
    
    def informe_precio_venta_diario_barril(self):
        print(f"- Precio venta diario del barril: {self.c_precio_venta_diario_barril()}")
        
    def c_precio_venta_semanal_barril(self):
        precio_venta_semanal_barril = round(self.c_costo_total_semanal() / self.produccion.c_produccion_semanal() + self.valor.set_precio_total_semanal(), 3)
        return precio_venta_semanal_barril
        
class Ventas:
    def __init__(self, op, prod):
        self.op = op
        self.prod = prod
        
    def c_ingreso_diario(self):
        ingreso_diario = round(self.prod.c_produccion_diaria() * self.op.c_precio_venta_diario_barril(), 3)
        return ingreso_diario
    
    def informe_ingreso_diario(self):
        print(f"- Ingreso diario: {self.c_ingreso_diario()}")
        
    def c_ingreso_semanal(self):
        ingreso_semanal = round(self.prod.c_produccion_semanal() * self.op.c_precio_venta_semanal_barril(), 3)
        return ingreso_semanal
        
    def informe_ingreso_semanal(self):
        print(f"- Ingreso semanal: {self.c_ingreso_semanal()}")
        
class UtilidadNeta:
    def __init__(self, ven, op):
        self.ven = ven
        self.op = op
        
    def c_utilidad_neta(self):
        utilidad_neta = round(self.ven.c_ingreso_semanal() - self.op.c_costo_total_semanal(), 3)
        return utilidad_neta
    
    def informe_utilidad_neta(self):
        print(f"- Utilidad Neta: {self.c_utilidad_neta()}")

def main():
    
    Pozo = PozoPetrolero()
    Prod = Produccion(Pozo)
    Val = Valor()
    Op = Operaciones(Prod, Val)
    Ven = Ventas(Op, Prod)
    UN = UtilidadNeta(Ven, Op)

    # Ingresar los datos de la clase PozoPetrolero
    print("-------------------------")
    print("DATOS DEL POZO PETROLERO")
    print("-------------------------")
    
    conteo = 1
    
    while conteo <= 2:
        
        print(f"• Día n°{conteo}")
        cap_tanque = float(input("Ingrese el limite de los tanques: "))
        Pozo.set_capacidad_tanque(cap_tanque)
        can_tanques = int(input("Ingrese la cantidad de los tanques: "))
        Pozo.set_cantidad_tanques(can_tanques)
        hrs_trabajadas = int(input("Ingrese las horas trabajadas: "))
        Pozo.set_horas_trabajadas(hrs_trabajadas)
        
        # Ingresar los datos de la clase Produccion
        print(f"• Fecha n°{conteo}")
        ano = int(input("Ingrese el año: "))
        mes = int(input("Ingrese el mes: "))
        dia = int(input("Ingrese el día: "))
        fecha_produccion_diaria = date(ano, mes, dia)
        Prod.set_fecha_produccion_diaria(fecha_produccion_diaria)
        conteo += 1
    
    # Ingresar los datos de la clase Valor
    print("-------------------------")
    print("          VALOR")
    print("-------------------------")
    
    conteo = 1
    
    while conteo <= 2:
        print(f"• Fecha n°{conteo}")
        ano = int(input("Ingrese el año: "))
        mes = int(input("Ingrese el mes: "))
        dia = int(input("Ingrese el día: "))
        fecha_valor_actual = date(ano, mes, dia)
        Val.set_fecha_actual(fecha_valor_actual)
        precio_actual_barril = float(input("Ingrese el precio actual del barril: "))
        Val.set_precio_actual_barril(precio_actual_barril)
        conteo +=1
    
    # Ingresar los datos de la clase Operacion
    print("-------------------------")
    print("       OPERACIONES")
    print("-------------------------")
    
    conteo = 1
    
    while conteo <= 2:
        print(f"• Día n°{conteo}")
        manten = float(input("Ingrese el costo del mantenimiento diario: "))
        suminis = float(input("Ingrese el costo de los suministros diarios: "))
        personal = float(input("Ingrese el costo personal diario: "))
        Op.set_manten_diario(manten)
        Op.set_suminis_diario(suminis)
        Op.set_personal_diario(personal)
        conteo += 1

    print("-------------------------")
    print("       RESULTADOS")
    print("-------------------------")

    # Informe sobre los datos introducidos en PozoPetrolero
    print("POZO PETROLERO:")
    Pozo.informe_capacidad_tanque()
    Pozo.informe_cantidad_tanques()
    Pozo.informe_horas_trabajadas()

    # Informe sobre los datos introducidos en Produccion
    print("PRODUCCIÓN:")
    Prod.informe_fecha_produccion_diaria()
    Prod.c_produccion_diaria()
    Prod.informe_produccion_diaria()
    Prod.informe_produccion_semanal()
    
    # Informe sobre los datos introducidos en Valor
    print("VALOR:")
    Val.informe_fecha_actual()
    Val.informe_precio_barril_actual()
    Val.informe_precio_total_semanal()
    
    # Informe sobre los datos introducidos en Operaciones
    print("OPERACIONES:")
    Op.informe_costo_total_diario()
    Op.informe_costo_semanal()
    Op.informe_precio_venta_diario_barril()
    
    # Informe sobre los datos introducidos en Ventas
    print("VENTAS:")
    Ven.informe_ingreso_diario()
    Ven.informe_ingreso_semanal()
    
    print("UTILIDAD NETA:")
    UN.informe_utilidad_neta()

if __name__ == "__main__":
    main()