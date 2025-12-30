import qrcode
nombreArchivo=input("Dime el nombre del archivo sin la extension: ")
textoQR=input("Dime el texto o enlace para el codigo QR:")
imagen  = qrcode.make(textoQR)
fichero=open(nombreArchivo+".png","wb")
imagen.save(fichero)
fichero.close()
print("El codigo qr ha sido generado con exito")
print("El archivo esta guardado en la carptea del script ")