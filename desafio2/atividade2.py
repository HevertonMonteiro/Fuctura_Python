valor = float(input("Digite o valor da compra (R$): "))

print("\nForma de pagamento:")
print("1 - À vista (10% de desconto)")
print("2 - Cartão (preço normal)")
print("3 - Parcelado (10% de acréscimo)")

opcao = int(input("Escolha a forma de pagamento (1, 2 ou 3): "))

if opcao == 1:
    valor_final = valor - (valor * 0.10)
    print(f"Valor final com desconto: R$ {valor_final:.2f}")

elif opcao == 2:
    valor_final = valor
    print(f"Valor final: R$ {valor_final:.2f}")

elif opcao == 3:
    valor_final = valor + (valor * 0.10)
    print(f"Valor final com acréscimo: R$ {valor_final:.2f}")

else:
    print("Opção inválida!")
