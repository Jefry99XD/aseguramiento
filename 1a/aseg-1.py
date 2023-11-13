# fecha = (year, month, day)
def fecha_es_tupla(f):
    return f[1] > 0 and f[1] < 13 and f[2] >0 and f[2] < 32
   
def bisiesto(f):
    if f[0] % 4 == 0 and (f[0] %100 != 0 or f[0] % 400 ==0):
        return True
    else:
        return False
    
def fecha_es_valida(f):
    
    return 

def dia_siguiente():
    return 

def ordinal_dia():
    return 

def imprimir_3x4():
    return 
 