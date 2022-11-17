from tkinter import N
from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print("==================")
    print("=======Banco======")
    print("==================")

    print("Selecione uma opção das opções abaixo: ")
    print("1 - Criar conta!")
    print("2 - Efetuar saque!")
    print("3 - Efetuar depósito!")
    print("4 - Efetuar transferência")
    print("5 - Listar contas")
    print("6 - Sair do sistema")

    opcao: int(input())

    if (opcao == 1):
        criar_conta()
    elif (opcao == 2):
        efetuar_saque()
    elif (opcao == 3):
        efetuar_deposito
    elif (opcao == 4):
        efetuar_transferencia()
    elif (opcao == 5):
        listar_contas()
    elif (opcao == 6):
        print("Volte sempre!")
        sleep(2)
        exit(0)
    else:
        print("Opção inválida")
        sleep(2)
        menu()


def criar_conta() -> None:

    print("Informe os dados do cliente abaixo: ")

    nome: str = input("Nome do cliente: ")
    email: str = input("Email do cliente: ")
    cpf: str = input("CPF do cliente: ")
    data_nascimento: str = input("Digite a data de nascimento do cliente: ")

    cliente: Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print("Conta criada com sucesso!")
    print("Dados da conta: ")
    print("----------------")
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if (len(contas) > 0):
        numero: int = int(input("Informe o número da sua conta: "))

        conta: Conta = buscar_conta_por_numero(numero)

        if (conta):
            valor: float = float(input("Informe o valor do saque: "))

            conta.sacar(valor)
        else:
            print(f"Não foi encontrada a conta com o número: {conta}")
    else:
        print("Ainda não existem contas cadastradas!")
        sleep(2)
        menu()

def efetuar_deposito() -> None:
    if (len(contas) > 0):
        numero: int = int(input("Informe o número da conta para depósito: "))

        conta: Conta = buscar_conta_por_numero(numero)

        if (conta):
            valor: float = float(input("Digite o valor do depósito: R$"))

            conta.depositar(valor)
        else:
            print(f"Não foi encontrada conta com o número {numero}")
    else:
        print("Ainda não existem contas cadastradas!")
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if (len(contas) > 0):
        numero_origem: int = int(input("Informe o número da sua conta: "))

        conta_origem: Conta = buscar_conta_por_numero(numero_origem)

        if(conta_origem):
            numero_destino : int = int(input("Informe o número da conta do destino: "))

            conta_destino: Conta = buscar_conta_por_numero(numero_destino)

            if (conta_destino):
                valor: float = float(input("Informe o valor da transferência: R$"))

                conta_origem.transferir(conta_destino, valor)
            else:
                print(f"A conta destino com número {numero_destino} não foi encoontrada!")
        else:
            print(f"A sua conta com número {numero_origem} não foi encontrada!")
    else:
        print("Ainda não existem contas cadastradas!")
    sleep(2)
    menu()        

def listar_contas() -> None:
    if (len(contas) > 0):
        print("Listagem de contas: ")
        
        for conta in contas:
            print(conta)
            print("--------------")
            sleep(1)
    else:
        print("Não existem contas cadastradas!")
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = N
    
    if (len(contas) > 0):
        for conta in contas:
            if (conta.numero == numero):
                c = conta
    return c


if (__name__ == "__main__"):
    main()
