from datetime import date
import os

with open("Universidad\\contador.txt", "w") as contador_inicial:
    contador_inicial.write("1")
    
contador = open("Universidad\\contador.txt", "r")
contenido = contador.readline()
contador.close()

ruta_diario = f"Universidad\\Datos_diarios_{contenido}.txt"
ruta_semanal = f"Universidad\\Datos_semanal_{contenido}.txt"

class PozoPetrolero:
    def __init__(self):
        self.__capacidad_tanque = []
        self.__cantidad_tanques = []
        self.__horas_trabajadas = []
        self.__tiempo_en_llenarse_un_tanque = []
        
    def set_capacidad_tanque(self, cap_tanque):
        self.__capacidad_tanque.append(cap_tanque)
        
    def get_capacidad_tanque(self):
        return self.__capacidad_tanque
        
    def informe_capacidad_tanque(self):
        with open(ruta_diario, "a") as archivo:
            archivo.writelines(f"DATOS DIARIOS:\n\n- Capacidad de los tanques:\n{self.get_capacidad_tanque()[0]}")
        print(f"- Capacidad del tanque: {self.get_capacidad_tanque()[0]}")
        
    def set_cantidad_tanques(self, can_tanques):
        self.__cantidad_tanques.append(can_tanques)
        
    def get_cantidad_tanques(self):
        return self.__cantidad_tanques   
    
    def informe_cantidad_tanques(self):
        with open(ruta_diario, "a") as archivo:
            archivo.writelines(f"\n- Cantidad de los tanques:\n{self.get_cantidad_tanques()[0]}")
        print(f"- Cantidad tanques: {self.get_cantidad_tanques()[0]}")
        
    def set_horas_trabajadas(self, hrs_trabajadas):
        self.__horas_trabajadas.append(hrs_trabajadas)
        
    def get_horas_trabajadas(self):
        return self.__horas_trabajadas
        
    def informe_horas_trabajadas(self):
        with open(ruta_diario, "a") as archivo:
            archivo.writelines(f"\n- Horas trabajadas:\n{self.get_horas_trabajadas()[0]}")
        print(f"- Horas trabajadas: {self.get_horas_trabajadas()[0]}")
        
    def set_tiempo_en_llenarse_un_tanque(self, tiemp_llenarse_tanque):
        self.__tiempo_en_llenarse_un_tanque.append(tiemp_llenarse_tanque)
        
    def get_tiempo_en_llenarse_un_tanque(self):
        return self.__tiempo_en_llenarse_un_tanque
    
    def informe_tiempo_en_llenarse_un_tanque(self):
        with open(ruta_diario, "a") as archivo:
            archivo.writelines(f"\n- Tiempo en llenarse un tanque:\n{self.get_tiempo_en_llenarse_un_tanque()[0]}")
        print(f"- Tiempo en llenarse un tanque: {self.get_tiempo_en_llenarse_un_tanque()[0]}")
        
class Produccion:
    def __init__(self, pozo):
        self.pozo = pozo
        self.__fecha_produccion_diaria = []
        
    def set_fecha_produccion_diaria(self, fecha_pd):
        self.__fecha_produccion_diaria.append(fecha_pd)
        
    def get_fecha_produccion_diaria(self):
        return self.__fecha_produccion_diaria
        
    def informe_fecha_produccion_diaria(self):
        with open(ruta_diario, "a") as archivo:
            archivo.writelines(f"\n- Fecha producción diaria:\n{self.get_fecha_produccion_diaria()[0]}")
        print(f"- Fecha producción diaria: {self.get_fecha_produccion_diaria()[0]}")
    
    def c_produccion_diaria(self):
        tanques_llenos = self.pozo.get_horas_trabajadas()[0] / self.pozo.get_tiempo_en_llenarse_un_tanque()[0]
        petroleo = tanques_llenos * self.pozo.get_capacidad_tanque()[0]
        produccion_diaria = round(petroleo / 159, 3)
        return produccion_diaria
    
    def informe_produccion_diaria(self):
        with open(ruta_diario, "a") as archivo:
            archivo.writelines(f"\n- Producción diaria. Total de barriles:\n{self.c_produccion_diaria()}")
        print(f"- Producción diaria. Total de barriles: {self.c_produccion_diaria()}")
        
    def c_produccion_semanal(self):
        
        def leer_lineas(linea):
            with open(ruta_diario, "r") as arch:
                lineas = arch.readlines()
                lineas_especificas = lineas[linea]
                return lineas_especificas
            
        linea1 = leer_lineas(13)
        linea2 = leer_lineas(40)
        linea3 = leer_lineas(67)
        linea4 = leer_lineas(94)
        linea5 = leer_lineas(121)
        linea6 = leer_lineas(148)    
        linea7 = leer_lineas(175)

        produccion_semanal = round(float(linea1) + float(linea2) + float(linea3) + float(linea4) + float(linea5) + float(linea6) + float(linea7), 3)
        return produccion_semanal
    
    def informe_produccion_semanal(self):
        with open(ruta_semanal, "w") as archivo:
            archivo.writelines(f"DATOS SEMANAL:\n\n- Producción semanal:\n{self.c_produccion_semanal()}")
        print("------------------------------")
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
        with open(ruta_diario, "a") as archivo:
            archivo.writelines(f"\n- Fecha actual:\n{self.get_fecha_actual()[0]}")
        print(f"- Fecha actual: {self.get_fecha_actual()[0]}")
        
    def set_precio_actual_barril(self, precio_actual):
        self.__precio_actual_barril.append(precio_actual)
        
    def get_precio_actual_barril(self):
        return self.__precio_actual_barril
        
    def informe_precio_barril_actual(self):
        with open(ruta_diario, "a") as archivo:
            archivo.writelines(f"\n- Precio barril actual:\n{self.get_precio_actual_barril()[0]}")
        print(f"- Precio barril actual: {self.get_precio_actual_barril()[0]}")
    
class Operaciones:
    def __init__(self, produccion, valor):
        self.__manten_diario = []
        self.__suminis_diario = []
        self.__cantidad_personal = []
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
    
    def set_cantidad_personal(self, cantidad_personal):
        self.__cantidad_personal.append(cantidad_personal)
        
    def get_cantidad_personal(self):
        return self.__cantidad_personal
    
    def set_personal_diario(self, personal_diario):
        self.__personal_diario.append(personal_diario)
        
    def get_personal_diario(self):
        return self.__personal_diario
    
    def informe_cantidad_personal(self):
        with open(ruta_diario, "a") as archivo:
            archivo.writelines(f"\n- Cantidad de personal:\n{self.get_cantidad_personal()[0]}")
        print(f"- Cantidad de personal: {self.get_cantidad_personal()[0]}")
    
    def c_costo_total_diario(self):
        costo_total_diario = self.__manten_diario[0] + self.__suminis_diario[0] + (self.__cantidad_personal[0] * self.__personal_diario[0])
        return costo_total_diario
        
    def informe_costo_total_diario(self):
        with open(ruta_diario, "a") as archivo:
            archivo.writelines(f"\n- Costo total diario:\n{self.c_costo_total_diario()}")
        print(f"- Costo total diario: {self.c_costo_total_diario()}")
        
    def c_costo_total_semanal(self):
        
        def leer_lineas(linea):
            with open(ruta_diario, "r") as arch:
                lineas = arch.readlines()
                lineas_especificas = lineas[linea]
                return lineas_especificas
            
        linea1 = leer_lineas(21)
        linea2 = leer_lineas(48)
        linea3 = leer_lineas(75)
        linea4 = leer_lineas(102)
        linea5 = leer_lineas(129)
        linea6 = leer_lineas(156)
        linea7 = leer_lineas(183)

        costo_total_semanal = round(float(linea1) + float(linea2) + float(linea3) + float(linea4) + float(linea5) + float(linea6) + float(linea7), 3)
        return costo_total_semanal
            
    def informe_costo_total_semanal(self):
        with open(ruta_semanal, "a") as archivo:
            archivo.writelines(f"\n- Costo total semanal:\n{self.c_costo_total_semanal()}")
        print(f"- Costo total semanal: {self.c_costo_total_semanal()}")
        
    def c_precio_venta_diario_barril(self):
        precio_venta_diario_barril = round((self.c_costo_total_diario() / self.produccion.c_produccion_diaria()) + self.valor.get_precio_actual_barril()[0], 3)
        return precio_venta_diario_barril
    
    def informe_precio_venta_diario_barril(self):
        with open(ruta_diario, "a") as archivo:
            archivo.writelines(f"\n- Precio venta diario del barril:\n{self.c_precio_venta_diario_barril()}")
        print(f"- Precio venta diario del barril: {self.c_precio_venta_diario_barril()}")

class Ventas:
    def __init__(self, op, prod):
        self.op = op
        self.prod = prod
        
    def c_ingreso_diario(self):
        ingreso_diario = round(self.prod.c_produccion_diaria() * self.op.c_precio_venta_diario_barril(), 3)
        return ingreso_diario
    
    def informe_ingreso_diario(self):
        with open(ruta_diario, "a") as archivo:
            archivo.writelines(f"\n- Ingreso diario:\n{self.c_ingreso_diario()}\n\n")
        print(f"- Ingreso diario: {self.c_ingreso_diario()}")
        
    def c_ingreso_semanal(self):
        
        def leer_lineas(linea):
            with open(ruta_diario, "r") as arch:
                lineas = arch.readlines()
                lineas_especificas = lineas[linea]
                return lineas_especificas
            
        linea1 = leer_lineas(25)
        linea2 = leer_lineas(52)
        linea3 = leer_lineas(79)
        linea4 = leer_lineas(106)
        linea5 = leer_lineas(133)
        linea6 = leer_lineas(160)
        linea7 = leer_lineas(187)

        ingreso_semanal = round(float(linea1) + float(linea2) + float(linea3) + float(linea4) + float(linea5) + float(linea6) + float(linea7), 3)
        return ingreso_semanal
    
    def informe_ingreso_semanal(self):
        with open(ruta_semanal, "a") as archivo:
            archivo.writelines(f"\n- Ingreso semanal:\n{self.c_ingreso_semanal()}")
        print(f"- Ingreso semanal: {self.c_ingreso_semanal()}")

class UtilidadNeta:
    def __init__(self, ven, op):
        self.ven = ven
        self.op = op
        
    def c_utilidad_neta(self):
        utilidad_neta = round(self.ven.c_ingreso_semanal() - self.op.c_costo_total_semanal(), 3)
        return utilidad_neta
    
    def informe_utilidad_neta(self):
        with open(ruta_semanal, "a") as archivo:
            archivo.writelines(f"\n- Utilidad neta:\n{self.c_utilidad_neta()}")
        print(f"- Utilidad neta: {self.c_utilidad_neta()}")

def main():

    while True:
        print("----------- MENÚ -------------")
        print("1) Ingresar trabajo del dÍa")
        print("2) Ver resultado total semanal")
        print("3) Salir")
        print("------------------------------")
        opcion = int(input("Opción: "))
        print("------------------------------")
        os.system('cls')

        Pozo = PozoPetrolero()
        Prod = Produccion(Pozo)
        Val = Valor()
        Op = Operaciones(Prod, Val)
        Ven = Ventas(Op, Prod)
        UN = UtilidadNeta(Ven, Op)

        if opcion == 1:
            
            archivo = open(ruta_diario, "a")
            archivo.close()
            
            with open(ruta_diario, "r") as f:
                lineas = f.readlines()
                
                if len(lineas) >= 188:
                    
                    print("¡Ya has completado una semana!\nPara registrar la siguiente semana cambia el\nnombre del archivo -Datos_diarios_1.txt-")
                    input("\nPresiona Enter para continuar...")
                    os.system('cls')
                    
                else:
            
                    print("------------------------------")
                    print("   DATOS - POZO PETROLERO ")
                    print("------------------------------")
                    cap_tanque = float(input("Ingrese la capacidad de los tanques: "))
                    Pozo.set_capacidad_tanque(cap_tanque)
                    can_tanques = int(input("Ingrese la cantidad de los tanques: "))
                    Pozo.set_cantidad_tanques(can_tanques)
                    hrs_trabajadas = int(input("Ingrese las horas trabajadas: "))
                    Pozo.set_horas_trabajadas(hrs_trabajadas)
                    tiempo_tanque = int(input("Ingrese las horas que dura en llenarse un tanque: "))
                    Pozo.set_tiempo_en_llenarse_un_tanque(tiempo_tanque)
                    
                    print("------------------------------")
                    print("  DATOS - DÍA DE PRODUCCIÓN")
                    print("------------------------------")
                    ano = int(input("Ingrese el año: "))
                    mes = int(input("Ingrese el mes: "))
                    dia = int(input("Ingrese el día: "))
                    fecha_produccion_diaria = date(ano, mes, dia)
                    Prod.set_fecha_produccion_diaria(fecha_produccion_diaria)
                    
                    print("------------------------------")
                    print("    DATOS - PRECIO ACTUAL")
                    print("------------------------------")
                    ano = int(input("Ingrese el año: "))
                    mes = int(input("Ingrese el mes: "))
                    dia = int(input("Ingrese el día: "))
                    fecha_valor_actual = date(ano, mes, dia)
                    Val.set_fecha_actual(fecha_valor_actual)
                    precio_actual_barril = float(input("Ingrese el precio actual del barril: "))
                    Val.set_precio_actual_barril(precio_actual_barril)
                    
                    print("------------------------------")
                    print("      DATOS - OPERACIONES")
                    print("------------------------------")
                    manten = float(input("Ingrese el costo del mantenimiento diario: "))
                    suminis = float(input("Ingrese el costo de los suministros diarios: "))
                    cantidad = int(input("Ingrese la cantidad del personal: "))
                    personal = float(input("Ingrese el costo personal diario: "))
                    Op.set_manten_diario(manten)
                    Op.set_suminis_diario(suminis)
                    Op.set_cantidad_personal(cantidad)
                    Op.set_personal_diario(personal)
                    
                    print("------------------------------")
                    print("          RESULTADOS")
                    print("------------------------------")
                    
                    Pozo.informe_capacidad_tanque()
                    Pozo.informe_cantidad_tanques()
                    Pozo.informe_horas_trabajadas()
                    Pozo.informe_tiempo_en_llenarse_un_tanque()
                    
                    Prod.informe_fecha_produccion_diaria()
                    Prod.informe_produccion_diaria()
                    
                    Val.informe_fecha_actual()
                    Val.informe_precio_barril_actual()
                    
                    Op.informe_cantidad_personal()
                    Op.informe_costo_total_diario()
                    Op.informe_precio_venta_diario_barril()
                    
                    Ven.informe_ingreso_diario()
                    
                    input("\nPresiona una tecla para continuar...")
                    os.system('cls')
            
        elif opcion == 2:
            
            with open(ruta_diario, 'r') as f:
                lineas = f.readlines()
                if len(lineas) >= 188:
                    
                    Prod.informe_produccion_semanal()
                    Op.informe_costo_total_semanal()
                    Ven.informe_ingreso_semanal()
                    UN.informe_utilidad_neta()
                    
                    input("\nPresiona una tecla para continuar...")
                    os.system('cls')
                    
                else:
                    print("Aun no tienes 7 días para esto.")
                    input("Presiona una tecla para continuar...")
                    os.system('cls')
                    
        elif opcion == 3:
            print("Finalizando programa...")
            break
        
        else:
            input("No ha ejecutado una de las opciones...")
            os.system('cls')
            
if __name__ == "__main__":
    main()