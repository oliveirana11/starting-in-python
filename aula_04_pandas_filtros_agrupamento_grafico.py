#banco de dados relacional - planilha
modelo=['uno', 'ka', 'gol', 'hb20']
preco=[100, 200, 300, 400]
print(f"o carro {modelo[0]} tem preço {preco [0]}")
#outro jeito
for i in range (len(modelo)): #quantidade de elementos na lista modelo (4)
    print(f"o carro {modelo[0]} tem preço {preco [0]}")
for i in range(4):
    print(i)
print()
for i in range (len(modelo)):
    print(f"o carro {modelo[0]} tem preço {preco [0]}")

modelo=['uno', 'ka', 'gol', 'hb20']
preco=[100, 200, 300, 400]
escolha = input("Diga o modelo do carro: ")
for i in range (len(modelo)):
    if modelo[i] == escolha:
        print(f"O carro {escolha} tem preço {preco [i]}")
    else:
        print ("O carro escolhido não está em nosso banco de dados!")

carros = {'modelo':['uno', 'ka', 'gol', 'hb20'],
    'preco':[100, 200, 300, 400],
    'cor':['branco', 'preto', 'branco', 'azul'],
    'potencia':[100, 120, 130, 200],
    'ano':[1990, 2010, 2000, 2020]
    }
import pandas as pd
carros = pd.DataFrame(carros)
carros.to_excel('C:/Users/anaka/OneDrive/Área de Trabalho/carros.xlsx')


import pandas as pd
dados = pd.read_excel('C:/Users/anaka/OneDrive/Área de Trabalho/carros_aula.xlsx')
print(dados)

preco_medio=dados['preco'].mean()
print(f"O preço médio dos carros é R${preco_medio}")

valores = dados['preco']>100000
print(dados[valores])

marca=dados['marca']=='Chevrolet'
print(dados[marca])

for marca in dados['marca'].unique():
    carros_marca=dados[dados['marca']==marca]
    preco_medio=dados['preco'].mean()
    print(f'O preço medio dos carros da marca {marca} é R$ {preco_medio}')

import pandas as pd
import matplotlib.pyplot as plt
dados = pd.read_excel('C:/Users/anaka/OneDrive/Área de Trabalho/carros_aula.xlsx')
dados = pd.DataFrame(dados)
dados['ano'].value_counts().plot.pie()
plt.show()
