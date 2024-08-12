def medianaArreglo(x): #Arreglos
    conjunto=[1,3,5,9,15,16] #conjunto de numeros
    x=conjunto
    if len(x)%2 != 0:
        operacionIndex = (len(x)-1)/2
        mediana = x[int(operacionIndex)]
    else:
        valorALaIzquierda = x[int((len(x)-2)/2)]
        valorALaDerecha = x[int(len((x))/2)]
        mediana = (valorALaIzquierda+valorALaDerecha)/2
    print(f"la media de los numeros es{mediana}")