from datetime import date

data = date.today()
print(data)
print(data.month)
mes = data.strftime("%b")
print(mes)
#meses=['janeiro','fevereiro','março','abril','maio','junho','agosto','setembro','outubro','novembro','dezembro']

estoquearq=open(f"estoque de.txt","a")
vendasarq=open(f"vendas de .txt","a")


estoque = {}
fim = False
produtos = []

def n():
    quantidade = int(input("Quantidade do produto: "))
    preco = float(input("Preço do produto: "))

    estoque[produto] = [quantidade, preco]

def programa():
    global estoque
    global fim
    global produtos
    global estoquearq
    global vendasarq
    while not fim:
        print(
            "\nDigite 'fim' para finalizar\nDigite 'p' para exibir o estoque\nDigite 'c' para comprar algo do estoque\nDigite 'e' para adicionar no estoque")
        opcao = input("Opção:  ")

        if opcao == "e":
            produto = input("\nNome do produto: ")
            produtos.append(produto)
            quantidade = int(input("Quantidade do produto: "))
            preco = float(input("Preço do produto: "))

            estoque[produto] = [quantidade, preco]
            estoquearq.write(f"produto:{produto}\npreço R$:{preco}\nestoque:{quantidade}\n\n")

        elif opcao == 'c':
            itens_disponiveis = []

            for i in estoque: itens_disponiveis.append(i)

            print(f'Produtos disponiveis: {", ".join(itens_disponiveis)}')

            if not itens_disponiveis:
                print('Não tem nenhum item no estoque!')
                programa()

            nome = input("Nome do produto: ")

            # Verificar se existe
            if nome not in itens_disponiveis:
                print('O item não existe!')
                programa()
            else:
                print(f'\t{nome} tem {estoque[nome][0]} unidades no estoque')
                print(f'\tPreço do {nome} = R${estoque[produto][1]}')

                qtde = int(input("Quantidade a comprar: "))
                if qtde <= estoque[produto][0]:  # qtde < estoque
                    preco = qtde * estoque[produto][1]  # preco
                    estoque[produto][0]=estoque[produto][0]-qtde

                    vendasarq.write(f"produto:{produto}\npreço R$:{preco}\nestoque:{quantidade-qtde}\n\n")

                    print(f'\nO total da compra deu R${preco}')
                    continuar = input('Deseja continuar? (S/N): ').lower()

                    if continuar == 's':
                        pass
                    else:
                        fim = True
                else:
                    print('Coloque uma quantidade menor que o estoque')

        elif opcao == 'p':
            print(estoque)

        elif opcao == "fim":
            fim = True
            print(estoque)
            break


programa()
estoquearq.close()
vendasarq.close()
