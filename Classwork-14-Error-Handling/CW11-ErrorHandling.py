import random
import os

# DEFINICIÓN DEL NOMBRE DEL ARCHIVO
nombre_archivo = "archivo.csv"

# PROCESS & OUTPUT (Protegido dentro de una estructura contextual segura)
try:
    print("Iniciando la generación de datos...")
    
    # 'with open' asegura que el archivo se cierre pase lo que pase (incluso ante errores)
    with open(nombre_archivo, "w") as archivo:
        # ESCRIBIR ENCABEZADOS
        archivo.write("X,Y,COLOR\n")

        for i in range(100_000):
            x = random.uniform(-10, 10)
            y = random.uniform(-10, 10)
            
            distancia = (x * x + y * y) ** 0.5
            iteraciones = 0
            color = 0
            
            # El ciclo corre en entornos matemáticos controlados
            while (distancia < 1) and (iteraciones < 100):
                distancia = distancia ** 2
                iteraciones += 1
                
            if distancia > 1: 
                color = 255  
            
            # Escritura en disco
            archivo.write(f"{x},{y},{color}\n")
            
except PermissionError as e:
    print(f"Error de Permisos: No se puede escribir en '{nombre_archivo}'. Asegúrate de que no esté abierto en Excel u otro programa. Detalles: {e}")
except (OSError, IOError) as e:
    print(f"Error de Entrada/Salida: Ocurrió un fallo en el disco duro o falta de espacio al escribir el archivo. Detalles: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado durante el procesamiento: {e}")
else:
    # Se ejecuta únicamente si el archivo se generó y escribió por completo sin fallos
    print("Done. El archivo se ha creado y guardado exitosamente.")