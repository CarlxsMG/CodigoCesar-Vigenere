cadena = "paris vaut bien une messe"
cadena_lista=[]
cadena_NoSpace = cadena.replace(" ","")
lista_cadena_cod = []
clave = "loup"
alfabeto = "abcdefghijklmnñopqrstuvwxyz"

message_cod = ""


for i in range(0,len(cadena_NoSpace)):   ## RECORRE EL IMPUT

    posicion = alfabeto.find(cadena_NoSpace[i])    ## BUSCA LA POSICION DE LA POSICION DE I EN EL ALFABETO // DEVUELVE -1 SI NO ESTA

    if(posicion==-1):       ## SI NO ESTA EN ALFABETO
        message_cod += cadena_NoSpace[i]                                            ## SE INSERTA EL MISMO VALOR
    else:                                                                           ## SI ESTA EN EL ALFABETO
        valor_clave = clave[i%(len(clave))]                                         ## BUSCA LA POSICION DEL CARACTER CLAVE PARA LA CODIFICACION DE i
        pos_clave = alfabeto.find(valor_clave)                                      ## LO BUSCA EN EL ALFABETO
        message_cod += alfabeto[(posicion+pos_clave)%len(alfabeto)]                 ## SE INSERTA VALOR CODIFICADO

for i in message_cod:
    lista_cadena_cod.append(i)

for j in cadena:
    cadena_lista.append(j)

while " " in cadena_lista:
    pos_Space = cadena_lista.index(" ")
    cadena_lista[pos_Space]="-"
    lista_cadena_cod.insert(pos_Space," ")

message_cod=""

for k in lista_cadena_cod:
    message_cod+=k

print("MENSAJE CODIFICADO:",message_cod)
    