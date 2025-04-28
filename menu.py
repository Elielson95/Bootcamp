import os
from datetime import datetime
from caixa import Caixa


class Menu:
    def menu():
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
Menu.menu()        