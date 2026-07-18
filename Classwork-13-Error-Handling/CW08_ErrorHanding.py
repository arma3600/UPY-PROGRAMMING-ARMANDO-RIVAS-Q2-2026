import math

# INPUT
a_in = input("Write the left endpoint of the interval: ").strip()
b_in = input("Write the right endpoint of the interval: ").strip()
f_x = input("Write the function to integrate: ").strip()
method = input("Write the integration method (LRM/RRM/MPM/TM): ").strip()

# PROCESS
area = None
validation_failed = False

try:
    try:
        if "pi" in a_in:
            a = math.pi
        else:
            a = float(a_in)
    except ValueError:
        print("[Error de entrada]: El límite inferior ingresado no es un número válido.")
        validation_failed = True
        raise

    try:
        if "pi" in b_in:
            b = math.pi
        else:
            b = float(b_in)
    except ValueError:
        print("[Error de entrada]: El límite superior ingresado no es un número válido.")
        validation_failed = True
        raise

    if a >= b:
        print("[Error de rango]: El límite izquierdo debe ser estrictamente menor que el derecho.")
        validation_failed = True
        raise ValueError()

    if not f_x:
        print("[Error de expresión]: No se detectó ninguna función matemática para evaluar.")
        validation_failed = True
        raise ValueError()

    if "^" in f_x:
        print("[Error de sintaxis]: Operador '^' no soportado. Recuerda usar '**' para las potencias en Python.")
        validation_failed = True
        raise ValueError()

    try:
        x = 1
        eval(f_x)
    except NameError:
        print("[Error de variable]: La ecuación contiene incógnitas o variables desconocidas (usa solo 'x').")
        validation_failed = True
        raise

    if method not in ["LRM", "RRM", "MPM", "TM"]:
        print(f"[Error de método]: '{method}' no es una opción válida. Elige entre LRM, RRM, MPM o TM.")
        validation_failed = True
        raise ValueError()

    n = 1000
    h = (b - a) / n
    area = 0.0

    if method == "TM":
        x = a
        area += (h / 2) * eval(f_x)
        
        for i in range(1, n):
            x = a + i * h
            area += (h / 2) * 2 * eval(f_x)
            
        x = b
        area += (h / 2) * eval(f_x)
        
    else:
        shift = 0
        constant = 0
        
        if method == "RRM":
            shift = 1
        elif method == "MPM":
            constant = h / 2
            
        for i in range(shift, n + shift):
            x = a + i * h + constant
            area += h * eval(f_x)

except ZeroDivisionError:
    print("[Error matemático]: Se detectó una división entre cero en el intervalo seleccionado (función indefinida).")
    area = None

except (SyntaxError, NameError, ValueError):
    area = None


# OUTPUT
if area is not None and not validation_failed:
    print(f"The integration of {f_x} is {area:.3f}")