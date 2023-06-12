opcion = 0

while opcion != 5:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        a = int(input("Introduce un numero: "))
        b = int(input("Introduce otro numero: "))
        print("La suma es:", a + b)

    elif opcion == 2:
        a = int(input("Introduce un numero: "))
        b = int(input("Introduce otro numero: "))
        print("La resta es:", a - b)
    
    elif opcion == 3:
        a = int(input("Introduce un numero: "))
        b = int(input("Introduce otro numero: "))
        print("La multiplicacion es:", a * b)
    
    elif opcion == 4:
        a = float(input("Introduce un numero: "))
        b = float(input("Introduce otro numero: "))
        print("La division es:", a / b)
    
    else:
        print("Hasta pronto")
