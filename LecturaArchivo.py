
def LeerEt(datos):    
    contador=1
    for objeto in datos:
        if objeto != ">":
            etiqueta = datos[1:contador]
           
            contador+=1
        else:
            print(etiqueta)
            break
        
    aux= contador
    for objeto in datos[contador:len(datos)]:
        
        info = datos[aux:contador]
        if objeto != "/":
            
            print(info, aux,"-", contador)

            contador+=1
        else:
            print(info)
            break


def seleccionarEtiqueta(etiqueta):
    e= etiqueta
    match etiqueta:
        case "Texto"| "texto":
            return e 
        case "Tipo" | "tipo":
            return e
        case "Funcion" |"funcion":
            return e 
        case "Estilo"|"estilo":
            return e   
        case _:
            print("¡ETIQUETA NO VÁLIDA!")






def cargaMasiva(ruta=None):  
        print('Subiendo datos') #Declaracion de que se estan subiendo
        print("Ruta: ", ruta)
        nombreArchivo = 'Archivo.txt'
        #nombreArchivo = ruta  tomar nombre y ruta del archivo de la barra de texto
        archivo = open (nombreArchivo,'r',encoding = "utf-8")   #Creando la variable archivo para python y diciendo qeu le lea con tildes y ñ
        datos = archivo.read()  #la variable datos toma el texto del archivo
        datos=datos.replace("\t", "")
        #print(datos)      
        datos=datos.replace("\n", "")
        datos=datos.replace(" ", "")
        #print(datos)
        LeerEt(datos)
        archivo.close()     #cierra el archivo

cargaMasiva()

