'''   
                Projeto: Sistema Bancário com Python
Objetivo:Criar sistema bancário com operações:sacar, depositar e visualizar extrato. 
        -Nesta primeira versão de testes ainda não é necessário verificar credenciais.
    
'''
import os
seleção = 0
Valor_em_conta = 0.0
Lista_depósitos = []
Lista_saques = []
limit_saques = 3
while True:
    os.system('cls') #limpa tela
    seleção = int(input("""Escolha a opção:
          [1]Depósito
          [2]Saque
          [3]Extrato
          [4]Sair 
"""))
    if seleção == 1: #Depósito
        valor_depósito = float(input("Digite o valor do depósito "))
        if valor_depósito <=0:
            print("valor inválido")
        else:
            Valor_em_conta += valor_depósito
            Lista_depósitos.append(F"R${valor_depósito:.2f}")
            print(f"Operação bem sucedida! Seu saldo atual é: R${Valor_em_conta}")                         
    elif seleção == 2: #saque
        if limit_saques == 0:
            print("Limite diário de saques atingido") 
        else:
            valor_saque = float(input("Digite o valor do saque "))
            if valor_saque < 0:
                print("Valor inválito") 
            else:
                if valor_saque > 500:
                    print("O saque máximo é 500 reais e até, tente novamente")
                else:
                    if Valor_em_conta < valor_saque:
                        print("Não há saldo suficiente para concluir a operação")
                    else:
                        limit_saques -= 1
                        Valor_em_conta -= valor_saque
                        print(f"Operação realizada com sucesso! Seu saldo atual é: R${Valor_em_conta}")
                       
                        Lista_saques.append(f"R${valor_saque:.2f}")
    elif seleção == 3:#extrato
        print("Seu Extrato".center(30,"#"))
        print(f"Seus depósitos: {Lista_depósitos}\nSeus Saques: {Lista_saques}\nSalto atual: R${Valor_em_conta:.2f}")
        
    elif seleção == 4:#sair
        print("saindo...")
        break
    else:#valores inválidos
        print("Resposta inválida")
    input("\nPressione enter para cotinuar...")
