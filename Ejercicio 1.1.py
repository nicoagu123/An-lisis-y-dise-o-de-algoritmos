
n = int(input("Ingrese un número: "))
if n % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
    
    
ultimo_digito = abs(n) % 10
print(f"El último dígito de {n} es: {ultimo_digito}")


a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))
if a >= b:
    print(f"El mayor entre {a} y {b} es: {a}")
if a < b:
    print(f"El mayor entre {a} y {b} es: {b}")

else:
    print(f"Los números {a} y {b} son iguales")





