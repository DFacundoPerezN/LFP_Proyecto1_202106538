import math


def ejecutarOperacion(operacion, a= None, b=None): #Metodo para todas las operaciones
    match operacion:
        case "SUMA"| "suma":
            return a+b 
        case "RESTA" | "resta":
            return a-b
        case "MULTIPLICACION" |"multiplicacion":
            return a*b 
        case "DIVISION"|"division":
            return a/b    
        case "POTENCIA"|"potencia":
            return a^b 
        case "RAIZ"|"raiz":
            return a^(1/b)
        case "MOD"|"mod":
            return a%7
        case "INVERSO"|"inverso":
            return 1/a
        case "SENO"|"seno":
            return math.sin(a)
        case "COSENO"|"coseno":
            return math.cos(a) 
        case "TANGENTE"|"tangente":
            return math.tan(a)
        case _:
            print("¡OPERACIÓN NO VÁLIDA!")

