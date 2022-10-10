from datetime import date
data=date.today()
meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro' , 'dezembro']
data2=str(data).split('-')
ano, mes, dia=data2
mes=meses[int(mes)-1]
print(dia,mes,ano)
mes=meses[0]


estoquearq1=open(f"estoque de janeiro.txt","a")
vendasarq1=open(f"vendas de janeiro.txt","a")

estoquearq2 = open(f"estoque de fevereiro.txt", "a")
vendasarq2 = open(f"vendas de fevereiro.txt", "a")

estoquearq3 = open(f"estoque de março.txt", "a")
vendasarq3 = open(f"vendas de março.txt", "a")

estoquearq4 = open(f"estoque de abril.txt", "a")
vendasarq4 = open(f"vendas de abril.txt", "a")

estoquearq5 = open(f"estoque de maio.txt", "a")
vendasarq5 = open(f"vendas de maio.txt", "a")

estoquearq6 = open(f"estoque de junho.txt", "a")
vendasarq6 = open(f"vendas de junho.txt", "a")

estoquearq7= open(f"estoque de julho.txt", "a")
vendasarq7 = open(f"vendas de julho.txt", "a")

estoquearq8 = open(f"estoque de agosto.txt", "a")
vendasarq8 = open(f"vendas de agosto.txt", "a")

estoquearq9 = open(f"estoque de setembro.txt", "a")
vendasarq9 = open(f"vendas de setembro.txt", "a")

estoquearq10 = open(f"estoque de outubro.txt", "a")
vendasarq10 = open(f"vendas de outubro.txt", "a")

estoquearq11 = open(f"estoque de novembro.txt", "a")
vendasarq11 = open(f"vendas de novembro.txt", "a")

estoquearq12 = open(f"estoque de dezembro.txt", "a")
vendasarq12 = open(f"vendas de dezembro.txt", "a")

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
    global mes
    global estoquearq1
    global vendasarq1
    global estoquearq2
    global vendasarq2
    global estoquearq3
    global vendasarq3
    global estoquearq4
    global vendasarq4
    global estoquearq5
    global vendasarq5
    global estoquearq6
    global vendasarq6
    global estoquearq7
    global vendasarq7
    global estoquearq8
    global vendasarq8
    global estoquearq9
    global vendasarq9
    global estoquearq10
    global vendasarq10
    global estoquearq11
    global vendasarq11
    global estoquearq12
    global vendasarq12

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
            estoquearq1.write(f"produto:{produto}\npreço R$:{preco}\nestoque:{quantidade}\n\n")

            if mes == "janeiro":
                estoquearq1.write(f"produto:{produto}\npreço R$:{preco}\nestoque:{quantidade}\n\n")
            elif mes == "fevereiro":
                estoquearq2.write(f"produto:{produto}\npreço R$:{preco}\nestoque:{quantidade}\n\n")
            elif mes == "março":
                estoquearq3.write(f"produto:{produto}\npreço R$:{preco}\nestoque:{quantidade}\n\n")
            elif mes == "abril":
                estoquearq4.write(f"produto:{produto}\npreço R$:{preco}\nestoque:{quantidade}\n\n")
            elif mes == "maio":
                estoquearq5.write(f"produto:{produto}\npreço R$:{preco}\nestoque:{quantidade}\n\n")
            elif mes == "junho":
                estoquearq6.write(f"produto:{produto}\npreço R$:{preco}\nestoque:{quantidade}\n\n")
            elif mes == "julho":
                estoquearq7.write(f"produto:{produto}\npreço R$:{preco}\nestoque:{quantidade}\n\n")
            elif mes == "agosto":
                estoquearq8.write(f"produto:{produto}\npreço R$:{preco}\nestoque:{quantidade}\n\n")
            elif mes == "setembro":
                estoquearq9.write(f"produto:{produto}\npreço R$:{preco}\nestoque:{quantidade}\n\n")
            elif mes == "outubro":
                estoquearq10.write(f"produto:{produto}\npreço R$:{preco}\nestoque:{quantidade}\n\n")
            elif mes == "novembro":
                estoquearq11.write(f"produto:{produto}\npreço R$:{preco}\nestoque:{quantidade}\n\n")
            elif mes == "dezembro":
                estoquearq12.write(f"produto:{produto}\npreço R$:{preco}\nestoque:{quantidade}\n\n")

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

                    if mes =="janeiro":
                        vendasarq1.write(f"produto:{produto}\nvalor R$:{preco}\nestoque:{quantidade-qtde}\n\n")
                    elif mes =="fevereiro":
                        vendasarq2.write(f"produto:{produto}\nvalor R$:{preco}\nestoque:{quantidade-qtde}\n\n")
                    elif mes =="março":
                        vendasarq3.write(f"produto:{produto}\nvalor R$:{preco}\nestoque:{quantidade-qtde}\n\n")
                    elif mes == "abril":
                        vendasarq4.write(f"produto:{produto}\nvalor R$:{preco}\nestoque:{quantidade - qtde}\n\n")
                    elif mes =="maio":
                        vendasarq5.write(f"produto:{produto}\nvalor R$:{preco}\nestoque:{quantidade-qtde}\n\n")
                    elif mes == "junho":
                        vendasarq6.write(f"produto:{produto}\nvalor R$:{preco}\nestoque:{quantidade - qtde}\n\n")
                    elif mes == "julho":
                        vendasarq7.write(f"produto:{produto}\nvalor R$:{preco}\nestoque:{quantidade - qtde}\n\n")
                    elif mes == "agosto":
                        vendasarq8.write(f"produto:{produto}\nvalor R$:{preco}\nestoque:{quantidade - qtde}\n\n")
                    elif mes == "setembro":
                        vendasarq9.write(f"produto:{produto}\nvalor R$:{preco}\nestoque:{quantidade - qtde}\n\n")
                    elif mes == "outubro":
                        vendasarq10.write(f"produto:{produto}\nvalor R$:{preco}\nestoque:{quantidade - qtde}\n\n")
                    elif mes == "novembro":
                        vendasarq11.write(f"produto:{produto}\nvalor R$:{preco}\nestoque:{quantidade - qtde}\n\n")
                    elif mes == "dezembro":
                        vendasarq12.write(f"produto:{produto}\nvalor R$:{preco}\nestoque:{quantidade - qtde}\n\n")

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

