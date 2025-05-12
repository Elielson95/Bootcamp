nome = 'Eli'
cpf = '067'
endereco = 'T'
agencia = '183'
conta = '2020'
saldo = 0
contaTeste = "2020"

diCliente = {'nome': nome, 'cpf': cpf, 'endereco': endereco, 'agencia': agencia, 'conta': conta, 'saldo': saldo}
liCliente = []


liCliente.append(diCliente)

  
for itemLista in liCliente:
    if itemLista['conta'] == contaTeste:
        itemLista["saldo"] = 20
        saldo = itemLista["saldo"]
        print(type(saldo))
        

print(liCliente)
