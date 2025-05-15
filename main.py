# DICIONÁRIO

nome = {
    "produtos": [],
}

quantidade = {
    "produtos": [],
}

valor = {
    "produtos": [],
}

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

            nome["produtos"].append(nome_prod)
            valor["produtos"].append(valor_prod)
            quantidade["produtos"].append(quant_prod)

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


