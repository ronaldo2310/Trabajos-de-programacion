#Eliminar lineas del archivo
#Abrir el archivo y leer lineas
with open("datos.txt", "r", enconding="utf-8") as archivo:
    lineas=archivo.readlines()
    
#Filtrar las lineas que no contienen "Segunda linea"
lineas_filtradas=[linea for linea in lineas if linea.strip() !="Segunda linea"] 

#Sobreescribir el archivo con la lineas filtradas
with open("datos.txt", "w", enconding="utc-8") as archivo:
    archivo.wrtitelines(lineas_filtradas)    