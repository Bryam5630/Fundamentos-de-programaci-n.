# crear el diccionario, y hay que agreagr datos, como nos pide la tarea
informacion_personal = {
    "nombre": "Carlos",
    "edad": 25,
    "ciudad": "Quito",
    "profesion": "Estudiante"
}

#aqui ya se empeiza a modificar la ciudad
informacion_personal["ciudad"] = "Guayaquil"

# aqui se agrega una nueva clave valor diferente
informacion_personal["pasatiempo"] = "Jugar fútbol"

# aqui verificamos si telefono existe en el diccionario , si no esta lo agregamos
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0991234567"

# eliminamos la clave edad
del informacion_personal["edad"]


print(informacion_personal)
