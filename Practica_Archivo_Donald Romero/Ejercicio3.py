#Generador de lista de compras
#Abrir el archivo en modo escritura
with open ("compras.txt", "w") as archivo:
    print("Ingrese los productos uno por uno, escriba la palabra 'fin' para terminar.")
    while True:
        producto=input("producto:")  #Solicitar el prodcuto al usuario
        if producto.lower()=="fin":    #Verificar si el usuario quiere terminar
            break
        archivo.write(producto + "\n")  #Escribir los productos en el archivo
        
#Notificar al usuario
print("Lista de compras guardadas en compras.txt")        