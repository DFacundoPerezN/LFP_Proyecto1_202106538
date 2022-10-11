from CrearArchivos.ReporteErrores import *

def revisar(ruta):
    
        archivo = open (ruta,'r')
        datos = archivo.read()
        revisarErrores(datos)
        erroresHTML(datos)

        archivo.close()

        print(datos)


def revisarErrores(datos):
        nFila=0
        nError=0

        lineas =datos.split("\n")
        for linea in lineas:
                nFila=nFila+1
                nColumna =0

                for token in linea:
                        nColumna=nColumna+1
                        
                        if(token.isdigit()|token.isalpha() or token==" " or token == ">" or token=="<" or token == "/" or token=="," or token == "[" or token=="]" or token == "=" or token == "."):
                                print('es caracter aceptado',token)
                        else:
                                nError=nError+1
                                print("Error # ", nError, ". ",token, "Fila: ",nFila, "  Columna: ",nColumna)

                
    
#revisar("Archivo.txt")    
texto=" hola \nque tal?"

print(texto)
revisarErrores(texto)
erroresHTML(texto)