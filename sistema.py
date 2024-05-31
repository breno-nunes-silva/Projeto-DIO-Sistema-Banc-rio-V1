menu = '''\n[----------------------------------]

Por favor, escolha o processo a ser realizado.

[d] Realizar depósito
[s] Realizar saque
[e] Emitir extrato
[q] Sair do sistema

[----------------------------------]

--->  '''

saldo = 0
lim = 500
lim_saques = 3
num_saques = 0
saq = []
depósitos = []

while True:
    processo = input(menu).lower()

    if processo == 's': #Processo de saque
        if num_saques < lim_saques:
            valor = float(input('Insira o valor do saque|  '))
            while valor <= 0 or valor > lim:
                valor = float(input('\nInsira um valor de saque maior que R$0,00 e menor ou igual a R$500,00\nInsira o valor do saque|  '))
            if valor <= saldo:
                saldo -= valor
                num_saques += 1
                saq.append(valor)
                print(f'Saque realizado com sucesso!\nR${valor:.2f} foram sacados da sua conta.')
            else:
                print('Valor de saque maior do que o saldo disponível.\nImpossível de realizar o processo.')
        else:
           print('Limite de saques diário atingido.')

    if processo == 'd': #Processo de depósito
        valor = float(input('Insira o valor do depósito|  '))
        while valor < 0:
            valor = float(input('\nInsira um valor de depósito positivo.\nInsira o valor do depósito|  '))
        saldo += valor
        depósitos.append(valor)
        print(f'Depósito realizado com sucesso!\nR${valor:.2f} foram depositados na sua conta.')

    if processo == 'e': #Processo de extrato
        print('[----------------------------------]\n\nDepósitos realizados:')
        for dps in depósitos:
           print(f'R${dps:.2f} depositados.') #
        
        print('\nSaques realizados:')
       
        for sq in saq:
            print(f'R${sq:.2f} sacados.')
        print(f'\nSaldo final: R${saldo:.2f}')

    if processo == 'q':
        break
