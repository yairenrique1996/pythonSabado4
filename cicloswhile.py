observador=10
print("**MENU**")
print("0.SALIR")
print("1.PYTHON")
print("2.C#")

while(observador != 0 ):
    observador = int(input("digite una opcion: "))
    if(observador == 0):
        break

    elif(observador == 1):
        print("El lenguaje de programación Python es ampliamente utilizado por empresas de todo el mundo para construir aplicaciones web")

    elif(observador == 2):
        print("C# es un lenguaje de programación orientado a componentes, orientado a objetos. C# proporciona construcciones de lenguaje para admitir directamente")    


    else:
        print("digite una opcion valida")    
     