
marca = input("Digite a marca do carro: ")
cor = input("Digite a cor do carro: ")
ano = int(input("Digite o ano do carro: "))


valor_compra = float(input("Digite o valor de compra do carro (R$): "))
anos = int(input("Em quantos anos pretende vender o veículo? "))


taxa_desvalorizacao = 0.10
valor_atual = valor_compra

for i in range(anos):
    valor_atual -= valor_atual * taxa_desvalorizacao


km_viagem = float(input("Quantos km terá a viagem? "))
consumo = float(input("Qual a média de consumo do veículo (km/l)? "))


litros_gastos = km_viagem / consumo


preco_gasolina = 6.50
custo_total = litros_gastos * preco_gasolina


print("\n--- RESUMO DO VEÍCULO ---")
print(f"Marca: {marca}")
print(f"Cor: {cor}")
print(f"Ano: {ano}")

print("\n--- DESVALORIZAÇÃO ---")
print(f"Valor estimado do carro após {anos} anos: R$ {valor_atual:.2f}")

print("\n--- VIAGEM ---")
print(f"Litros gastos na viagem: {litros_gastos:.2f} L")
print(f"Custo total da viagem: R$ {custo_total:.2f}")
