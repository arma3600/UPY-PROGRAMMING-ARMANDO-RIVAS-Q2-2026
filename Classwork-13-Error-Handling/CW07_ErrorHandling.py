class DigitoVerificadorError(Exception):
    pass


# INPUT

check = True
while check:
    try:
        rol = input("Ingrese el rol: ")
        
        # Validación de que exista el guion antes de separar
        if "-" not in rol:
            raise ValueError("Rol inválido: No tiene el formato XXXXXXXXX-X, el rol no trae guion")
        
        #Validar si hay mas de un guion
        if rol.count("-") > 1:
            raise ValueError("No tiene el formato XXXXXXXXX-X\n(el rol trae más de un guion)")
        
        rol_sin_digito, digito = rol.split("-")
    
        
        # Validación de caracteres numéricos
        if not rol_sin_digito.isnumeric():
            raise ValueError("Los digitos del rol deben ser numéricos ,la parte del rol antes del guion no son puros números")
        
             #Validacion de que el digito verificador sea un numero
        if not digito.isnumeric():
            raise ValueError("El digito verificador debe ser numérico\n(lo que va después del guion no es un número)")
        
        check = False
    except ValueError as e:
        print(f"Rol inválido: {e}")


# PROCESS

invertido = rol_sin_digito[::-1]

secuencia = [2, 3, 4, 5, 6, 7]
suma = 0

for index in range(len(invertido)):
    multiplicando = secuencia[index % 6]
    numero = int(invertido[index:index+1])
    suma += numero * multiplicando
    
total = suma % 11

verificador = 11 - total

# Validación del dígito verificador usando la excepción personalizada
try:
    if verificador != int(digito):
        raise DigitoVerificadorError(f"El digito verificado no coincide, (el dígito que escribiste no coincide con el que calcula tu programa calculado: {verificador}")
except DigitoVerificadorError as e:
    print(e)


# OUTPUT
else:
    print(f"{rol_sin_digito}-{verificador}")