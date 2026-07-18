import random
import os


nombre_archivo = "archivo.csv"


try:
    print("Iniciando la generación de datos...")
    
   
    with open(nombre_archivo, "w") as archivo:
       
        archivo.write("X,Y,COLOR\n")

        for i in range(100_000):
            x = random.uniform(-10, 10)
            y = random.uniform(-10, 10)
            
            distancia = (x * x + y * y) ** 0.5
            iteraciones = 0
            color = 0
            
           
            while (distancia < 1) and (iteraciones < 100):
                distancia = distancia ** 2
                iteraciones += 1
                
            if distancia > 1: 
                color = 255  
            
           
            archivo.write(f"{x},{y},{color}\n")
            
except PermissionError as e:
    print(f"Error de Permisos: No se puede escribir en '{nombre_archivo}'. Asegúrate de que no esté abierto en Excel u otro programa. Detalles: {e}")
except (OSError, IOError) as e:
    print(f"Error de Entrada/Salida: Ocurrió un fallo en el disco duro o falta de espacio al escribir el archivo. Detalles: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado durante el procesamiento: {e}")
else:
    
    print("Done. El archivo se ha creado y guardado exitosamente.")