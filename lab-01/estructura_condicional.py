# Programa para verificar si un número es par o impar
numero_str = input("Ingrese un número: ")

if numero_str.isdigit():
    numero = int(numero_str)
    if numero % 2 == 0:
        print("===> El número es par")
    else:
        print("===> El número es impar")
else:
    print("===> Error: Ingrese un número válido")
