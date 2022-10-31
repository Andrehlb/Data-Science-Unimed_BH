# 'Python'

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
