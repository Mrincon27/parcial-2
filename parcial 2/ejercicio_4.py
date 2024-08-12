def promedio():
    numeros_conjunto = [None] * 5
    i = 0
    sum  = 0
    while i < 5:
        try:
            numeros_conjunto[i] = float(input("Dijite un numero por favor: "))
            sum = sum + numeros_conjunto[i]
            i += 1
        except ValueError:
            print("El valor ingresado no es un número real. Intente de nuevo.")

    print(f"El conjunto de numeros es:{numeros_conjunto}")

    promedio_numeros = sum / 8 

    print(f"El promedio es:{promedio_numeros}")