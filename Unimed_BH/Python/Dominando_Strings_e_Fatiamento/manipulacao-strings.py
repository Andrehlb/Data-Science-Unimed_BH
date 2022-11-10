nome = 'André Luiz'
idade = 50
profissão = 'Biólogo e coder'
linguagem = 'Python'
saldo = 45.345
print('Nome:  %s, Idade:  %s' % (nome, idade), 'Nome é tipo: ', type(nome), 'Idade é tipo: ', type(idade))
print('Nome:  %s, Idade:  %f' % (nome, idade), 'Nome é tipo: ', type(nome), 'Idade é tipo: ', type(idade))
print('Nome:  %s, Idade:  %d' % (nome, idade), 'Nome é tipo: ', type(nome), 'Idade é tipo: ', type(idade))

print()
print('Método Format')
print('Nome: {}, Idade: {}'.format(nome, idade), 'nome é tipo: ', type(nome), 'Idade é tipo: ', type(idade))
print('Nome: {}, Idade: {}'.format(idade, nome), 'nome é tipo: ', type(nome), 'Idade é tipo: ', type(idade))
print('Nome: {1}, Idade: {0}'.format(idade, nome), 'nome é tipo: ', type(nome), 'Idade é tipo: ', type(idade))
print('Nome: {1}, Idade: {0}, Nome: {1} {1} {1} {1}'.format(idade, nome), '\nnome é tipo: ', type(nome), 'Idade é tipo: ', type(idade))
print('Nome: {nome}, Idade: {idade}'.format(nome=nome, idade=idade), '\nnome é tipo: ', type(nome), 'Idade é tipo: ', type(idade))
print('Nome: {name}, Idade: {age}'.format(age=idade, name=nome), '\nnome é tipo: ', type(nome), 'Idade é tipo: ', type(idade))
print('Nome: {name}, Idade: {age} {name} {name} {age}'.format(age=idade, name=nome), '\nnome é tipo: ', type(nome), 'Idade é tipo: ', type(idade))

print()
print('Usando um dicionário para o Método Format')

dados = {'nome2':'André Luiz Barbosa', 'idade2': 50}
print('Nome: {nome2}, Idade: {idade2}'.format(**dados), '\nnome é tipo: ', type(nome), 'Idade é tipo: ', type(idade))

print()
print('Usando o método f e inserindo a variável saldo')
print(f'Nome: {nome}, Idade: {idade}, Saldo: {saldo}')
print(f'Nome: {nome}, Idade: {idade}, Saldo: {saldo:10.2f}')
print(f'Nome: {nome}, Idade: {idade}, Saldo: {saldo:.2f}')

