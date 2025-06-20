#Solicitando datos al usuario
nombre=input("Ingrese tu nombre:")
apellido=input("Ingrese su apellido:")
edad=input("Ingrese su edad:")
salario=input("Ingrese su salario:")

#Formtear los datos de una linea
linea=f"{nombre},{apellido},{edad},{salario}\n"

#Guardar los datos en un archivo
ruta=input("Nombre del archivo:")
with open(ruta,"a") as archivo:
    archivo.write(linea)
    archivo.write("Primera linea\n")
    archivo.write("Segunda linea\n")
    archivo.write("Tercera linea\n")
    
print(f"Datos guardados correctamentes.")    