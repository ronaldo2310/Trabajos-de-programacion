#Diario personal simple
from datetime import datetime

#solicitar la emtrada al usuario
entrada=input("Escribe tu entrada de diario:")

#Fecha y hora actual
ahora=datetime.now()
fecha_ahora=ahora.strftime("%Y-%m-%d %H:%M:%S")

#Abrir el archivo diario y escribir la entrada
with open ("diario.txt", "a") as archivo:
    archivo.write(f"{fecha_ahora}\n")
    archivo.write(f"{entrada}\n")
    
#Mostramos la confirmacion
print("Entrada guardada en diario.txt")
    

