
controladora = 100

print("*********************************")
print("*** Empanadas el machetasoome ***")
print("*********************************")
print("*1.Agregar el sabor de empanada:*")
print("*2.Mostrar el sabor de empanada:*")
print("*3.Editasr el sabor de empanada:*")
print("*******0.Salir del proceso*******")
print("*********************************")

while (controladora!=0):
    empanada=None
    controladora=int(input("Digite una opciom: "))
    if controladora == 1:
        empanada =input("Cual es el sabor: ")
    elif controladora == 2:
         print(f"El sabor es: {empanada}")
    elif controladora == 3:
        empanada =input("Cual es el sabor: ")
    elif controladora == 0:
        print("Chao gonorrea")
    else: 
        print("OPCION INVALIDA")

