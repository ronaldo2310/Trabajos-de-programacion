#Lector de datos CSV
#Abrir el archivo productos.csv en modo lectura y con codificacion utf-8
with open ('producto.csv', 'r', encondig='utf-8') as archivo:
    #Recorrer cada linea del archivo
    for linea in archivo:
        linea=linea.strip() #Quitar los espacios 
        if not linea:
            continue #para saltar las lineas vacias
        partes=linea.slipt(',') #se va a separar la lineas en partes utilizando las comas
        if len(partes) != 4:
            print("Lineas con formato incorrecto:", linea) #Avisar si la linea no va tener 3 elementos
            continue
        numero, nombre, precio, cantidad=partes #Asignar las partes para la variable
        #Imprimir de forma ordenada
        print(f"{numero} | Producto: {nombre} | precio: ${precio} | stock: {cantidad} unidades")