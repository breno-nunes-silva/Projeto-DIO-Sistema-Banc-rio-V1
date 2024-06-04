
lim = 500
lim_saques = 3 
saldos_num_saqs = [] # casa usuário tem uma lista que indica seu saldo e quantidade de saques
saq_users = [] # cada usuário tem uma lista que indica todos os seus saques
dep_users = [] # cada usuário também tem uma lista que indica todos os seus depósitos
users = [] # contém as informações dos usuários, em um dicionário onde o cpf é a chave e o valor são as outros informações dele [nome, data de nascimento, endereço]
contas = [] # contém as informações das contas correntes. Cada lista dentro desta possui um dicionário de chave número da conta e valor cpf do dono e o número da agencia que é fixo '0001'
# Tenha em mente que nas listas de contas, saques, depósitos, saldo e num_saques, o número da conta subtraido de 1 sempre levará as suas respectivas listas


#
# OUTRAS FUNÇÕES
#


def find_key(dicto, valor): # encontra uma chave com base em um valor previamente conhecido do dicionário.
    for a in dicto:
        if dicto[a] == valor:
            return a


def converter(num): # recebe uma string contendo números e outros caracteres, retorna uma string apenas com números.
    n = []
    for numero in str(num):
        if numero.isnumeric() == True:
            n.append(numero)
    return ''.join(n)



def listar_users(users): # lista os usuários presentes em users
    for indx in users:
        for key in indx:
            name = indx[key][0]
            date = indx[key][1]
            adress = indx[key][2]
            cpf  = find_key(indx,indx[key])
            print(f'CPF: {cpf} e Informações do Usuário| Nome: {name} : Data de nascimento: {date} : Endereço: {adress}')



def listar_contas(contas): #lista as contas presentes em contas
    for conta in contas:
        numero_da_conta = contas.index(conta)+1
        dono_da_conta = conta[0][numero_da_conta]
        agencia = conta[1]
        print(f'Conta: {numero_da_conta} | CPF dono: {dono_da_conta} | Agência: {agencia}')

#
# CADASTRO E CRIAÇÃO DE CONTA
#
    
def cadastrar_user(users):
    # padrão = {cpf: [nome, data de nascimento, endereço]}

    nome=input('\nInsira seu nome|  ') #'William Bonner'
    data=input('Insira sua data de nascimento por extenso|  ') #'14 de outubro de 2008'
    cpf= input('Insira seu CPF|  ') #'187.550.577-64'
    endereço= input('logradouro - número - bairro - cidade/sigla_do_estado\nInsira seu endereço seguindo o padrão descrito acima|  ') #'ieebdjd - 87 - jddbdd - pppp/MN'

    n_cpf = converter(cpf)

    if n_cpf in users:
        print('\nOperação falhou! Já há um usuário com este cpf.')
    else:
        users.append({n_cpf:[nome, data, endereço]})


        
def cadastrar_conta(users, contas): #agência fixa 0001 # contas devem ser contadas de 1 em 1
    cpf =input('\nInsira o CPF do usuário que abrirá a conta|  ')

    n_cpf = converter(cpf)
    valido = False

    for usuario in users:
        if n_cpf in usuario.keys():
            valido = True

    if valido == False:    
        print('Operação falhou! Insira um CPF válido da lista de usuários')

    else:
        contas.append( [{len(contas)+1:n_cpf}  , '0001'] )
        saq_users.append([])
        dep_users.append([]) #todas as listas tem índice igual ao número da conta -1
        saldos_num_saqs.append([0.0 , 0]) # O primeiro num é o saldo e o segundo é a quantia de saques feitos

#
# OPERAÇÕES DE USUÁRIO
#

def emitir_extrato(saq,dep):
    print(f'[----------------------------------]\n\nSAQUES REALIZADOS\n')
    for s in saq:
        print(f'R${s:.2f}')
    print(f'[----------------------------------]\n\nDEPÓSITOS REALIZADOS\n')
    for d in dep:
        print(f'R${d:.2f}')



def saque(*, saldos_num_saqs, lim, lim_saques,emitir_extrato,conta,saq_users,dep_users): #Criar funcionalidade no menu de caso não hajam contas ser impossivel de realizar operações
    if saldos_num_saqs[conta][1] < lim_saques:
        valor = float(input('Insira o valor do saque|  '))

        while valor <= 0 or valor > lim:
            valor = float(input('\nInsira um valor de saque maior que R$0,00 e menor ou igual a R$500,00\nInsira o valor do saque|  ')) 

        if saldos_num_saqs[conta][0] < valor:
            print(f'Operação falhou! Saldo insuficiente. [Saldo atual: R${saldos_num_saqs[conta][0]:.2f}]')    

        else:
            saldos_num_saqs[conta][0] -= valor
            saldos_num_saqs[conta][1] += 1
            saq_users[conta].append(valor)
            emitir_extrato(saq_users[conta],dep_users[conta])
    else:
        print('Operação falhou" Limite de saques atingido.')



def deposito(saldos_num_saqs, emitir_extrato,dep_users, saq_users,conta,/):
    valor = float(input('Insira o valor do depósito|  '))

    while valor <= 0:
        valor = float(input('Valor inválido!\nInsira um valor de depósito acima de R$0.00|  '))

    saldos_num_saqs[conta][0] += valor
    dep_users[conta].append(valor)
    emitir_extrato(saq_users[conta],dep_users[conta])

#
#
# SISTEMA DE MENU / ACESSO A CONTA
#
#

menu_log = '''\nEscolha uma opção do menu.

[----------------------------------]

[sign] Cadastrar usuário.
[current] Cadastrar conta-corrente.

[enter] Acessar menu de processos.

[users] Listar usuários.
[accounts] Listar contas-correntes.

[out] Sair do sistema.

[----------------------------------]

--->  '''
menu_processos = '''
[----------------------------------]

Por favor, escolha o processo a ser realizado.

[d] Realizar depósito.
[s] Realizar saque.
[e] Emitir extrato.
[q] Sair do sistema.

[----------------------------------]

--->  '''

while True:
    processo = input(menu_log).lower()
    if processo == 'out':
        break


    elif processo == 'sign':
        cadastrar_user(users)


    elif processo == 'current':
        if not (users == []):
            cadastrar_conta(users, contas)
        else:
            print('É necessário um usuário para abrir uma conta!')

            
    elif processo == 'users':
        listar_users(users)


    elif processo == 'accounts':
        listar_contas(contas)


    elif processo == 'enter':
        if contas == []:
            print('É necessário uma conta para acessar o menu de processos!')
        else:

            listar_contas(contas)
            conta = int(input('\nAo selecionar uma conta-corrente, insira apenas o número da conta.\nSelecione uma conta|  '))-1
            while True:
                processo_conta = input(menu_processos).lower()

                if processo_conta == 'd':
                    deposito(saldos_num_saqs, emitir_extrato,dep_users, saq_users,conta)

                elif processo_conta == 's':

                    saque(saldos_num_saqs = saldos_num_saqs,
                          lim=500,
                          lim_saques = 3,
                          emitir_extrato = emitir_extrato,
                          conta = conta,
                          saq_users = saq_users,
                          dep_users = dep_users)

                elif processo_conta == 'e':
                    emitir_extrato(saq_users[conta],dep_users[conta])
                    print(f'\nSaldo atual: R${saldos_num_saqs[conta][0]:.2f}')

                elif processo_conta == 'q':
                    break
                else:
                    print('Insira um processo válido!')
    else:
        print('Insira um processo válido!')
