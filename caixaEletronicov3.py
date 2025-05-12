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

saldo = 0

class Menu:
    
    def sacar(self, liCliente):
        encontrado = False
        conta = str(input("Informe a conta: "))
        for itemLista in liCliente:
            
                if itemLista['conta'] == conta:
                    saldo = itemLista['saldo']

                    while True:
                        valor = int(input("Informe um valor de saque até 500,00: "))
                        if valor <= 500:
                            if valor > saldo or saldo == 0:
                                print("Saldo insuficiente!")
                                retorno = False
                                break
                            else:
                                retorno = True
                                break
                        
                               
                    if retorno == True:
                        limite = itemLista['limite']
                        extratoAntigo = itemLista['extrato']
                        encontrado = True
                        if limite < 5:
                            saldo = saldo - valor
                            limite = limite + 1
                                                       
                            itemLista['limite'] = limite
                            itemLista['saldo'] = saldo
                            
                            data = str(datetime.now().ctime())
                            
                            extrato = extratoAntigo + str("[ "+"Valor: "+str(valor)+"| Data: "+data+"| Qnt Saques: "+str(limite)+"]")
                            itemLista['extrato'] = extrato
                            
                            
                            
                            print("Saque efetuado com sucesso!")
                        else:
                            print("Limite do saque excedido!")

        if encontrado == False:
            print("Conta não encontrada!")
            
        return liCliente

    def depositar(self, liCliente):
        encontrado = False
        conta = input("Informe a conta para depósito: ")
        valor = int(input("Informe o valor a ser depositado: "))
        
        for itemLista in liCliente:
           
            if itemLista['conta'] == conta:
                saldo = itemLista['saldo']
                saldo = saldo + valor
                itemLista['saldo'] = saldo
                encontrado = True
                
        if encontrado == False:
            print("Conta não encontrada!")        
        return liCliente
       
    def extrato(self):
        pass
        #print(cliente)         
    
    def sair(self):
        exit    
        
        
        
        
    #def menu():
        transacoes = 0
        deposito = 0
        saques = []
        registrosDepositos = []
        saldo = 0
        ciclo = True
        retorno = False
        
        while True:
            
            opcao = input("MENU\n\n1 - SACAR\n2 - DEPOSITAR\n3 - EXTRATO\n4 - Sair\n\n")
            
            if opcao == "1":

                while True:
                    valor = float(input("Informe um valor de saque até 500,00: "))
    
                    if valor <= 500:
                        
                        if valor < saldo or saldo == 0:
                            print("Saldo insuficiente!")
                            break
                        
                        else:
                            retorno = True
                            break
                                           
                if retorno == True:
                    saldo = valor - saldo
                    transacoes = transacoes + 1
                    data = str(datetime.now().ctime())
                    mes = str(datetime.now().date())
                    print(mes)
                    tempo = str("Valor: "+str(valor)+" Data: "+data+"Qnt Saques: "+str(transacoes))
                    print("Saque efetuado com sucesso!")
                    retorno = False
                    

                print("\n")
               
            elif opcao == "2":
                banco = input("Informe o Banco: ")
                agencia = input("Informe a agencia com dígito: ")
                conta = input("Informe a conta com dígito: ")
                valor = float(input("Informe um valor para depósito: "))
                saldo = saldo + valor
                deposito = deposito + 1 
                data = str(datetime.now().ctime())
                mes = str(datetime.now().date())
                print(mes)
                tempo = str("Banco: "+banco+" Agencia: "+agencia+" Conta: "+conta+" Saque: "+str(deposito)+" Data: "+data+" Valor: "+str(valor)+" Saldo: "+str(saldo))
                registrosDepositos.append(tempo)
                transacoes = transacoes + 1
                
            elif opcao == "3":
                registrosDepositos.append("Saldo: "+str(saldo))
                print(registrosDepositos)    
            
            else:
                break

    