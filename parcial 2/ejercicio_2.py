def contiene_vocales(X):
    vocales=["a","e","i","o","u"]
    for i in range(len(X)-1):
        vocal=0
        for j in range(i+1,len(X)):
            vocal = vocales and (X[i][j]==X[j][i])
    return vocal
