from CrearArchivos.ReporteErrores import *

def revisar(ruta):
    
        archivo = open (ruta,'r')
        datos = archivo.read()
        revisarErrores(datos)
        erroresHTML(datos)
        conseguirTexto(datos)
        archivo.close()

        #print(datos)

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
                                nError=nError
                        else:
                                nError=nError+1
                                print("Error # ", nError, ". ",token, "Fila: ",nFila, "  Columna: ",nColumna)

def conseguirTexto(datos):
    datosSeparados=datos.split("<Texto>")
    datosSeparados=datosSeparados[1].split("</Texto>")
    print(datosSeparados[0])
    
revisar("Archivo.txt")    
texto=" hola \nque tal?"

prueba="rrrr <Texto> EN MEDIO </Texto> AMAMAMAMMA"

#conseguirTexto(prueba)

#print(texto)
#revisarErrores(texto)
#erroresHTML(texto)