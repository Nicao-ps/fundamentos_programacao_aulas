# Faça um programa aonde o cliente irá escolher
# o sabor de pizza e o sistema irá exibir o valor.
print('''
    =======================================
    🍕 Bem vindo a Pizzaria SABORES:
        1 - Mussarela (R$ 30,00)
        2 - Calabresa (R$ 35,00)
        3 - Frango com Catupiry (R$ 40,00)
    =======================================
''')

opcao = int(input('Digite o numero do sabor desejado: '))
if opcao == 1:
    print('Você escolheu a pizza de Mussarela. O valor é R$ 30,00')
elif opcao == 2:
    print('Você escolheu a pizza de Calabresa. O valor é R$ 35,00')
elif opcao == 3:
    print('Você escolheu a pizza de Frango com Catupiry. O valor é R$ 40,00')
else:
    print('Opção inválida. Por favor, escolha uma opção entre 1 e 3.')
