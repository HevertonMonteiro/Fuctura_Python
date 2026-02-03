numeros_inteiros = []

for numeros in range(5):
    numero = int(input("Digite 1 número inteiros "))
    numeros_inteiros.append(numero)
print("\nNúmeros digitados:", numeros_inteiros)

print("\nNúmeros pares digitados:")
for numeri in numeros_inteiros:
    if numeri % 2 == 0:
        print(numeri)

print("\nNumeros impares digitados:")
for numeral in numeros_inteiros:
    if numeral % 2 != 0:
        print(numeral)

print("\nSoma total:")
for total in numeros_inteiros:
    total = sum(numeros_inteiros)
print(total)