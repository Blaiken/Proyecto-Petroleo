class PozoPetrolero:
    def __init__(self,capacidad_tanque,cantidad_tanques):
        self.capacidad_tanque = capacidad_tanque
        self.cantidad_tanques = cantidad_tanques
        
    def ingresar_capacidad_tanque(self):
        pass
    
    def ingresar_cantidad_tanques(self):
        pass
    
    def informe_capacidad_tanque(self,capacidad_tanque):
        print(f"Capacidad tanque: {capacidad_tanque}")
    
    def informe_cantidad_tanques(self, cantidad_tanques):
        print(f"Cantidad tanques: {cantidad_tanques}")
        
class Produccion:
    def __init__(self,f_dia,f_mes,f_ano):
        self.f_dia = f_dia
        self.f_mes = f_mes
        self.f_ano = f_ano
        
    def ingresar_fecha_produccion(self):
        pass
    
    def c_produccion_diaria(self):
        pass
    
    def c_produccion_semanal(self):
        pass
    
    def informe_fecha_produccion(self,dia,mes,ano):
        print(f"Fecha: {dia}-{mes}-{ano}")
    
    def informe_produccion_diaria(self):
        pass
    
    def informe_produccion_semanal(self):
        pass
    
class Operaciones:
    def __init__(self,costos_diarios,manten_diario,suminis_diario,personal_diario):
        self.costos_diarios = costos_diarios
        self.manten_diario = manten_diario
        self.suminis_diario = suminis_diario
        self.personal_diario = personal_diario
        
    def c_costo_total_semanal(self):
        pass
    
    def c_costo_total_diario(self):
        pass
    
    def c_ingreso_semanal(self):
        pass
    
    def informe_costo_total_diario(self):
        pass
    
    def  informe_costo_total_sem(self):
        pass
    
    def informe_ingreso_semanal(self):
        pass
    
class Valor:
    def __init__(self, precio_barril_actual, fecha_actual):
        self.precio_barril_actual = precio_barril_actual
        self.fecha_actual = fecha_actual
        
    def ingresar_fecha_actual(self):
        pass
    
    def informe_fecha_actual(self):
        pass
    
class UtilidadNeta:
    def __init__(self, ingreso_semanal, costo_total_semanal):
        self.ingreso_semanal = ingreso_semanal
        self.costo_total_semanal = costo_total_semanal
        
    def c_utilidad_neta_semanal(self):
        pass
    
    def informe_utilidad_neta_semanal(self):
        pass
        
print("FECHA: ")
p_dia = int(input("Dia: "))
p_mes = int(input("Mes: "))
p_ano = int(input("Año: "))
Produccion(p_dia,p_mes,p_ano)

Prod = Produccion(p_dia,p_mes,p_ano)
Prod.informe_fecha_produccion(p_dia,p_mes,p_ano)


cap_tanque = int(input("Capacidad tanque: "))
can_tanques = int(input("Cantidad tanques: "))
PozoPetrolero(cap_tanque, can_tanques)

PozoP = PozoPetrolero(cap_tanque, can_tanques)
PozoP.informe_cantidad_tanques(cap_tanque)
PozoP.informe_capacidad_tanque(can_tanques)



