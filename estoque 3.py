from datetime import date
data=date.today()
meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro' , 'dezembro']
ano, mes, dia=str(data).split("-")
mes=meses[int(mes)-1]
print(dia, mes, ano)

for i in meses:
    exec(f"estoque{i}=open(f\"estoque de {i}.txt\",\"a\")")
    exec(f"vendas{i}=open(f\"vendas de {i}.txt\",\"a\")")


estoque = {}
fim = False
produtos = []


def n1():
    quantidade = int(input("Quantidade do produto: "))
    preco = float(input("Preço do produto: "))

    estoque[produto] = [quantidade, preco]

def n2():
    preco = float(input("Preço do produto: "))

    estoque[produto] = [quantidade, preco]

def programa():
    global estoque
    global fim
    global produtos
    global mes


    while not fim:
        print(
            "\nDigite 'fim' para finalizar\nDigite 'p' para exibir o estoque\nDigite 'c' para comprar algo do estoque\nDigite 'e' para adicionar no estoque")
        opcao = input("Opção:  ")

        if opcao == "e":
            produto = input("\nNome do produto: ")
            produtos.append(produto)
            quantidade = int(input("Quantidade do produto: "))
            if quantidade.isnumeric == False:
                n1()
            preco = float(input("Preço do produto: "))
            if preco.isnumeric==False:
                n2()

            estoque[produto] = [quantidade, preco]

            for i in meses:
                if i == mes:
                    exec(rf'estoque{i}.write(f"produto:{produto}\npreço R$:{preco}\nestoque:{quantidade}\n\n")')


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


                    for i in meses:
                        if mes == i:
                            exec(rf"vendas{i}.write(f'produto:{produto}\nvalor R$:{preco}\nestoque:{quantidade-qtde}\n\n')")

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

