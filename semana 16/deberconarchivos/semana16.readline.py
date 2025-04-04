
ruta= "C:/Users/User/Downloads/semana 16/deberconarchivos/my_notes.txt"   # se busca en donde esta el archivo

información=open(ruta,'r')      #se abre la ruta y le digo que lo lea

print(información.readlines())     #aqui al poner el comando readlines, se imprime todo en una sola linea

