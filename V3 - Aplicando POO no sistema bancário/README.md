# Projeto DIO| Sistema Bancário V3

## Objetivo geral
 * Aplicar os ensinamentos de Programação Orientada a Objetos no sistema bancário.

## Classes

### Cliente
Classe feita para armazenar as informações de um cliente, como endereço e contas em seu nome. Tem métodos para a realização de um transação, chamando uma conta, e adicionar uma conta à sua lista.
#### Pessoa Física
Classe que herda Cliente, específica para pessoas físicas. Possui os atributos de cpf, data de nascimento e nome além dos atributos de sua superclasse.

### Conta
Classe feita para armazenar os dados de uma conta de banco e realizar transações. Possui métodos de saque, depósito, criar uma conta a partir de um cliente e uma agênciae também uma property que expressa seu saldo.

#### Conta Corrente
Clsse que herda Conta, específica para contas com necessidade de atividade bancária. Limita o número de saques por sessão em um valor dado pelo usuário e limita o valor máximo de saque em um valor também informado pelo usuário (ambos por padrão são 3 e 500, respectivamente).

### Histórico
Classe que armazena o histórico de transações de uma conta. Cada instância de Conta possui uma instância própria de Histórico também.

### Transação
Classe abstrata que é a interface das classes de transação. Possui um método abstrato para registrar a transação no histórico de uma conta e uma property abstrata para expressar o valor da transação. 
#### Saque
Classe que herda da interface Transação. Remete ao tipo de transação saque.
#### Saque
Classe que herda da interface Transação. Remete ao tipo de transação depósito.