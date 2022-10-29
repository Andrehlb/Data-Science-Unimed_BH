# 'Python'

# letra = P
# letra = y
# letra = t
# letra = h
# letra = o
# letra = n

texto = input('Digite um nome: ')

vogais = 'AEIOU'
print(f'Iterando item por item de {texto}, fica: ')
for c in texto:
    print(c + '|', end='')
print() #quebra de linha

#For tem mais uma instrução o for..else