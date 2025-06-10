#guardamos el archivo
# abrimos el archivo
escritura= open("archivos.txt", "w")
escritura.write("esto se escribio en el archivo\n y esto en la linea siguiente\n\t\t\tY esto en una linea tabulada\n")
# cerramos el archivo
escritura.close()

#lectura de ficheros
lectura= open("archivos.txt.","r")
#leemos una linea
leelinea=lectura.readline()
print("leyendo una linea\n:"+leelinea)
lectura.close()
lectura= open("archivos.txt.","r")
leetodo=lectura.readlines()  
print(type(leetodo))
#podemos usar redlines, que devuelve una lista con cada linea
print("leyendo todo \n"+leetodo[1])