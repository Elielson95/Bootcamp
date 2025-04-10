import os


banco = ""
agencia = ""
conta = ""
saldo = 0
qntSaques = 0
valor = 501
saques = []
depositos = []

while True:

    opcao = input("\n\nMenu\n\n1 - Sacar\n2 - Depositar\n3 - Extrato\n")
    
    if opcao == "1":
        print("\n\n")
        if qntSaques < 3:
            valor = float(input("Informe o valor: "))
            if valor <= 500:
                if valor <= saldo:
                    saldo = saldo - valor
                    print("Saque efetuado com sucesso!")
                    saques.append(valor)
                    qntSaques+=1
                else:
                    print("\nSaldo insuficiente!")  
            else: 
                print("Limite de saque é de 500,00")                   
        else:
            print("Limite máximo de saque atingido.")
        
    elif opcao == "2":
        print("\n\n")
        banco = input("Informe o Banco: ")
        agencia = input("Informe a agencia com dígito: ")
        conta = input("Informe a conta com dígito: ")
        valor = float(input("Informe um valor válido a ser depositado: "))  
        depositos.append(valor)
        saldo = saldo + valor   
        
    else:
        print("\n\n")
        print("Agencia: ",agencia+"\nConta: "+conta+"\nSaldo: ","R$:",saldo,"\nQuantidade de saques efetuado: ",qntSaques)    
        print("Saques: ","R$:",saques)    
        print("Depositos: ","R$:",depositos) 
    