    # While
idoso = input('Você é idoso?\n(sim/não): ')
while idoso.lower() != 'sim' and idoso.lower() != 'não': 
    #.lower transforma o que o usuário digitou em minúsculo
    print("Você deve digitar sim ou não!!")
    idoso = input('Você é idoso?\n(sim/não): ')

cartao = input("Você tem cartão\n(sim/não): ")
while cartao.lower() != 'sim' and cartao.lower() != 'não':
    print("Você deve digitar sim ou não!!")
    cartao = input('Você tem cartão\n(sim/não): ')

if idoso == 'sim' and cartao == 'sim':
    print('Pode estacionar!')
else:
    print('Procure outra vaga!')

letra = input('Digite uma letra: ')
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('Você digitou uma vogal!')
else:
    print('Não é uma vogal!')

vogais = ['a', 'e', 'i', 'o', 'u']
letra = input('Digite uma letra: ')
if letra in vogais:
    print(f'{letra} é uma vogal')
else:
    print(f'{letra} não é uma vogal')

estado_civil = input('VocÊ é solteiro/a(s),casado/a(c), divorciado/a(d), viúvo/a(v)\n: ')
while estado_civil not in ['s', 'c', 'v', 'd']:
    print('Erro!')
    estado_civil = input('VocÊ é solteiro/a(s),casado/a(c), divorciado/a(d), viúvo/a(v)\n: ')
