from abc import ABC, abstractmethod, abstractproperty


### CLIENTE ###

class Cliente():
    def __init__(self, endereço):
        self._endereço = endereço
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        if isinstance(transacao, Saque):
           conta.sacar(int(input('Insira o valor do Saque|  ')))
        elif isinstance(transacao, Deposito):
            conta.depositar(int(input('Insira o valor do Deposito|  ')))

    def add_conta(self, conta):
        self._contas.append(conta)



class PessoaFisica(Cliente):
    def __init__(self,endereço, nome, data_nascimento, cpf):
        super().__init__(endereço)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

### /CLIENTE ###
### CONTA ###

class Conta:
    _num_contas = 0

    def __init__(self,agencia, saldo = 0,/, *, cliente):
        Conta._num_contas += 1
    
        self._saldo = saldo
        self._agencia = agencia
        self.cliente = cliente
        self.num = Conta._num_contas
        self.hist = Historico(self)


    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    
    def sacar(self, valor):
        saldo_faltando = self.saldo < valor
        if saldo_faltando:
            print('Saldo insuficiente. Saque falhou.')
            return False
        else:
            self.saldo -= valor
            Saque(valor).registrar(self)
            return True

    def depositar(self, valor):
        negativo = valor <= 0
        if negativo:
            print('Valor inválido. Depósito falhou.')
            return False
        else:
            self.saldo += valor
            Deposito(valor).registrar(self)
            return True


    @classmethod
    def nova_conta(cls, cliente, agencia)
        return Conta(agencia, cliente=cliente)



class ContaCorrente(Conta):
    def __init__(self, agencia,  limite = 500, lim_saques = 3, saldo = 0,/, *, cliente):
        super().__init__(agencia, saldo, cliente, num, hist)
        self._limite = limite
        self._lim_saques = lim_saques

    def sacar(self, valor):
        saldo_faltando = self.saldo < valor
        numero_saques_acabou = len(self.hist.saques) > lim_saques
        valor_excedeu = valor > limite 
        if numero_saques_acabou or valor_excedeu or saldo_faltando:
            print('Operação de saque falhou.')
            return False
        else:
            self.saldo -= valor
            Saque(valor).registrar(self)
            print('Operação de Saque realizada com sucesso!')
            return True


### /CONTA ###
### HISTORICO ###

class Historico:
    def __init__(self, conta):
        self.saques = {}
        self.depos = {}
        self.conta = conta

    def adicionar_trans(self, transacao):
        if isinstance(transacao, Saque):
            self.saques[f'{len(self.saques)+1}° Saque.'] = transacao.valor
        elif isinstance(transacao, Deposito):
            self.depos[f'{len(self.saques)+1}° Depósito.'] = transacao.valor

### /HISTORICO ###
### TRANSAÇÕES ###

class Transacao(ABC):
    @abstractmethod
    def registrar(self,conta):
        pass
    
    @abstractproperty
    def valor(self):
        pass

class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor or 0
    
    def registrar(self,conta):
        conta.hist.adicionar_trans(self)



class Deposito(Transacao):
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor or 0
    
    def registrar(self,conta):
        conta.hist.adicionar_trans(self)

### /TRANSAÇÕES ###
