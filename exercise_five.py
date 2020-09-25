#Crie um programa em Python que sirva como calculadora através dos inputs do usuário.
#A calculadora precisará solicitar ao usuário o primeiro número, a operação (soma, subtração, multiplicação, divisão, resto divisão),
#e na sequência solicitar o segundo número. Por fim, o programa deverá printar a operação matemática realizada e o resultado.

#A descrição da pergunta se contradizia da descrição da prova que era pra colocar os valores em tempo de execucao sem pedir para o usuario
number_1 = int(input('Insira o primeiro numero: '))
operation = input('''
    Insira uma operação para continuar
    + para soma
    - para subtracao
    * para multiplicação
    / para divisaão
    / para resto
    ''')
number_2 = int(input('Insira o segundo numero:'))


# Soma
if operation == '+':
    print(f'Soma: {number_1} + {number_2} =  {number_1 + number_2}')

# Subtracao
elif operation == '-':
    print(f'Subtracao: {number_1} - {number_2} = {number_1 - number_2}')

# Multiplicação
elif operation == '*':
    print(f'Multiplicação: {number_1} * {number_2} = {number_1 * number_2}')


# Divisão

elif operation == '/':
    print(f'Divisão: {number_1} / {number_2} = {number_1 / number_2}')

# Resto
elif operation == '%':
    print(f'Resto: {number_1} % {number_2} = {number_1 % number_2}')

else:
    print('Selecione uma operacao valida')
