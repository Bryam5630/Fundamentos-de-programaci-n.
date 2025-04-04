# hay que abrir el archivo y decirle que hacer.

ruta= "C:/Users/User/Downloads/semana 16/deberconarchivos/my_notes.txt"  # se busca en donde esta el archivo

información=open(ruta,'r')   #se abre la ruta y le digo que lea

print(información.read())    # va a imprimir todo el texto que hay en el archivo.


