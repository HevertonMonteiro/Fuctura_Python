cadastro = {
    'nome': input("Digite seu nome: "),
    'altura': float(input("Digite sua altura: ")),
    'peso': float(input("Digite seu peso: "))
}
cadastro ['data_de_nascimento'] = '1999-11-24'
if 'peso' in cadastro:
    cadastro.update({'peso': 80.0})
if 'altura' in cadastro:
    cadastro.pop('altura')

print("\nCadastro:")
for chave, valor in cadastro.items():
    print(f"{chave}: {valor}")