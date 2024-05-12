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
    def __init__(self, fecha_actual, precio_actual_barril):
        self.__fecha_actual = fecha_actual
        self.__precio_actual_barril = precio_actual_barril
        
    def set_fecha_actual(self, fecha_actual):
        self.__fecha_actual = fecha_actual
        
    def get_fecha_actual(self):
        return self.__fecha_actual
        
    def informe_fecha_actual(self):
        print(f"- Fecha actual: {self.get_fecha_actual()}")
        
    def set_precio_actual_barril(self, precio_actual):
        self.__precio_actual_barril = precio_actual
        
    def get_precio_actual_barril(self):
        return self.__precio_actual_barril
        
    def informe_precio_barril_actual(self, ):
        print(f"- Precio barril actual: {self.get_precio_actual_barril()}")
        
    def set_precio_total_semanal(self):
        datos = round(self.get_precio_actual_barril()*7, 3)
        return datos
    
    def get_precio_total_semanal(self):
        resultado = self.set_precio_total_semanal()
        return resultado
        
    def informe_precio_total_semanal(self):
        print(f"- Precio total semanal: {self.get_precio_total_semanal()}")

def main():
    
    Pozo = PozoPetrolero()
    Prod = Produccion(Pozo)

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
    ano = int(input("Ingrese el año: "))
    mes = int(input("Ingrese el mes: "))
    dia = int(input("Ingrese el día: "))
    fecha_valor_actual = date(ano, mes, dia)
    precio_actual_barril = float(input("Ingrese el precio actual del barril: "))
    Val = Valor(fecha_valor_actual, precio_actual_barril)
    Val.set_fecha_actual(fecha_valor_actual)
    Val.set_precio_actual_barril(precio_actual_barril)

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

if __name__ == "__main__":
    main()