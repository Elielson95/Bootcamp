banco = ""
agencia = ""
conta = ""
saldo = 0
qntSaques = 0
valor = 501
saques = []
depositos = []


class Caixa():
    
    def sacar(valor):
        
        if valor <= 500:
            if valor <= saldo:
                retorno = True
                saldo = saldo - valor
            else:
                
                retorno = False
        else: 
            print("Limite de saque é de 500,00")   
            retorno = False                
        return retorno
                
    def depositar():
        global saldo
        banco = input("Informe o Banco: ")
        agencia = input("Informe a agencia com dígito: ")
        conta = input("Informe a conta com dígito: ")
        valor = float(input("Informe o valor: "))  
        saldo = saldo + valor   

        
    def extrato():
        
        return saldo


        

