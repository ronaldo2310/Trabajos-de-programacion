# Ejemplo de lectura de un archivo de texto con readlines()
archi1=open("datos.txt","r")
lineas=archi1.readlines()
print("El archivo tiene", len(lineas), "lineas")
print("El contenido del archivo")
for linea in lineas:
    print(linea, end='')
archi1.close()