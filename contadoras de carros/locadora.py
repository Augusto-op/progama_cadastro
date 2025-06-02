def mostrar_linha():

    print('-' * 50)

# Exemplo de uso da funcao mostrar_linha
mostrar_linha()

print("Aluguel de Carro com a maior frota do Brasil | Localiza")

mostrar_linha()

nome = input('Digite seu nome:')
print(f'Ola,{nome}! Estamos felizes em te-lo conosco.')

mostrar_linha()

carro = input('Digite qual carro deseja alugar: (1-BMW | 2-Mustang | 3-HB20 | 4-Fusca | 5-Civic | 0-sair):')
mostrar_linha()
if carro == 'BMW':
    print(f'Sr(a). {nome}, voce escolheu um otimo carro! da marca {carro}')
elif carro == 'Mustang':
    print(f'Sr(a).{nome} voce escolheu um belo carro para sair e tirar aquela onda com seu {carro} ')
elif carro == 'HB20':
    print(f'Ola Sr(a). {nome}, Voce escolheu um belo carro! Da marca {carro}')
elif carro == 'Fusca':
    print(f'otima escolha de carro Sr(a). {nome}, um exelente {carro}!')
elif carro == 'Civic':
    print(f'Boa escolha do seu {carro}! Sr(a).{nome}')
else:
    print(f'Que pena que voce nao escolheu, mas tenha um otimo')