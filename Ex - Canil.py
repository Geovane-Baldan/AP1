import time
listaDogs = []
contGeral = 0
contViraLata = 0
totalKg = 0


class Dog:
    def __init__(self):
        self.nome = ""
        self.peso = 0.0
        self.raca = ""
        self.idade = 0


def exibirMenu():
    print("="*45)
    print("Menu:")
    print("1 - Cadastrar novo cachorro")
    print("2 - Listar cadastros")
    print("3 - Atualizar os dados")
    print("4 - Encontrar o mais velho")
    print("5 - Excluir os cachorros por raça")
    print("6 - Percentual de Vira-latas")
    print("7 - Encontrar o mais magro")
    print("8 - Exibir a quantidade por raça")
    print("9 - Exibir o estoque de ração para 12 meses")
    print("10 - Sair")
    print("="*45)


def validarNome(lista, nome):
    jaExiste = False
    for elemento in lista:
        if elemento.nome == nome:
            jaExiste = True
    return jaExiste


def cadastrarDogs(lista1,):
    novoDog = Dog()

    global contGeral, contViraLata, totalKg

    nomeDog = input("Digite o nome do animal: ").capitalize()
    nomeRepetido = validarNome(lista1, nomeDog)

    if nomeRepetido is False:
        novoDog.nome = nomeDog

        pesoDog = float(input("Digite o peso: "))
        totalKg += pesoDog

        racaDog = input("Digite a raça: ").capitalize()

        if racaDog == "Vira lata" or racaDog == "Vira-lata":
            contViraLata += 1

        idadeDog = int(input("Digite a idade: "))

        novoDog.peso = pesoDog
        novoDog.raca = racaDog
        novoDog.idade = idadeDog

        contGeral += 1

        lista1.append(novoDog)

        print("\n\033[32mCachorro cadastrado com sucesso!\033[0m\n")

    else:
        print("\n\033[31mErro! Nome ja cadastrado!\033[0m\n")


def listarDogs(lista):
    num = 1
    if len(lista) != 0:
        print("="*30)
        for elemento in lista:
            print("\nDados do Dog {}:".format(num))
            time.sleep(0.3)
            print("Nome: {}".format(elemento.nome))
            time.sleep(0.3)
            print("Peso: {}Kg".format(elemento.peso))
            time.sleep(0.3)
            print("Raça: {}".format(elemento.raca))
            time.sleep(0.3)
            print("Idade: {} anos".format(elemento.idade))
            time.sleep(0.3)
            num += 1
        print("="*30)
    else:
        print("\n\033[31mNenhum cachorro cadastrado!\033[0m\n")


def atualizarDogs(lista):
    nomeDog = input("Digite o nome do animal: ").capitalize()
    att = False
    for elemento in lista:
        if elemento.nome == nomeDog:
            elemento.peso = float(input("Digite o novo peso: "))
            elemento.raca = input("Digite a nova raça: ").capitalize()
            elemento.idade = int(input("Digite a nova idade: "))
            att = True
            print("\n\033[32mCachorro atualizado com sucesso!\033[0m\n")

    if att is False:
        print("\n\033[31mERRO! Cachorro não encontrado!\033[0m\n")


def encontrarIdoso(lista):
    maisVelho = ""
    idadeMaisVelho = 0

    if len(lista) != 0:
        for elemento in lista:
            if elemento.idade > idadeMaisVelho:
                idadeMaisVelho = elemento.idade
                maisVelho = elemento.nome

        print("\nO cachorro mais velho é o {} que tem {} anos.\n".format(maisVelho, idadeMaisVelho))

    else:
        print("\n\033[31mERRO! Nenhum cachorro cadastrado!\033[0m\n")


def excluirDogs(lista):
    sucesso = False

    racaEsc = input("Digite a raca que deseja excluir: ").capitalize()

    for elemento in lista:
        if elemento.raca == racaEsc:
            lista.remove(elemento)
            sucesso = True

    if sucesso is True:
        print("\n\033[32mCachorros excluídos com sucesso!\033[0m\n")

    else:
        print("\n\033[31mNenhum cachorro foi excluído!\033[0m\n")


def percentualDogs():
    if contGeral > 0:
        print("\nOs cachorros vira-lata representam {}% do total.".format((contViraLata / contGeral) * 100))
    else:
        print("\nOs cachorros vira-lata representam {}% do total.".format((contViraLata / 1) * 100))


def maisMagro(lista):
    dogPeso = lista[0].peso
    dogMagro = ""
    if len(lista) != 0:
        for elemento in lista:
            if elemento.peso < dogPeso:
                dogPeso = elemento.peso
                dogMagro = elemento.nome

        print("\nO cachorro mais magro é o {} que pesa {}Kg.".format(dogMagro, dogPeso))

    else:
        print("\n\033[31mERRO! Nenhum cachorro cadastrado!\033[0m\n")


def listarPorRaca():
    if len(listaDogs) != 0:
        racas = []
        for i in listaDogs:
            racas.append(i.raca)
        for a in racas:
            print("{} : {} cães.".format(a, racas.count(a)))
            for z in racas:
                if z == a:
                    del racas[racas.index(z)]
    else:
        return


def quantRacao():
    totalMeses = int(input("Digite a quantidade de meses que deseja fazer estoque: "))
    if totalMeses < 1:
        print("\n\033[31mPor favor insira uma quantidade válida!\033[0m\n")
    else:
        conta = totalKg * 2 * totalMeses

        if totalMeses > 1:
            print("Você deve comprar {}Kg de ração para aguentar {} meses.".format(conta, totalMeses))
        else:
            print("Você deve comprar {}Kg de ração para aguentar 1 mês.".format(conta))


while True:
    exibirMenu()
    op = int(input("Digite a opção desejada: "))

    if op == 1:
        cadastrarDogs(listaDogs)

    elif op == 2:
        listarDogs(listaDogs)

    elif op == 3:
        atualizarDogs(listaDogs)

    elif op == 4:
        encontrarIdoso(listaDogs)

    elif op == 5:
        excluirDogs(listaDogs)

    elif op == 6:
        percentualDogs()

    elif op == 7:
        maisMagro(listaDogs)

    elif op == 8:
        listarPorRaca()

    elif op == 9:
        quantRacao()

    elif op == 10:
        print("Até logo!")
        break
