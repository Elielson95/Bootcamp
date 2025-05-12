#Criar funções para: Sacar, depositar e histórico
#Criar usuário(nome, cpf e endereço completo)
#Criar conta corrente
#Vincular conta ao usuário
'''
Armazenar contas em uma lista, o cliente pode ter mais de uma conta
'''

import os
from datetime import datetime
from caixaEletronicov1 import Caixa
import random
from caixaEletronicov3 import Menu

saldo = 0
class horas():

    def menu(self):
        
        liCliente = []
   
        while True:
            opcao = input("MENU\n\n1 - CADASTRAR\n2 - SACAR\n3 - DEPOSITAR\n4 - EXTRATO\n5 - SAIR\n\n")
            
            if opcao == "1":
                cpfDuplicado = True
                nome = input("Informe o nome: ")
                cpf = input("Informe o cpf: ")
                endereco = input("Informe o endereço: ")
                agencia = str(random.randrange(100, 999))
                conta = str(random.randrange(1000, 10000))
                saldo = 0
                limite = 0
                extrato = " "
                for duplicidade in liCliente: 
                    if cpf == duplicidade['cpf']:
                        cpfDuplicado = False
                if cpfDuplicado == False:
                            
                    diCliente = {'nome': nome, 'cpf': cpf, 'endereco': endereco, 'agencia': agencia, 'conta': conta, 'saldo': saldo, 'limite': limite, 'extrato': extrato}
                    liCliente.append(diCliente)
                    print("Conta cadastrada com sucesso!")
                else:
                    print("Cpf informado já se encontra cadastrado em nossa base de dados.")                    
            
            elif opcao == "2":
                
                Menu.sacar(self, liCliente)
                                
            elif opcao == "3":
                
                Menu.depositar(self, liCliente)
                                
            elif opcao == "4":
                print(liCliente)
                #self.extrato()
                
            else:

                break  
        
horas().menu()            