print("---Bienvenido al supermercado de confianza---")
print("---Vamos a realizar el pago---")

def calcular_descuento(Valor,descuento=0.10):

    proceso = Valor * descuento

    return proceso

#Primera Llamada

monto1= float(input("Ingrese su valor inicial: "))
descuento1= calcular_descuento(monto1)
Valor_final_a_pagar= monto1-descuento1

print("Su valor inicial es de:" , monto1)
print("El descuento que se le aplicará es de:", descuento1,"%")
print("Su valor final a cancelar será de:", Valor_final_a_pagar)

#Segundo llamado

monto2=float(input("Ingrese su valor inicial: "))
porcentaje_de_descuento= int(input("Ingrese el descuento que quiere tener"))

descuento2= calcular_descuento(monto2,porcentaje_de_descuento/100)
Valor_final_a_pagar2= monto2-descuento2

print("Su valor inicial que debe pagar es de:",monto2)
print("El descuento que se le aaplico es de :",porcentaje_de_descuento,"%")
print("Su valor final a pagar es de :",Valor_final_a_pagar2)

