<<<<<<< HEAD
'''
Trabalho desenvolvido com o intuito de organizar e automatizar processos no Mercadão do Zé
Autores: Andrei Machado e André Oliveira

'''

# DICIONÁRIO
=======
# DICIONÁRIO

>>>>>>> 357228f9f20b32f3a2d4f52eece2697cb4159d98
nome = {
    "produtos": [],
}

<<<<<<< HEAD

=======
>>>>>>> 357228f9f20b32f3a2d4f52eece2697cb4159d98
quantidade = {
    "produtos": [],
}

<<<<<<< HEAD

=======
>>>>>>> 357228f9f20b32f3a2d4f52eece2697cb4159d98
valor = {
    "produtos": [],
}

<<<<<<< HEAD

# VARIÁVEIS
i = 0 # Quantidade de itens
opcao = 0 # opção do menu
sair = True # saída do programa


# CADASTRAR PRODUTOS
def cadastrar(nome, valor, quantidade, i):
    with open("estoque.txt", "a", encoding="utf-8") as arquivo:
        nome_prod = input(f"\nDigite o nome do {i + 1}º produto: ")

        try:
            valor_prod = float(input(f"Digite o valor do {i + 1}º produto: "))
            while valor_prod <= 0:
                print("\nValor do produto inválido.\nTente novamente.\n")
                valor_prod = float(input(f"Digite o valor do {i + 1}º produto: "))              

            quant_prod = int(input(f"Digite a quantidade do {i + 1}º produto: "))
            while quant_prod <= 0:
                print("\nQuantidade de Produtos Inválida.\nTente novamente.\n")
                quant_prod = int(input(f"Digite a quantidade do {i + 1}º produto: "))
=======
# VARIÁVEIS

i = 0
opcao = 0

# MENU

while opcao != 5:
    print("\nMERCADÃO DO ZÉ\n")
    print("1 - ADICIONAR PRODUTO")
    print("2 - LISTAR PRODUTO")
    print("3 - ALTERAR PRODUTO")
    print("4 - BUSCAR PRODUTO")
    print("5 - SAIR")
    opcao = int(input("\nDigite uma das opções apresentadas acima: \n"))

    # CADASTRAR PRODUTOS
    if opcao == 1:
            nome_prod = input(f"\nDigite o nome do {i + 1}º  produto: ")

            valor_prod = float(input(f"Digite o valor do {i + 1}º  produto: "))

            while valor_prod <= 0:
                print("\nValor do produto inválido.\nTente novamente.\n")
                valor_prod = float(input(f"Digite o valor do {i + 1}º  produto: "))

            quant_prod = int(input(f"Digite a quantidade do {i + 1}º  produto: "))

            while quant_prod <= 0:
                print("\nQuantidade de Produtos Inválida.\nTente novamente.\n")
                quant_prod = int(input(f"Digite a quantidade do {i + 1}º  produto: "))
>>>>>>> 357228f9f20b32f3a2d4f52eece2697cb4159d98

            nome["produtos"].append(nome_prod)
            valor["produtos"].append(valor_prod)
            quantidade["produtos"].append(quant_prod)

<<<<<<< HEAD
            arquivo.write(f"Produto: {nome_prod}" + "\n")
            arquivo.write(f"Valor: {str(valor_prod)}" + "\n")
            arquivo.write(f"Quantidade: {str(quant_prod)}" + "\n")
            arquivo.write("----------------\n")

            i += 1
        except ValueError:
            print("Digite um número ao invés de uma letra ou texto")
        return i


# LISTAR PRODUTOS
def listar(nome):
    print("\nProdutos Cadastrados:\n")
    for i in range(len(nome["produtos"])):
        print(f" - Produto {i + 1} - {nome['produtos'][i]}")


# ALTERAR O PRODUTO NO .TXT
def salvar_estoque(nome, valor, quantidade):
    with open("estoque.txt", "w", encoding="utf-8") as arquivo:
        for i in range(len(nome['produtos'])):
            arquivo.write(f"Produto: {nome['produtos'][i]}" + "\n")
            arquivo.write(f"Valor: {str(valor['produtos'][i])}" + "\n")
            arquivo.write(f"Quantidade: {str(quantidade['produtos'][i])}" + "\n")
            arquivo.write("----------------\n")


# ALTERAÇÃO DA QUANTIDADE
def manipular(nome, quantidade):
    alterar = input("\nDigite o nome do produto que você deseja alterar em estoque: ")

    if alterar in nome["produtos"]:
        indice = nome["produtos"].index(alterar)
        quant_alterar = int(input("\n(ATENÇÃO: insira números positivos para adicionar e negativos para diminuir)\n\nInsira a quantidade de produtos que serão alterados: "))
        try:
            quantidade["produtos"][indice] += quant_alterar
            print(f"Estoque atualizado. Novo total de {alterar}: {quantidade['produtos'][indice]}")
            salvar_estoque(nome, valor, quantidade)
        except ValueError:
            print("Digite um número ao invés de uma letra ou texto")
    else:
        print("\nProduto não encontrado.")


# BUSCAR PRODUTOS
def buscar(nome, valor, quantidade):
    buscar = input("\nDigite o nome do produto que você quer buscar: ")
    encontrado = False

    for indice in range(len(nome["produtos"])):
        if nome["produtos"][indice].lower() == buscar.lower():
            print(f"\nNome: {nome['produtos'][indice]}")
            print(f"Valor: R${valor['produtos'][indice]:.2f}")
            print(f"Quantidade: {quantidade['produtos'][indice]}")
            encontrado = True

    if not encontrado:
        print("\nProduto não encontrado. Favor tente novamente")


# MENU
def menu(opcao, sair, i):
    while sair:
        print("\nMERCADÃO DO ZÉ\n")
        print("1 - ADICIONAR PRODUTO")
        print("2 - LISTAR PRODUTO")
        print("3 - ALTERAR PRODUTO")
        print("4 - BUSCAR PRODUTO")
        print("5 - SAIR")  

        try:
            opcao = int(input("\nDigite uma das opções apresentadas acima: \n"))
            if opcao == 1:
                i = cadastrar(nome, valor, quantidade, i)
            elif opcao == 2:
                listar(nome)
            elif opcao == 3:
                manipular(nome, quantidade)
            elif opcao == 4:
                buscar(nome, valor, quantidade)
            elif opcao == 5:
                sair = False
            else:
                print("Digite um número maior que 0!")    
        except ValueError:
            print("Digite um número ao invés de uma letra ou texto")


# CHAMAR MENU
with open("estoque.txt", "r", encoding="utf-8") as arquivo:
    print("\n--- ESTOQUE ATUAL ---\n")
    print(arquivo.read())
    menu(opcao, sair, i)
=======
            i += 1



    # LISTAR PRODUTOS
    elif opcao == 2:

        print("\nProdutos Cadastrados:\n")
        for i in range(len(nome["produtos"])):
            print(f" - Produto {i} - {nome['produtos'][i]}")


    # ENTRADA E SAÍDA
    elif opcao == 3:
            
        alterar = input("\nDigite o nome do produto que você deseja alterar em estoque: ")
            
        if alterar in nome["produtos"]:
            indice = nome["produtos"].index(alterar)
            quant_alterar = int(input("\n(ATENÇÃO: insira números positivos para adicionar e negativos para diminuir)\n\nInsira a quantidade de produtos que serao alterados:"))
            quantidade["produtos"][indice] += quant_alterar
            print(f"Estoque atualizado. Novo total de {alterar}: {quantidade['produtos'][indice]}")
            
        else:
            print("\nProduto não encontrado. Favor tente novamente")



    # BUSCAR PRODUTOS
    elif opcao == 4:
            
        buscar = input("\nDigite o nome do produto que você quer buscar: ")
        encontrado = False
            
        for indice in range(len(nome["produtos"])):
            if nome["produtos"][indice].lower() == buscar.lower():
                print(f"\nNome: {nome['produtos'][indice]}")
                print(f"Valor: R${valor['produtos'][indice]:.2f}")
                print(f"Quantidade: {quantidade['produtos'][indice]}")
                encontrado = True
            
        if not encontrado:
            print("\nProduto não encontrado. Favor tente novamente")
            

    elif opcao < 1 or opcao > 5:
        print("Opcao Errada! Escolha uma opção entre: 1-5.\n")


>>>>>>> 357228f9f20b32f3a2d4f52eece2697cb4159d98
