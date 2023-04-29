
lista = [1,2,3,4,3]


def boomerang(lista):
    if len(lista)<3:
        print("El tmaño de l alista es muy corto para analizarlo")
    if len(lista) >= 3:
        contador = 0
        
        for i in range(len(lista)-2):
            if lista[i] == lista[i+2] and lista[i] != lista[i+1]:
                contador += 1
           
        print(contador, "Boomerangs")

boomerang(lista)