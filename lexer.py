#fabian y ricky 
import re

# abre el archivo y giuarda cada línea en una lista y se recorre por lineas
def lexerAritmetico(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    #el ":<N" sirve para llenar espacios y asi que se vea uniforme, 
    # inicia a contar 30 espacios desde el primer caracter que se lee
    print(f"{'Token':<30} {'Tipo'}")

    for linea in lineas:
        linea = linea.strip()

        i = 0
        while i < len(linea):

            # si es espacio, se suma i+1 y no se toma en cuenta
            if linea[i].isspace():
                i += 1
                continue

            #se pone el rango i+2 para que se descarte que es una division 
            if linea[i:i+2] == "//":
                comentario = linea[i:]
                print(f"{comentario:<30} Comentario")
                break

            if linea[i] == '(':
                print(f"{'(':<30} Paréntesis que abre")
                i += 1
                continue

            if linea[i] == ')':
                print(f"{')':<30} Paréntesis que cierra")
                i += 1
                continue

            if linea[i] == '=':
                print(f"{'=':<30} Asignación")
                i += 1
                continue

            if linea[i] == '+':
                print(f"{'+':<30} Suma")
                i += 1
                continue
            if linea[i] == '*':
                print(f"{'*':<30} Multiplicación")
                i += 1
                continue

            if linea[i] == '/':
                print(f"{'/':<30} División")
                i += 1
                continue

            if linea[i] == '^':
                print(f"{'^':<30} Potencia")
                i += 1
                continue

            if linea[i] == '-':
            
                #el -? hace que el signo sea opcional, \.\d+ permite que haya numeros despues de un punto opcional igual
                #[eE][+-]?\d+ permite que haya un numero entero despues de la Ee. en resumen esto nos 
                # da la opcion de que sea un numero entero, decimal o de notacion cientifica.
                match = re.match(r'-?\d+(\.\d+)?([eE][+-]?\d+)?', linea[i:])
                if match:
                    token = match.group(0) #para que guarde el numero completo que se encontró, con todo y despues del punto 
                    if '.' in token or 'E' in token or 'e' in token:
                        print(f"{token:<30} Real")
                    else:
                        print(f"{token:<30} Entero")
                    i += len(token)#que i pase ya al siguiente dato 
                else:
                    print(f"{'-':<30} Resta")
                    i += 1
                continue

                #si no inicia con "-"
            match = re.match(r'-?\d+(\.\d+)?([eE][+-]?\d+)?', linea[i:])
            if match:
                token = match.group(0)
                if '.' in token or 'E' in token or 'e' in token:
                        print(f"{token:<30} Real")
                else:
                    print(f"{token:<30} Entero")
                i += len(token) 
                continue

            # cualquier variable de letra mayuscula o minuscula 
            match = re.match(r'[a-zA-Z]', linea[i:])
            if match:
                token = match.group(0)
                print(f"{token:<30} Variable")
                i += 1
                continue

lexerAritmetico("expresiones.txt")