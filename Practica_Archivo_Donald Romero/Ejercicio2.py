#Contador de lineas

#Solicitar al usuario el nombre del archivo
nombre_archivo=input("Ingrese el nombre del archivo:")

#Abrir el archivo en modo lectura
try:
    with open(nombre_archivo, "r") as archivo:
        lineas=archivo.readlines()   #Leer todas las lineas de una lista
        num_lineas=len(lineas)
        print(f"El archivo '{nombre_archivo}', tiene {num_lineas} lineas")  #Obtener y mostrar el numero de lineas
except FileNotFoundError: #Si el archivo no se encuentra
    print(f"Error: el archivo '{nombre_archivo}': no fue encontrado")
        
        
    