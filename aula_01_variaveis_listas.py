print('hello world!!!')

saudacao = 'hello world!!!'
print(saudacao)
print(type(saudacao)) 
#---type mostra o tipo de variável que estou usando (no caso saudação)---
palavra_1 = 'maria'
palavra_2 = 'joao'
saudacao = palavra_1 + palavra_2 
#---a soma de strings se chama concatenação---
print(saudacao)

a = 2
b = 3
#print (f"A operação {a} + {b} resulta em {a+b}")
# "f" indica que tudo que esta entre chaves o programa sabe que é uma variável e não um caracter
# --- operadores aritméticos -, +, /, *, ** ---
print (f"A operação {a} - {b} resulta em {a-b}")
print (f"A operação {a} * {b} resulta em {a*b}")
print (f"A operação {a} / {b} resulta em {a/b}")
print (f"A operação {a} ** {b} resulta em {a**b}")

#---input = passa uma orientação a respeito do que o usuário deve fazer
#---input está associado a uma variável, diferente de print
nome = input("Diga seu nome: ")
idade = input("Diga sua idade: ")
print(f"Olá, {nome}! Você tem {idade} anos!")

# curiosidade: a letra f é f de formatação de strings

a=input("Diga um número: ")
b=input("Diga outro número: ")
print (f"A operação {a} + {b} resulta em {a+b}")
# resultado dessa operação foi 58, pois eu não contei que as variáveis a e b eram numeros

a=int(input("Diga um número: "))
b=int(input("Diga outro número: "))
print (f"A operação {a} + {b} resulta em {a+b}")
#agora sim, ao colocar int antes do input o python transforma em inteiro

#Calculadora
a=int(input("Diga um número: "))
b=int(input("Diga outro número: "))
print (f"A operação {a} + {b} resulta em {a+b}")
print (f"A operação {a} - {b} resulta em {a-b}")
print (f"A operação {a} * {b} resulta em {a*b}")
print (f"A operação {a} / {b} resulta em {a/b}")
print (f"A operação {a} ** {b} resulta em {a**b}")

#Operadores booleanos
a = 2
b = 3

print (f"{a} > {b} dá {a>b}")
print (f"{a} < {b} dá {a<b}")
print (f"{a} >= {b} dá {a>=b}")
print (f"{a} <= {b} dá {a<=b}")
print (f"{a} == {b} dá {a==b}")
print (f"{a} != {b} dá {a!=b}")

#Condicionais

idade = int(input('Diga a sua idade: '))
if idade < 18:
    print('Você não pode comprar bebidas alcoolicas!')
else:
    print('Você pode comprar bebidas alcoolicas!')

# Operadores booleanos and e or
# um operador boleano significa ser true or false
# exercício: Você so pode estacionar na vaga especial se for idoso ou deficient
# OR
# true or false = true (é idoso mas não é deficiente = pode estacioar)
# false or true = true (não é idoso mas é deficiente = pode estacionar)
# true or true = true (é idoso e é deficiente = pode estacionar)
# false or false = false (não é idoso e não é deficiente = não pode estacionar)

idoso = input('Você é idoso? (sim/não): ')
deficiente = input('Você é deficiente? (sim/não): ')
if idoso == 'sim' or deficiente == 'sim':
    print('Pode estacionar!')
else:
    print('Procure outra vaga!')

# AND:
# true or false = false (ser idoso mas não ter cartão de idoso = não pode estacionar)
# false or true = false (não ser idoso mas ter cartão de idoso = não pode estacionar)
# true or true = true (ser idoso e ter cartão de idoso = pode estacionar)
# false or false = false (não é idoso e não tem cartão = não pode estacionar)

idoso = input('Você é idoso? (sim/não): ')
cartao = input('Você tem cartão? (sim/não): ')
if idoso == 'sim' and cartao == 'sim':
    print('Pode estacionar!')
else:
    print('Procure outra vaga!')

letra = input('Digite uma letra: ')
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('Você digitou uma vogal!')
else:
    print('Não é uma vogal!')
