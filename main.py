"""
*** Exercício com abstração, herança, encapsulamento e polimorfismo. ***

Criar um sistema bancário que tenha clientes, contas e banco.
    - O cliente tem uma conta e possa sacar/depositar nessa conta.
    - Contas corrente tem limite extra.
    - Banco tem clientes e contas.

Este módulo no momento é apenas para testar os módulos cliente, contas e banco
"""

#todo Uma melhor integração entre os módulos

from banco import Banco
from cliente import Pessoa, Cliente
from contas import ContaCorrente, ContaPoupanca

banco = Banco()

cliente_01 = Cliente('Chrystian', 'Costa', 26, 'Masculino')
cliente_02 = Cliente('Gizele', 'Danzo', 36, 'Feminino')
cliente_03 = Cliente('Leticia', 'Durazo', 27, 'Feminino')

conta_01 = ContaCorrente(1111, '111111', 0.0, 1000.00)
conta_02 = ContaCorrente(2222, '222222', 0.0, 2000.00)
conta_03 = ContaPoupanca(3333, '333333', 0.0)

cliente_01.inserir_conta(conta_01)
cliente_02.inserir_conta(conta_02)
cliente_03.inserir_conta(conta_03)

print('Seção de falhas')
if banco.autentificar(cliente_01):
    cliente_01.conta.depositar(1000)
    cliente_01.conta.sacar(1500)
    cliente_01.conta.mostrar_dados()

if banco.autentificar(cliente_02):
    cliente_02.conta.depositar(2000)
    cliente_02.conta.sacar(2500)
    cliente_02.conta.mostrar_dados()

if banco.autentificar(cliente_03):
    cliente_03.conta.depositar(3000)
    cliente_03.conta.sacar(1000)
    cliente_03.conta.sacar(3000)
    cliente_03.conta.mostrar_dados()
print('')

print('Seção de Inserções')
banco.inserir_cliente(cliente_01)
banco.inserir_cliente(cliente_02)
banco.inserir_cliente(cliente_03)
print('')

print('Seção de Sucessos')
if banco.autentificar(cliente_01):
    cliente_01.conta.depositar(1000)
    cliente_01.conta.sacar(1500)
    cliente_01.conta.mostrar_dados()

if banco.autentificar(cliente_02):
    cliente_02.conta.depositar(2000)
    cliente_02.conta.sacar(2750)
    cliente_02.conta.mostrar_dados()

if banco.autentificar(cliente_03):
    cliente_03.conta.depositar(3000)
    cliente_03.conta.sacar(1000)
    cliente_03.conta.sacar(3000)
    cliente_03.conta.mostrar_dados()
print('')
