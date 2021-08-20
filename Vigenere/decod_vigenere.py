message = "aomxd kuke pctx jht wsnio"
message_list = []
message_NoSpace = message.replace(" ","")
clave = "loup"
message_NoSpace_decod = ""
message_decod = ""
message_decod_list = []

alfabeto = "abcdefghijklmnñopqrstuvwxyz"

for i in range (0,len(message_NoSpace)):
    pos_clave = i%len(clave)                        ## RELACIONA LA POSICION DEL CARACTER CON SU CARACTER CORRESPODIENTE DE LA CLAVE
    pos_clave_alf = alfabeto.find(clave[pos_clave])        ## BUSCA EL CARACTER CLAVE EN EL ALFABETO
    pos_i = alfabeto.find(message_NoSpace[i])                        ## BUSCA EL CARACTER CODIFICADO EN EL ALFABETO

    pos_character = pos_i - pos_clave_alf           ## BUSCA LA POSICION DEL CARACTER DECODIFICADO

    pos_alfabeto = pos_character%len(alfabeto)

    message_NoSpace_decod += alfabeto[pos_alfabeto]

for j in message:
    message_list.append(j)
for k in message_NoSpace_decod:
    message_decod_list.append(k)

while " " in message_list:
    pos_Space = message_list.index(" ")
    message_list[pos_Space]="-"
    message_decod_list.insert(pos_Space," ")

for l in message_decod_list:
    message_decod+=l

print("MENSAJE DESCODIFICADO:",message_decod) 
