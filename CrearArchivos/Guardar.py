import os

def guardar(ruta, nombreArchivo):
    
        archivo = open (ruta,'r')
        datos = archivo.read()
        archivo.close()

        newFile = open (nombreArchivo, "w")
        newFile.write(datos)
        newFile.close

        print(datos)
    