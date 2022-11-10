# 'Python'
print('usando um iterável')
texto1 = ''
vogais1 = 'AEIOU'
for letra in texto1:
    if letra.upper() in vogais1:
        print(letra, end='')
    else:
        print() #adiciona uma quebra de linha

# letra = P
# letra = y
# letra = t
# letra = h
# letra = o
# letra = n
#um elemento previamente conhecido com estrutura iterável, o for é mais indicado.
#texto = input('Digite um nome: ')
texto = ""
vogais = 'AEIOU'
print(f'Iterando item por item de {texto}, fica: ')
for c in texto:
    print(c + '|', end='')
print() #quebra de linha

#For tem mais uma instrução o for..else
print()
print('Usando o for..else')
texto = ''
vogais = 'AEIOU'
#print(f'Iterando item por item de {texto}, fica: ')
for c in texto:
    print(c + '|', end='')

else:
    print() #quebra de linha / identação diferente
    print('Executando no final do laço, após a quebra de linha')
# função range

print('usando função built in range com for')
for numero in range(4):
    print(numero, sep='\n')

for numero2 in range(5):
    print(numero2, end=' \n')

for numero3 in range(6):
    print(numero3, end='\n')

print('usando range para exibir a tabuada do 5,\nlembrando que a contagem é de 5 em 5')
for numero4 in range(0,51,5):
    print(numero4)

print('Executando até que algo aconteça, sem valor de vezes que o bloco deve ser executado, use while')

opcao = -1
while opcao != 0:
    opcao = int(input('[1] sacar \n[2] Extrato \n[0] Sair do menu \n'))

    if opcao == 1:
        print('Saque sendo efetuado')
    elif opcao == 2:
        print('Exibindo extrato...')
    else:
        print('Fim da execução')
else:
    print('Obrigado por usar nossos serviços!\n')

    #usando o BREAK
    print('Usando o BREAK\n')

    opcao = -1
while opcao != 0:
    opcao = int(input('Informe um valor: \n'))

    if opcao == 10:
        print('Obrigado por usar nossos serviços')
        break
    print(opcao)

print()

print('Outra forma de fazer')

while 1 == 1:
    numero5 = int(input('Informe um valor: \n'))

    if numero5 == 10:
        print('Obrigado por usar nossos serviços')
        break
    print(numero5)

print()

print('fazendo a parada da execução usando o laço for\n')

for numero5 in range(100):
    # if numero5 == 10:
    #     break
    print(numero5, end=' ')

print()

print('Usando o continue, com encerramento ao escolher 10, vai suprimir o valor 12 da faixa de 0 a 20')
# while 1 == 1:
# numero6 = int(input('Informe um valor: \n'))

    # if numero6 == 10:
    #     print('Obrigado por usar nossos serviços')
    #     break
    # print(numero6)

print()

print('fazendo a parada da execução usando o laço for\n')

for numero6 in range(20):
    if numero6 == 12:
        continue
    print(numero6, end=' ')

print()

print('Programa para exibir apenas os números ímpares\n')

for numero6 in range(20):
    if numero6 % 2 == 0:
        continue
    print(numero6, end=' ')

print()
print('Usando continue dentro do while')
while True:
    numero7 = int(input('Informe um valor: \n'))
    
    if numero7 == 10:
        print('Obrigado por usar nossos serviços')
        break

    if numero7 % 2 == 0:
        continue
    
    
    
    print(numero7)
