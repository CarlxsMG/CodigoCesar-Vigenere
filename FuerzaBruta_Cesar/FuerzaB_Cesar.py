## CODIFICA EL MENSAJE
def codCes(message,alf,k):  

    message_cod = ""

    for i in message:   ## RECORRE EL IMPUT

        posicion = (alf.find(i))    ## BUSCA LA POSICION DE LA POSICION DE I EN EL ALFABETO // DEVUELVE -1 SI NO ESTA

        if(posicion==-1):       ## SI NO ESTA EN ALFABETO
            message_cod += i    ## SE INSERTA EL MISMO VALOR
        else:                                                   ## SI ESTA EN EL ALFABETO
            message_cod += alf[(posicion+k)%len(alf)]      ## SE INSERTA EL MISMO VALOR
    
    return message_cod      ## DEVUELVE EL IMPUT CIFRADA

## PRUEBA TODAS LAS COMBINACIONES
def FuerzaBruta(cod_input,alf,message):    

    for i in range(-1,-len(alf),-1):
        decod = ""                  ## VARIABLE MENSAJE DESCODIFICADO

        for j in cod_input:         ## RECORRE EL IMPUT    
            if j not in alf:        ## INSERTA EL MISMO VALOR SI NO ESTA EN EL ALFABETO
                decod += j
            else:                   
                posicion = alf.find(j)
                decod += alf[posicion+i]

        if decod == message:
            return decod, -(i)
    
    return None


## ----------------------------------------------------
alfabeto = "abcdefghijklmnñopqrstuvwxyz"

patron = int(input("Introduce patron\n"))
character = input("Introduce 1 cadena de caracteres\n")

cod_input = codCes(character,alfabeto,patron)
FuerzaBruta_var = FuerzaBruta(cod_input,alfabeto,character)

if FuerzaBruta_var == None:
    print("No he podido descifrarla")
else:
    print("\n"*9)
    print(cod_input)
    print("LA TENGO :)")
    print("El mensaje original es:",FuerzaBruta_var[0])
    print("El patron usado fue", FuerzaBruta_var[1])


