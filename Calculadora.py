print("Bienvenido a la calculadora")
print("Elije que deseas hacer")

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
Error = ("No se puede dividir entre 0")

Opcion = int(input("Elije que opcion quieres "))

Num1 = float (input("Elije tu primer numero "))
Num2 = float (input ("Elije tu segundo numero "))

if Opcion == 1:
    print(Num1 + Num2)
elif Opcion == 2:
    print(Num1 - Num2)
elif Opcion == 3:
    print(Num1 * Num2)
elif Opcion == 4:
    if Num2 == 0:
        print("Error, no se puede dividir entre 0")
    else:
        print(Num1 / Num2)
else:
    print("Opción inválida")


