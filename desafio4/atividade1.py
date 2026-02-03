soma = 0

numero = int(input("Digite um número de 0 a 20: "))
while numero != 0:
    soma += numero
    numero = int(input("Digite um número de 0 a 20: "))
print(f"A soma dos números digitados é: {soma}")