'''   
                Projeto: Sistema Bancário com Python
Objetivo:Criar sistema bancário com operações:sacar, depositar, visualizar extrato, cadastrar cliente e
criar conta. 
        
'''
import os
lista_usuarios=[]
lista_cpf = []
usuario = {}
endereço = {}
lista_contas = []
lis_num_contas =['']
numero_da_conta = len(lis_num_contas)
conta = {}
seleção = 0
Valor_em_conta = 0.0
Lista_depósitos = []
Lista_saques = []
limit_saques = 3
def deposito(valor,/):
    global Valor_em_conta
    if valor<=0:
        print("valor inválido")   
    else:
        Valor_em_conta += valor
        Lista_depósitos.append(F"R${valor:.2f}")
        print(f"Operação bem sucedida! Seu saldo atual é: R${Valor_em_conta}")

def saque(*,qte_saques_restantes,Valor_em_conta):
    if qte_saques_restantes == 0:
        print("Limite diário de saques atingido") 
    else:
        valor_saque = float(input("Digite o valor do saque "))
        if valor_saque <= 0:
            print("Valor inválito") 
        else:
            if valor_saque > 500:
                print("O saque máximo é 500 reais e até, tente novamente")
            else:
                if Valor_em_conta < valor_saque:
                    print("Não há saldo suficiente para concluir a operação")
                else:
                    global limit_saques
                    limit_saques -= 1
                    Valor_em_conta -= valor_saque
                    print(f"Operação realizada com sucesso! Seu saldo atual é: R${Valor_em_conta}")
                    Lista_saques.append(f"R${valor_saque:.2f}")
    return Valor_em_conta               

def extrato(Lista_depósitos,Lista_saques,/,*,Valor_em_conta):
    print("Seu Extrato".center(30,"#"))
    print(f"Seus depósitos: {Lista_depósitos}\nSeus Saques: {Lista_saques}\nSalto atual: R${Valor_em_conta:.2f}")

def criar_usuario():
    usuario['nome']=input("Digite o Nome completo: ")
    usuario['nascimento']=input("Digite a data de nascimento(DD/MM/AAAA): ")
    usuario['cpf'] = input("Digite seu CPF(Somente numeros): ")
    for i in usuario["cpf"]:
        if i == '.' or i == '-':
            print("Formato do CPF é inválido")
            return
    if int(usuario["cpf"]) > 99999999999 or int(usuario["cpf"]) < 1:
        print("Formato do CPF é inválido")
        return
    else:
        for i in range(len(lista_cpf)):
            if usuario["cpf"] == lista_cpf[i]:
                print("Usuário já cadastrado")
                return
        
    print("A seguir, digite as informações do endereço")
    endereço['logradouro'] = input("Logradouro: ")
    endereço['numero'] = input("Número: ")
    endereço['bairro'] = input("Bairro: ")
    endereço['cidade'] = input("Cidade: ")
    endereço['sigla_estado'] = input("Sigla do estado: ")
    usuario['endereço'] = endereço
    lista_usuarios.append(usuario)
    lista_cpf.append(int(usuario["cpf"]))
    
def criar_conta():  
    global numero_da_conta  
    cpf_atual = int(input("Digite o cpf"))
    tem_usuario = False
    for i in range(len(lista_cpf)):
        if cpf_atual == lista_cpf[i]:
            tem_usuario = True
            conta['usuário'] = lista_usuarios[i]
            break
    if tem_usuario == False:
        print("CPF não cadastrado, Cadastre seu usuário: ")
        criar_usuario()
    for j in range(len(lista_cpf)):
        if cpf_atual == lista_cpf:
            conta['usuário'] = lista_usuarios[j]
            break
    conta['agência'] = '0001'
    conta['Numero_da_conta'] = numero_da_conta
    numero_da_conta+=1
    lista_contas.append(conta)
    print("Conta cadastrada com sucesso")
while True:
    os.system('cls') #limpa tela
    seleção = int(input("""Escolha a opção:
          [1]Depósito
          [2]Saque
          [3]Extrato
          [4]Criar usuário
          [5]Criar Conta 
          [6]Lista de Usuários   
          [7]Lista de contas                                       
          [8]Sair 
"""))
    if seleção == 1:
        valor_depósito = float(input("Digite o valor do depósito "))
        deposito(valor_depósito)                       
    elif seleção == 2:
        Valor_em_conta = saque(qte_saques_restantes = limit_saques,Valor_em_conta=Valor_em_conta) 
    elif seleção == 3:
        extrato(Lista_depósitos, Lista_saques, Valor_em_conta=Valor_em_conta)
    elif seleção == 4:
        criar_usuario()
    elif seleção == 5:
        criar_conta()
    elif seleção == 6:#Apenas para verificação
        print(lista_usuarios)
    elif seleção == 7:#Apenas para verificação
        print(lista_contas)
    elif seleção == 8:#sair
        print("saindo...")
        break
    else:#valores inválidos
        print("Resposta inválida")
    input("\nPressione enter para cotinuar...")
