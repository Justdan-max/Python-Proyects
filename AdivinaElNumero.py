import random
secreto = random.randint(1, 10)

print ("Bienvenidos a Adivina el numero")
print ("Elije un numero del 1 - 10")

Num = int(input("Elije el numero "))

print ("El numero es...")

while Num != secreto:
    print("Ese no es el número. Intenta de nuevo.")
    Num = int(input("Elije otro número: "))
    if Num > secreto:
        print ("Este numero es muy alto. Intenta de nuevo")
    else:
        print ("Este numero es muy bajo. Intenta de nuevo")

print("¡Correcto! El número era", secreto)
