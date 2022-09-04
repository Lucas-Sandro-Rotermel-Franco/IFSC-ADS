#Atividade 1
def cadastraContato(lista, index) :
    nrTelefone = input("Informe o número de telefone: ")
    print(nrTelefone in lista.values())
    if (nrTelefone in lista.values()):
        print("Numero já existe na lista.")
        return 0
    else:
        lista[index] = nrTelefone
        return 1

def removeContato(lista):
    nrTelefone = input("Informe o número que deseja remover: ")
    lista_Valores = list(lista.values())
    if (nrTelefone in lista.values()):
        posicao = lista_Valores.index(nrTelefone)
        del lista[posicao]
        return lista
    else:
        print("Numero não existe na lista.")

def listaContatos(lista):
    print(lista)

lista = {}
index = 0
while (True):
    print("1 - Cadastrar novo contato")
    print("2 - Remove contato")
    print("3 - Listar todos os contatos")
    print("0 - Sair")
    opcao = int(input("Informe a sua opção: "))
    
    if (opcao == 1):
        index += cadastraContato(lista, index)
    elif (opcao == 2):
        lista = removeContato(lista)
    elif (opcao == 3):
        listaContatos(lista)
    elif (opcao == 0):
        break

#Atividade 2
veiculos={
    "gol"     : [15, 2019, 28.900],
    "onix"    : [5 , 2019, 27.800],
    "sandeiro": [7 , 2016, 15.700],
    "hb20"    : [12, 2020, 38.500],
    "siena"   : [9 , 2016, 18.200],
    "prisma"  : [6 , 2015, 14.300],
    "voyage"  : [4 , 2020, 48.100],
    "uno"     : [2 , 2019, 28.400]
}

def atualizaEstoque():
    modelo = input("Qual modelo deseja atualizar o estoque:")
    if (modelo in veiculos):
        qtd = int(input("Qual o valor que deseja alterar o estoque: "))
        veiculos[modelo][0] = qtd
    else:
        print("Modelo não existente")

    return veiculos

def vendeCarro():
    modelo = input("Qual modelo será vendido? ")
    if (modelo in veiculos):
        qtd = veiculos[modelo][0]

        if (qtd > 0):
            veiculos[modelo][0] -= 1
        else:
            print("Não temos mais estoque desse carro.")
    else:
        print("Modelo não existente")
    
    return veiculos

def geraRelatorio():
    print(veiculos)

while (True):
    print("1 - Atualiza estoque")
    print("2 - Vende carro")
    print("3 - Gera relatório")
    print("0 - Sair")
    opcao = int(input("Informe a sua opção: "))
    
    if (opcao == 1):
        veiculos = atualizaEstoque()
    elif (opcao == 2):
        veiculos = vendeCarro()
    elif (opcao == 3):
        geraRelatorio()
    elif (opcao == 0):
        break

#Atividade 3
contatos = {}

def insereContato():
    nome = input("Informe o nome do contato: ")
    if (nome in contatos):
        print("Contato já existente")
    else:
        contatos[nome] = [input("Informe o sobrenome: "), input("Informe o telefone celular: "), input("Informe o telefone comercial: "), input("Informe o e-mail: ")]

def buscaContatoPorNome():
    nome = input("Informe o nome que procura: ")
    if (nome in contatos):
        print(contatos[nome])
    else:
        print("Contato não existe!")

def geraRelatorioContatos():
    print(contatos)

while(True):
    print("1 - Insere contato")
    print("2 - Busca contato por nome")
    print("3 - Gera relatório")
    print("0 - Sair")
    opcao = int(input("Informe a sua opção: "))
    
    if (opcao == 1):
        insereContato()
    elif (opcao == 2):
        buscaContatoPorNome()
    elif (opcao == 3):
        geraRelatorioContatos()
    elif (opcao == 0):
        break

#Atividade 4
arquivo = open('ip.txt', 'r')

lista = arquivo.readlines()
arquivo.close

ipsValido = ''
ipsInvalido = ''

for idx in range (len(lista)):
    lista2 = lista[idx].rsplit('.')

    if (int(lista2[0]) <= 255 and int(lista2[1]) <= 255 and int(lista2[2]) <= 255 and int(lista2[3]) <= 255):
        ipsValido += lista[idx]
    else:
        ipsInvalido += lista[idx]

print("IPsVálidos", ipsValido)
print("IPsInválidos", ipsInvalido)

arquivo = open("ipsValido.txt", 'w')
arquivo.write(ipsValido)
arquivo.close

arquivo = open("ipsInvalido.txt", 'w')
arquivo.write(ipsInvalido)
arquivo.close
