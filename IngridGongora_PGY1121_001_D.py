
def grabar(datos_alumno):
    run = input(print("Run: "))
    input(print("Nombre: "))
    input(print("Apellido: "))
    input(print("Fecha de Nacimiento: "))
    input(print("Carrera: "))

    asignatura = ["asignatura1", "asignatura2", "asignatura3", "asignatura4"]
    promedio = ["nota1", "nota2", "nota3", "nota4"]
    asig_promedio = zip(asignatura, promedio)
    for elemento1, elemento2 in asig_promedio:
            print(f"{elemento1:15} {elemento2}") 

def buscar(run_alumno):
    run_alumno = input(print("Ingrese el run del alumno que desea buscar: ")) 

def imprimir_certificados():
    print("¿Que certificado desea imprimir?")
    print("1) Alumno regular")
    print("2) Notas")
    print("3) Matricula")
    opc = int(input(print("Opcin: ")))

    if opc == 1: 
        print("Certificado Alumno Regular")
        print("--------------------------")
        print("Run Alumno: ")
        print("Nombre Completo: ")
        print("Carrera: ")
    elif opc == 2:
        print ("Certificado de Notas")
        print("Run Alumno: ")
        print("Nombre Completo: ")
        print("Carrera: ")

        asignatura = ["asignatura1", "asignatura2", "asignatura3", "asignatura4"]
        promedio = ["nota1", "nota2", "nota3", "nota4"]
        asig_promedio = zip(asignatura, promedio)
        for elemento1, elemento2 in asig_promedio:
            print(f"{elemento1:15} {elemento2}") 
    else:
        print("Certificado Matricula")
        print("--------------------------")
        print("Run Alumno: ")
        print("Nombre Completo: ")
        print("Carrera: ")

def Salir():
    decision = input("¿Deseas terminar el procedimiento? (s/n): ")

    if decision.lower() == "s":
        print("Terminando el procedimiento...")
        
    elif decision.lower() == "n":
        print("Regresando al menú principal...")
        
    else:
        print("Opcion no valida. Por favor, ingresa 's' para terminar o 'n' para regresar al menú principal.")
    

print("Menu \n")
print("\n 1) Grabar")
print("2) Buscar") 
print("3) Imprimir certificados") 
print("4) Salir")
opc = int(input(print("Opcion:  ")))

if opc == 1 :
    grabar
elif opc == 2:
    buscar
elif opc == 3:
    imprimir_certificados()
elif opc == 4:
    Salir() 
else:
    print("La opcion indicada no es valida")
