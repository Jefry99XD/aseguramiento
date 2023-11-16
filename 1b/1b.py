from datetime import date
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
            elif f[1] == 4 or f[1] == 6 or f[1] == 9 or f[1] == 11:
                return False
            elif f[1] < 13 and f[2] < 32:
                return True
            else:
                return False
        case 30:
            if f[1] == 4 or f[1] == 6 or f[1] == 9 or f[1] == 11:
                return True
            elif f[1] == 1 or f[1] == 3 or f[1] == 5 or f[1] == 7 or f[1] == 8 or f[1] == 10 or f[1] == 12:
                return False
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

def dia_semana(f):
    #
    if not fecha_es_valida(f):
        raise Exception("Fecha no valida")
    return int((f[2] +  f[0] + (f[0]/4) + (31*f[1]/12)) % 7)

def fecha_futura(f, n):
    if not fecha_es_valida(f):
        raise Exception("Fecha no valida")
    if n < 0:
        raise Exception("n no valido")
    if n ==0:
        return f
    fechaFutura = f
    for i in range(0, n):
        fechaFutura = dia_siguiente(fechaFutura)
    return fechaFutura
    
def dias_entre(f1, f2):
    if not fecha_es_valida(f1) and not fecha_es_valida(f2):
        raise Exception("Fecha no valida")
    dias = 0
    copy = f1
    if f1 < f2:
        while copy != f2:
            copy = dia_siguiente(copy)
            dias+=1
    else:
        copy2 = f2
        while copy2 != f1:
            copy2 = dia_siguiente(copy2)
            dias+=1
    return dias
    
    

def edad_al(f1, f2):
    if not fecha_es_valida(f1) and not fecha_es_valida(f2):
        raise Exception("Fecha no valida")
    if f1[0] > f2[0]:
         raise Exception("Fecha no valida")
    edad = [abs(f1[0]-f2[0]), abs(f1[1]-f2[1]), abs(f1[2]-f2[2])]
    if edad[1] == 0:
        if edad[2] > 0:
            edad[1]=f1[1]
            edad[0] -= 1
    return tuple(edad)
    
def fecha_hoy():
    f = (date.today().year, date.today().month, date.today().day)
    return f

def edad_hoy(f):
    if not fecha_es_valida(f):
        raise Exception("Fecha no valida")
    return edad_al(f, fecha_hoy())

a = (2020, 4, 22)
nac = (1999, 11,27)
print(a)
print("nacimiento prueba", nac)
print("dia semana ", dia_semana(fecha_hoy()))
print("fecha futura", fecha_futura(fecha_hoy(), 41))
print("dias entre", a, " ", fecha_hoy(), "  ", dias_entre(a, fecha_hoy()))
print("edad_al", edad_al((1999, 11,27), (2027,5,16)))
print("fecha hoy", fecha_hoy()) 
print("edad hoy", edad_hoy((1999, 11,27)))




    
