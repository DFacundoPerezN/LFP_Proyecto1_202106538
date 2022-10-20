from tkinter import NE

inicioHTML="<!DOCTYPE html>  \n <html > \n "

cabezaHTML="<head>\n    <title>Diego Facundo Pérez Nicolau, 202106538</title>\n  </head>\n"
cabeceraHTML="  <body>\n  <header> <h1> Diego Facundo Pérez Nicolau, </br> 202106538</h1> </header> \n\n<article>"

empezarTabla="<article>\n<table Border=5> \n\n <tr> <td><h3>No. </h3></td> <td><h3> Lexema </h3></td> <td><h3> Tipo </h3></td> <td><h3> Columna</h3></td> <td><h3> Fila </h3></td> </tr>\n"

cerrarTablaHTMl ="\n</body>\n</html>"

def erroresHTML(datos):

    archivoHTMl = open ("PaginasHTML\ERRORES_202106538.html", "w")
    archivoHTMl.write(inicioHTML)
    archivoHTMl.write(cabezaHTML)
    archivoHTMl.write(cabeceraHTML)
    archivoHTMl.write(empezarTabla)


    nFila=0
    nError=0
    lineas =datos.split("\n")
    for linea in lineas:
        nFila=nFila+1
        nColumna =0

        for token in linea:
            nColumna=nColumna+1
            
            if(token.isdigit()|token.isalpha() or token==" " or token==">" or token=="<" or token=="/" or token=="," or token =="[" or token=="]" or token =="=" or token=="."):
                nError=nError    
            else:
                nError=nError+1
                nuevaLinea=str("\n <tr> <td> "+ str(nError)+ "</td> <td> "+str(token)+ "</td> <td> Error </td> <td>"+str(nColumna)+ " </td> <td> "+str(nFila)+ "</td> </tr>")
                archivoHTMl.write(nuevaLinea)


    archivoHTMl.write(cerrarTablaHTMl)
    archivoHTMl.close