from PIL import Image

config = {}

# 1. LECTURA SEGURA DE CONFIGURACIÓN
try:
    # Usamos 'with' para garantizar que el archivo se cierre pase lo que pase
    with open("config.txt", 'r') as archivo:
        for num_linea, linea in enumerate(archivo, start=1):
            linea_limpia = linea.strip()
            if not linea_limpia:  # Ignorar líneas vacías
                continue
                
            if '=' not in linea_limpia:
                raise ValueError(f"Formato incorrecto en línea {num_linea}: se esperaba 'clave=valor'.")
                
            clave, valor = linea_limpia.split('=')
            clave = clave.strip()
            valor = valor.strip()
            
            # Conversión de tipos de datos de forma segura
            config[clave] = float(valor) if "." in valor else int(valor)

except FileNotFoundError:
    print("Error Crítico: El archivo de configuración 'config.txt' no existe.")
    exit(1)
except ValueError as e:
    print(f"Error de Configuración: {e}")
    exit(1)


# 2. LECTURA SEGURA DE LOS DATOS CSV
try:
    with open("clase.csv", 'r') as data:
        datos = data.readlines()
        
    if not datos:
        raise ValueError("El archivo 'clase.csv' está vacío.")
        
    datos.pop(0)  # Remover encabezado

except FileNotFoundError:
    print("Error Crítico: El archivo de datos 'clase.csv' no fue encontrado.")
    exit(1)
except ValueError as e:
    print(f"Error de Datos: {e}")
    exit(1)


# 3. PROCESAMIENTO MATEMÁTICO Y GENERACIÓN DE IMAGEN
try:
    # Validar la existencia de las llaves obligatorias en el diccionario
    claves_obligatorias = ["alto", "ancho", "max_iter"]
    for c in claves_obligatorias:
        if c not in config:
            raise KeyError(f"Falta la variable de configuración obligatoria: '{c}'.")

    alto, ancho, max_iter = config["alto"], config["ancho"], config["max_iter"]

    # Validación de reglas del dominio usando raise
    if max_iter <= 0:
        raise ZeroDivisionError("La variable 'max_iter' debe ser un número entero mayor a cero.")
    if alto <= 0 or ancho <= 0:
        raise ValueError("Las dimensiones 'alto' y 'ancho' deben ser mayores a cero.")

    img = Image.new('HSV', (alto, ancho))

    for num_fila, dato in enumerate(datos, start=2):  # start=2 por el encabezado eliminado
        dato_limpio = dato.strip()
        if not dato_limpio:
            continue
            
        partes = dato_limpio.split(",")
        if len(partes) != 3:
            raise ValueError(f"Fila {num_fila} malformada en el CSV. Se esperaban 3 valores y se obtuvieron {len(partes)}.")

        fila, columna, iteraciones = map(int, partes)
        
        # Validación de límites de la imagen (Evitar IndexError oculto de PIL)
        if columna >= ancho or fila >= alto or columna < 0 or fila < 0:
            raise IndexError(f"Línea {num_fila}: Las coordenadas ({columna}, {fila}) exceden el tamaño de la imagen ({ancho}x{alto}).")

        brillo = 40 if (iteraciones == max_iter) else int((iteraciones / max_iter) * 255)
        img.putpixel((columna, fila), (brillo, 255, 255))
        
    img_rgb = img.convert('RGB')
    img_rgb.save("mandelbrot-clase.png")

except KeyError as e:
    print(f"Error de Parámetro: {e}")
except ZeroDivisionError as e:
    print(f"Error Matemático: {e}")
except IndexError as e:
    print(f"Error de Límites: {e}")
except ValueError as e:
    print(f"Error de Conversión en Procesamiento: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado al procesar la imagen: {e}")
else:
    # El "Happy Path" del PDF: solo dice DONE si todo el flujo terminó sin levantar excepciones
    print("DONE")