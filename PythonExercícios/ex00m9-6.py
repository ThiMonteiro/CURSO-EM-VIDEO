# resposta do curso
n = str(input('Escreva o seu nome completo: ')).strip()
print('Muito prazer em te conhecer!!')
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

