import time
carList = []
totalVendas = 0
att = 0


class Carro:
    def __init__(self):
        self.modelo = ""
        self.placa = ""
        self.status = ""
        self.ano = 0
        self.preco = 0.0


def exibirMenu():
    print("\n")
    print("\033[30m="*30)
    print("Menu:")
    print("0 - Sair")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Vender")
    print("5 - Exibir a receita")
    print("6 - Valor total por status")
    print("7 - Reservar")
    print("8 - Total de atualizações")
    print("9 - Acima de R$50000")
    print("10 - Consulta para compra\033[0m")
    print("="*30)


def validarPlaca(placa, lista):
    placaValida = True
    for x in lista:
        if x.placa == placa:
            placaValida = False
    return placaValida


def validarAno(ano):
    anoValido = False
    if 1990 < ano <= 2018:
        anoValido = True
    return anoValido


def cadastrarCarro(lista):
    novoCarro = Carro()
    novoCarro.modelo = input("Digite o modelo: ").capitalize()

    placaCar = input("Digite a placa: ").upper()
    placaValida = validarPlaca(placaCar, lista)
    if placaValida is True:
        novoCarro.placa = placaCar

    novoCarro.preco = float(input("Digite o valor:R$ "))

    anoCar = int(input("Digite o ano: "))
    anoValido = validarAno(anoCar)
    if anoValido is True:
        novoCarro.ano = anoCar

    statusCar = input("Digite o status: ").upper()
    novoCarro.status = statusCar

    if placaValida and anoValido is True:
        lista.append(novoCarro)
        print("\n\033[32mCarro cadastrado com sucesso!\033[0m\n")

    else:
        print("\n\033[31mERRO! Não foi possível cadastrar o carro!\033[0m\n")


def listarCarro(lista):
    if len(lista) != 0:
        for x in lista:
            print("\n\033[30mDados do {}\033[0m".format(x.modelo))
            time.sleep(0.3)
            print("Placa: {}".format(x.placa))
            time.sleep(0.3)
            print("Ano: {}".format(x.ano))
            time.sleep(0.3)
            print("Valor: R${:.2f}".format(x.preco))
            time.sleep(0.3)
            print("Status: {}".format(x.status))
            time.sleep(0.3)
    else:
        print("\n\033[31mNenhum carro cadastrado!\033[0m\n")


def atualizarCarro(lista):
    global att
    placaCarro = input("\nDigite a placa do veículo que deseja atualizar: ")
    foiAtualizado = False
    for x in lista:
        if x.placa == placaCarro:
            x.modelo = input("Digite o novo modelo: ").upper()
            x.preco = float(input("Digite o novo preço:R$ "))
            x.status = input("Digite o novo status: ").upper()
            foiAtualizado = True
            print("\n\033[32mCarro atualizado com sucesso!\033[0m\n")
            att += 1

    if foiAtualizado is False:
        print("\n\033[31mNenhum carro encontrado com essa placa!\033[0m\n")


while True:
    exibirMenu()
    op = int(input("\nDigite a opção desejada: "))

    if op == 0:
        print("Até logo!")
        break

    elif op == 1:
        cadastrarCarro(carList)

    elif op == 2:
        listarCarro(carList)

    elif op == 3:
        atualizarCarro(carList)
