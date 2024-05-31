# Projeto DIO| Sistema Bancário V1

>[!IMPORTANT]
> A v1 do sistema trabalha com apenas um usuário, logo, não é necessário identificar número de agência e conta bancária.

## Operações possíveis
 * [x] Realizar depósito
 * [x] Realizar saque
 * [x] Emitir extrato
 * [x] Sair do sistema

### Especificações do Depósito
- Apenas valores positivos serão permitidos.
- Todos os depósitos devem ser armazenados em uma variável.

### Especificações do Saque
* Máximo de 3 saques diários, todos com limite de até R$500.00. 
* Caso não haja saldo, o sistema deve informar que não é possível fazer o saque por falta de saldo. 
* Os saques devem ser armazenados em uma variável.

### Especificações do extrato
* Deve emitir todos os saques e depósitos armazenados.
* Deve apresentar o valor do saldo.
* Todos os valores devem ser expressos no formato R$xxx.xx