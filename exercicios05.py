# Questão 3 – Par ou Ímpar

# Crie um programa em Python que peça ao usuário um número inteiro.

# Se o número for par, mostre: "O número é par."

# Caso contrário, mostre: "O número é ímpar."

n1= int(input('Digite um número : '))

if n1 % 2 == 0 : 
    print('Esse número é par ')
else :
    print('Esse número é ímpar')