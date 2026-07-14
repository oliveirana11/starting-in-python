# for
# len quantidade de coisas dentro de uma lista
# for variavel in conjunto - print (variavel) --> no for a variavel assume todas as coisas dentro do conjunto

professores = ['Danilo', 'Gabi', 'Acelote', 'Toniho', 'Leninha']
disciplinas = ['python', 'historia', 'matemática', 'quimica', 'biologia','portugues']
print(len(professores))
print(len(disciplinas))

print('Os professores são: ')
for nome in professores:
    print(nome)
print('As matérias que ensinam são: ')
for materia in disciplinas:
    print(materia)

# Fizemos for por elementos, mas gostariamos de mostrar na tela
# o professor x materia. Para isso precisamos parear elemento por posição
# o for nao ser mais por elemento

# ​A função *range* gera uma sequência de números, 
# e o *i* assume o valor de cada um deles a cada volta

for i in range(len(professores)):
   print(f'professores[{i}] = {professores[i]}')

for i in range(len(professores)):
    print(f'O/A professor/a {professores[i]} ensina {disciplinas[i]}')

import pandas as pd
professores = ['Danilo', 'Gabi', 'Acelote', 'Toniho', 'Leninha', 'leo']
disciplinas = ['python', 'historia', 'matemática', 'quimica', 'biologia','portugues']
dados={
    'profs' : professores,
    'materias' : disciplinas
}
print(pd.DataFrame(dados))

import pandas as pd
carros ={
    'modelo':['uno','gol','polo','kombi'],
    'preço':[20000, 30000, 60000, 15000],
    'marca':['fiat', 'vw', 'vw','vw'],
    'fabricação':[2005,2015,2023,1975]
}
df = pd.DataFrame(carros)
print(df)
df.to_excel('carros.xlsx')
