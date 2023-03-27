
precos = {
    'regular': {
        (0, 100): 1.5,
        (100, 500): 2.5,
        (500, float('inf')): 3.5
    },
    'expresso': {
        (0, 100): 3,
        (100, 500): 5,
        (500, float('inf')): 7
    },
    'agendado': {
        (0, 100): 2,
        (100, 500): 4,
        (500, float('inf')): 6
    }
}

desconto_remesa_grande = 0.1 
desconto_remesa_curta = 0.05  

print('Bem-vindo à calculadora de custos de envio!')
print('------------------------------------------')

peso = float(input('Digite o peso da mercadoria em quilogramas: '))
distancia = float(input('Digite a distância a ser percorrida em quilômetros: '))

print('\nTipos de envio disponíveis:')
print(' 1 - Regular')
print(' 2 - Expresso')
print(' 3 - Agendado')
tipo_envio = int(input('Escolha o tipo de envio: '))

preco_por_quilo = precos['regular'][(0, 100)] if peso < 100 else \
                  precos['regular'][(100, 500)] if peso < 500 else \
                  precos['regular'][(500, float('inf'))]


preco_por_km = precos['regular'][(0, 100)] if distancia < 100 else \
               precos['regular'][(100, 500)] if distancia < 500 else \
               precos['regular'][(500, float('inf'))]


custo = peso * preco_por_quilo * distancia * preco_por_km * precos['regular'][(0, float('inf'))]


if peso >= 1000:
    custo *= 1 - desconto_remesa_grande
if distancia < 50:
    custo *= 1 - desconto_remesa_curta

print('\nCálculo de custos:')
print(f'Peso da mercadoria: {peso} kg')
print(f'Distância a percorrer: {distancia} km')
print(f'Tipo de envio escolhido: {list(precos.keys())[tipo_envio-1]}')
print(f'Preço por quilo: R${preco_por_quilo:.2f}')
print(f'Preço por quilômetro: R${preco_por_km:.2f}')
print(f'Custo total de envio: R${custo:.2f}')
