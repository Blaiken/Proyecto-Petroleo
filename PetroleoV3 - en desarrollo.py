from datetime import date

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
        
    def set_capacidad_tanque(self, cap_tanque):
        self.__capacidad_tanque.append(cap_tanque)
        
    def get_capacidad_tanque(self):
        return self.__capacidad_tanque
        
    def informe_capacidad_tanque(self):
        with open(ruta_diario, "a") as archivo:
            archivo.writelines(f"DATOS DIARIOS:\n\n- Limite de los tanques:\n{self.get_capacidad_tanque()[0]}")
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
            archivo.writelines(f"\n- Fecha:\n{self.get_fecha_produccion_diaria()[0]}")
        print(f"- Fecha: {self.get_fecha_produccion_diaria()[0]}")
    
    def c_produccion_diaria(self):
        produccion_diaria = round(self.pozo.get_capacidad_tanque()[0] * self.pozo.get_cantidad_tanques()[0] / self.pozo.get_horas_trabajadas()[0] / 159, 3)
        return produccion_diaria
    
    def informe_produccion_diaria(self):
        with open(ruta_diario, "a") as archivo:
            archivo.writelines(f"\n- Producción diaria:\n{self.c_produccion_diaria()}")
        print(f"- Producción diaria: {self.c_produccion_diaria()}")
        
    def c_produccion_semanal(self):
        
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[11]
            linea1 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[34]
            linea2 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[57]
            linea3 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[80]
            linea4 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[103]
            linea5 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[126]
            linea6 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[149]
            linea7 = linea_especifica.strip()

        produccion_semanal = round(float(linea1) + float(linea2) + float(linea3) + float(linea4) + float(linea5) + float(linea6) + float(linea7), 3)
        return produccion_semanal
    
    def informe_produccion_semanal(self):
        with open(ruta_semanal, "a") as archivo:
            archivo.writelines(f"DATOS SEMANAL:\n\n- Producción semanal:\n{self.c_produccion_semanal()}")
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
        with open(ruta_diario, "a") as archivo:
            archivo.writelines(f"\n- Costo total diario:\n{self.c_costo_total_diario()}")
        print(f"- Costo total diario: {self.c_costo_total_diario()}")
        
    def c_costo_total_semanal(self):
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[17]
            linea1 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[40]
            linea2 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[63]
            linea3 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[86]
            linea4 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[109]
            linea5 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[132]
            linea6 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[155]
            linea7 = linea_especifica.strip()

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
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[21]
            linea1 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[44]
            linea2 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[67]
            linea3 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[90]
            linea4 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[113]
            linea5 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[136]
            linea6 = linea_especifica.strip()
            
        with open(ruta_diario, "r") as archivo:
            lineas = archivo.readlines()
            linea_especifica = lineas[159]
            linea7 = linea_especifica.strip()

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

while True:
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
        
        archivo = open(f"Universidad\\Datos_diarios_{contenido}.txt", "a")
        archivo.close()
        
        with open(f"Universidad\\Datos_diarios_{contenido}.txt", "r") as f:
            lineas = f.readlines()
            
            if len(lineas) >= 160:
                
                suma = int(contenido) + 1
                caracter = str(suma)
                archivo = open(f"Universidad\\contador.txt", "w")
                archivo.writelines(caracter)
                archivo.close()
                input("¡Ya has completado una semana!\nPresiona Enter para continuar...")
                archivo = open(f"Universidad\\Datos_diarios_{caracter}.txt", "a")
                archivo.close()
                
            else:
        
                print("-------------------------")
                print(" DATOS - POZO PETROLERO ")
                print("-------------------------")
                cap_tanque = float(input("Ingrese la capacidad de los tanques: "))
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
                
                input("Presiona una tecla para continuar...")
        
    elif opcion == 2:
        
        numero = input("Diga el numero del archivo que quiera saber el total: ")
        
        with open(f"Universidad\\Datos_diarios_{numero}.txt", 'r') as f:
            lineas = f.readlines()
            if len(lineas) >= 160:
                
                Prod.informe_produccion_semanal()
                Op.informe_costo_total_semanal()
                Ven.informe_ingreso_semanal()
                UN.informe_utilidad_neta()
                
                input("Presiona una tecla para continuar...")
                
            else:
                print("Aun no tienes 7 días para esto.")
                input("Presiona una tecla para continuar...")
                
    elif opcion == 3:
        print("Finalizando programa...")
        break
    
    else:
        input("No ha ejecutado una de las opciones...")