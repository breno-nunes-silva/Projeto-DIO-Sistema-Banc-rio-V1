# Projeto DIO| Sistema Bancário V2

## Objetivo geral
 * [x] Separar as funções de saque, depósito e extrato.
 * [x] Nova função de cadastrar usuário.
 * [x] Nova função de criar conta-corrente.

### Novas especificações de Saque
A função saque deve receber argumentos apenas por keyword_only. 

### Novas especificações de depósito
A função depósito deve receber argumentos apenas por positional_only.

### Novas especificações do extrato.
A funçãoeve receber argumentos tanto por positional_only e por keyword_only.

## Novas funções
### Especificações de cadastrar usuário.
O programa deve armazena os usuários em uma lista e um usuário é composto por: nome, data de nascimento, cpf e endereço. o endereço é uma string composta por logradouro - nro - bairro - cidade/sigla_estado. Somento os números do CPF são armazenados e 2 usuários não podem ter o mesmo CPF.

### Especificações de criar conta-corrente.
O programa deve armazena as contas em uma lista e uma conta é composta por: agência, usuário e número da conta. O número da conta é sequencial, iniciando em 1. A agência é fixa como '0001'. O usuário é indicado pelo seu cpf vinculado a conta e um cpf pode estar vinculado a mais de uma conta.

Cada conta criada, cria 3 objetos de lista dentro das listas de Saldo/num_saques, saques e depósitos. As 3 listas criadas pela conta sempre terão o index como o número da conta subtraído de 1. As listas criadas servem para armazenar as variáveis ligadas a uma conta-corrente.