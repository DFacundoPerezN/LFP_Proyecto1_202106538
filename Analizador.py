from CrearArchivos.Analisis import*
import CrearArchivos.Analisis
import operaciones

inicioHTML="<!DOCTYPE html>  \n <html lang=\"es\"> \n "
cabezaHTML="<head>\n    <title> Revision Diego Facundo Pérez Nicolau, 202106538</title>\n  </head>\n"
cabeceraHTML="  <body>\n  <header> <h1> Operaciones, </br> aritmeticas</h1> </header> "


def conseguirTexto(datos):
    datosSeparados=datos.split("<Texto>")
    datosSeparados=datosSeparados[1].split("</Texto>")
    return (datosSeparados[0])

def conseguirOperaciones(datos):
    datosOP=datos.split("<Tipo>")
    datosOP=datosOP[1].split("</Tipo>")
    operaciones=datosOP[0]

    operaciones=operaciones.replace("\t", "")     
    #operaciones=operaciones.replace("\n", "")
    operaciones=operaciones.replace(" ", "")

    operaciones=operaciones.split("</Operacion>")
    listasOperaciones=[]

    for operacion in operaciones:
        try:
            listasOperaciones.append(hacerOperacion(operacion))
        except:
            operacion=operacion.replace("<", "")
            operacion=operacion.replace(">", "")
            operacion=operacion.split("\n")
            listasOperaciones.append(operacion)
    
    return listasOperaciones
        

def conseguirNumero(linea):
    try:
        datosSeparados=linea.split("<Numero>")
        datosSeparados1=datosSeparados[1].split("</Numero>")
        return datosSeparados1[0]
        #print(datosSeparados1[0])
    except:
        print("no hay numero")

def hacerOperacion(datos):
    componentes=[]
    lineas=datos.split("\n")
    lineas[1]=lineas[1].replace("<Operacion=","")
    lineas[1]=lineas[1].replace(">","")

    componentes.append(lineas[1])
    componentes.append(conseguirNumero(lineas[2]))
    try:
        componentes.append(conseguirNumero(lineas[3]))
    except:
        print("no hay segundo numero")

    respuesta=operaciones.ejecutarOperacion(lineas[1],float(componentes[1]),float(componentes[2]))
    componentes.append(respuesta)

    for c in componentes:
        print(c)

    return componentes

#hacerOperacion("<Operacion=RESTA>\n<Numero>84</Numero>\n<Numero>33.7</Numero>")

def crearHTMLResultados(ruta):
    archivo = open (ruta,'r')
    datos = archivo.read()   
    textoA = conseguirTexto(datos)
    listasOperaciones = conseguirOperaciones(datos)
    archivo.close()

    archivoHTMl = open ("PaginasHTML\RESULTADOS_202106538.html", "w")

    archivoHTMl.write(inicioHTML)
    archivoHTMl.write(cabezaHTML)
    archivoHTMl.write(cabeceraHTML)

    archivoHTMl.write("\n<article>")
    archivoHTMl.write(textoA)
    archivoHTMl.write("</article>\n")

    archivoHTMl.write("\n<article>")

    for operacion in listasOperaciones:
        archivoHTMl.write("\n<br>")
        archivoHTMl.write("---------------Operacion----------------")
        for componente in operacion:
            archivoHTMl.write("<br>")
            archivoHTMl.write(str(componente))

crearHTMLResultados("Archivo.txt")
