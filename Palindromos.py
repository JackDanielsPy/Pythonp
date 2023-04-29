"""
Enunciado: Escribe una función que recibe un texto y devuelve verdadero o falso (Boolean) según sean o no palíndromos.
* Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
* NO se tienen en cuenta los espacios, signos de puntuación y tildes.
* Ejemplo: Ana lleva al oso la avellana
"""
#frase = "Ana lleva al oso la avellana"
#frase = "Que te ha parecido el reto"
frase = "Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida "
a,b = "aeiou", "áéíóú" 
trans = str.maketrans(b,a)
# Intercambio vocales con acento por vocales sin acento

def palindromo(frase):
    f = frase.lower()
    frasemis = f.replace(" ", "")
    frasemid = frasemis.replace(",","")
    frased = "".join(frasemid)
    print(frased.translate(trans))
    frase1 = frased[::-1]
    frase2 = frase1.lower()
    print(frase2.translate(trans))      
    if frased.translate(trans) == frase2.translate(trans):
        print("Si es un palindromo")            
    else:
        print("No es un palindromo")
       
palindromo(frase)