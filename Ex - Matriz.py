from random import randint
ind = 0
matriz = []
end = -1
linhas = 0
colunas = 0
contPares = 0


def menu():
    print("\n")
    print("="*40)
    print("Menu:")
    print("1 - Gerar matriz")
    print("2 - Encontrar numero especifico")
    print("3 - Encontrar correspondente por posição")
    print("4 - Encontrar numeros pares")
    print("5 - Sair")
    print("="*40)


def gerarMatriz():
    global linhas, colunas, contPares
    linhas = int(input("\nQuantas linhas: "))
    colunas = int(input("Quantas colunas: "))
    for i in range(linhas):
        linha = []

        for j in range(colunas):
            valor = randint(0, 9)
            linha.append(valor)
            if valor % 2 == 0 and valor != 0:
                contPares += 1

        matriz.append(linha)

    for i in range(linhas):
        print(matriz[i])


def numEspecifico():
    global linhas, colunas
    while True:
        elemento = int(input("\nDigite um numero que deseja procurar na matriz: "))
        if elemento < 10 or elemento > 0:
            existe = False
            for i in range(linhas):
                for j in range(colunas):
                    if matriz[i][j] == elemento:
                        print("Achei o numero {} na: Linha[{}] e Coluna [{}]".format(elemento, i+1, j+1))
                        existe = True

            if existe is False:
                print("\nNão foi encontrado esse numero na matriz!")

        continuar = input("\nDeseja continuar procurando? ").capitalize()
        if continuar not in "SimS":
            break


def posicao():
    m = int(input("\nDigite a linha: "))
    if m > linhas:
        print("A matriz nãp possui tantas linhas assim!")
    else:
        n = int(input("Digite a coluna: "))
        if n > colunas:
            print("A matriz nãp possui tantas colunas assim!")
        else:
            print("\nO elemento na posição [{}][{}] é o {}".format(m, n, matriz[m-1][n-1]))


def pares():
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] % 2 == 0:
                if matriz[i][j] != 0:
                    print("O número {} que está na posição [{}][{}] é par.".format(matriz[i][j], i+1, j+1))

    print("\nAo todo foram gerados {} numeros pares.".format(contPares))


while end != 0:
    menu()
    op = int(input("\nDigite a opção desejada: "))

    if op == 1:
        gerarMatriz()

    elif op == 2:
        numEspecifico()

    elif op == 3:
        posicao()

    elif op == 4:
        pares()

    elif op == 5:
        print("Até logo!")
        end = 0

    else:
        print("Selecione uma opção válida!")