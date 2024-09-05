saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
valor = 0
numero_saques = 0

def deposito():
        valor = 0
        while valor <=0:   
            print("Digite um valor acima de R$0")
            valor = float(input())
        global saldo
        saldo += valor
        extrato.append((f"Deposito: R$ {valor:,.2f}"))

def saque():
        valor = None
        global numero_saques
        global saldo
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor do saque: "))
            if valor <= saldo:
                while valor > limite:
                    if valor > limite:
                        print(f"Erro: o valor não pode exceder o limite de R${limite}.")
                        valor = float(input("Digite o valor do saque: "))
                saldo -= valor
                numero_saques += 1
                #extrato[numero_saques] = valor
                extrato.append((f"Saque: R$ {valor:,.2f}"))
            else:
                 print("Saldo Excedido!")
        else:
            print("Limite de saques diários atingido!")

while True:
    print("""
                (D) - Deposito
                (S) - Saque
                (E) - Extrato
                (Q) - SAIR""")
    opcao = input()
    

    if opcao == "d":
        print("deposito")
        deposito()

    elif opcao == "s":
        print("Saque")
        saque()

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo Atual R$ {saldo:,.2f}")
        print("==========================================")

    elif opcao == "q":
        print("sair")
        break

    else:
        print("Operacao invalida")