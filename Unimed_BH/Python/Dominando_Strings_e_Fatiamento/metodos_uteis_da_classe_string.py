nome = 'aNdRé lUiZ'

print(nome.upper()) #tudo maiúsculo
print(nome.lower()) #t. minúsculo
print(nome.title()) #primeira letra em maiúsculo

texto = '  Hello World!    ' #início 2 e fim com 4 espaços

print('|' + texto.strip() + '|') #retira todos os espaços
print('|' + texto.rstrip() + '|') #r. espaços da direita
print('|' + texto.lstrip() + '|') #r. espaços da esquerda

#junção e centralização
print('Junção e centralização')
print()
print('###'+ nome +'###')
print(nome.center(16))
print(nome.center(16, '|'))
print()
#método Join
print('Método Join')
print('-'.join(nome))

print()
print('Usando iteração com for para adicionar "-"')
for letra in nome:
    print(letra, end='-')