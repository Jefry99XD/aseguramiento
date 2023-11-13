# fecha = (year, month, day)
def fecha_es_tupla(f):
    #Todas las fechas deben ser creadas como tuplas de tres números enteros positivos (ternas)
    return f[0] > 0 and f[1] > 0  and f[2] >0 

def bisiesto(f):
#Dado un año perteneciente al rango permitido, determinar si este es bisiesto.
    return f[0] % 4 == 0 and (f[0] %100 != 0 or f[0] % 400 ==0)
    
def fecha_es_valida(f):
    # Dada una fecha, determinar si ésta es válida según el calendario gregoriano
    if not fecha_es_tupla(f):
        return False
    match f[2]:
        case 31:
            if f[1] == 1 or f[1] == 3 or f[1] == 5 or f[1] == 7 or f[1] == 8 or f[1] == 10 or f[1] == 12:
                return True
            elif f[1] < 13 and f[2] < 32:
                return True
            else:
                return False
        case 30:
            if f[1] == 4 or f[1] == 6 or f[1] == 9 or f[1] == 11:
                return True
            elif f[1] < 13 and f[2] < 32:
                return True
            else:
                return False
        case 29:
            if f[1] == 2:
               if bisiesto(f):
                   return True
               else:
                   return False
            elif f[1] < 13 and f[2] < 32:
                return True
            else:
                return False
        case _:
            if f[1] < 13 and f[2] < 32:
                return True
            else:
                return False
            
def dia_siguiente(f):
    # Dada una fecha válida, determinar la fecha del día siguiente
    siguiente = [f[0], 1, 1]
    if f[1] == 12 and f[2]==31:
        siguiente[0] = f[0]+1
        return tuple(siguiente)
    match f[2]:
        case 31:
            if f[1] == 1 or f[1] == 3 or f[1] == 5 or f[1] == 7 or f[1] == 8 or f[1] == 10 or f[1] == 12:
                siguiente[2] = 1
                siguiente[1] = f[1] + 1
            else:
                siguiente[1] = f[1]
                siguiente[2] = f[2] + 1
        case 30:
            if f[1] == 4 or f[1] == 6 or f[1] == 9 or f[1] == 11:
                siguiente[2] = 1
                siguiente[1]= f[1] + 1
            else:
                siguiente[1] = f[1]
                siguiente[2] = f[2] + 1
        case 29:
            if f[1] == 2:
               siguiente[2] = 1
               siguiente[1]= f[1] + 1
            else:
                siguiente[1] = f[1]
                siguiente[2] = f[2] + 1
        case _:
            if f[1]==2 and f[2] == 28:
                if bisiesto(f):
                    siguiente[1] = f[1]
                    siguiente[2] = f[2] + 1
                else:
                    siguiente[1] = f[1] + 1
                    siguiente[2] = 1
            else:
                siguiente[1] = f[1]
                siguiente[2] = f[2] + 1
    return tuple(siguiente)

def ordinal_dia(f):
    if f[1] == 1:
        return f[2]
    match f[1]:
        case 12:
            if bisiesto(f):
                return 335 + f[2]
            else:
                return 334 + f[2]
        case 11:
            if bisiesto(f):
                return 305 + f[2]
            else:
                return 304 + f[2]
        case 10:
            if bisiesto(f):
                return 273 + f[2]
            else:
                return 274 + f[2]
        case 9:
            if bisiesto(f):
                return 244 + f[2]
            else:
                return 243 + f[2]
        case 8:
            if bisiesto(f):
                return 213 + f[2]
            else:
                return 212 + f[2]
        case 7:
            if bisiesto(f):
                return 182 + f[2]
            else:
                return 181 + f[2]
        case 6:
            if bisiesto(f):
                return 152 + f[2]
            else:
                return 151 + f[2]
        case 5:
            if bisiesto(f):
                return 121 + f[2]
            else:
                return 120 + f[2]
        case 4:
            if bisiesto(f):
                return 91 + f[2]
            else:
                return 90 + f[2]
        case 3:
            if bisiesto(f):
                return 60 + f[2]
            else:
                return 59 + f[2]
        case 2:
            return 31 + f[2]
'''
def imprimir_3x4(f):
    calcularYearGregoriano(f)
    return 

def calcularYearGregoriano(year):
'''