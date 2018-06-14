from time import sleep
main = []


class Palavra:
    def __init__(self):
        self.termo = ''
        self.sinonimos = []
        self.classe = ''


def menu():
    print('\n\033[30m')
    print('='*30)
    print('Menu:')
    print('0 - Sair')
    print('1 - Cadastrar')
    print('2 - Listar')
    print('3 - Novo sinonimo')
    print('4 - Termo com mais sinonimos')
    print('5 - Buscar palavra pela classe')
    print('6 - Excluir termo')
    print('7 - Excluir sinonimo')
    print('='*30)
    print('\n\033[0m')


def testarRepeticao(termo):
    jaExiste = False
    for x in main:
        if termo == x.termo:
            jaExiste = True

    return jaExiste


def cadastro():
    novaPalavra = Palavra()

    termoPalavra = input('Digite o termo: ').capitalize()
    termoValido = testarRepeticao(termoPalavra)

    if termoValido is False:

        sinonimoPalavra = input('Digite um sinonimo dessa palavra: ').capitalize()

        classePalavra = input('Digite a classe gramatical dessa palavra: ').capitalize()

        novaPalavra.termo = termoPalavra
        novaPalavra.sinonimos.append(sinonimoPalavra)
        novaPalavra.classe = classePalavra

        main.append(novaPalavra)
        print('\n\033[32mPalavra cadastrada com sucesso!\033[0m')

    else:
        print('\n\033[31mErro! Palavra ja cadastrada!\033[0m')


def listar():
    num = 1
    if len(main) != 0:
        for x in main:
            print("\n\033[30mDados da palavra {}:".format(x.termo))
            sleep(0.3)
            print('A palavra {} possui {} caracteres.'.format(x.termo, len(x.termo)))
            sleep(0.3)
            print('Essa palavra possui {} sinonimos que sao: '.format(len(x.sinonimos)))
            sleep(0.3)
            for y in x.sinonimos:
                print('{}. {}'.format(num, y))
                num += 1
                sleep(0.2)
            print('Classe: {}\033[0m'.format(x.classe))
            sleep(0.2)
    else:
        sleep(0.3)
        print('\n\033[31mNenhuma palavra cadastrada!\033[0m')
        sleep(0.2)


def novoSinonimo():
    palavra = input('Digite a palavra que deseja adicionar um novo sinonimo: ').capitalize()

    for x in main:
        if palavra == x.termo:

            print('\n\033[30mEsse termo ja tem os seguintes sinonimos cadastrados: \n{}\n\033[0m'.format(x.sinonimos))

            novosin = input('Digite o novo sinonimo: ').capitalize()
            x.sinonimos.append(novosin)

            sleep(0.3)
            print('\n\033[32mSinonimo adicionado com sucesso!\033[0m')
            sleep(0.2)

        else:
            sleep(0.3)
            print('\n\033[31mPalavra nao encontrada!\033[0m')
            sleep(0.2)


def maisSinonimos():
    termoMaisSin = ''
    numSin = 0

    for x in main:
        if len(x.sinonimos) > numSin:
            numSin = len(x.sinonimos)
            termoMaisSin = x.termo

    print('O termo {} tem a maior quantidade de sinonimos, possuindo {} sinonimos.'.format(termoMaisSin, numSin))
    sleep(0.3)


def buscaPorClasse():
    num = 1
    existe = False
    classeBusca = input('Digite a classe desejada: ').capitalize()

    print('Foram encontradas as seguintes palavras da classe {}:'.format(classeBusca))
    for x in main:
        if x.classe == classeBusca:
            sleep(0.2)
            print('{}. {}'.format(num, x.termo))
            num += 1
            existe = True
            sleep(0.3)

    if existe is False:
        print('\n\033[31mNenhuma palavra dessa classe foi encontrada!\033[0m')


def excluirTermo():
    if len(main) != 0:
        foiEncontrado = False

        termoExcl = input('Digite o termo que deseja excluir: ').capitalize()
        for x in main:
            if x.termo == termoExcl:
                main.remove(x)
                foiEncontrado = True
                print('\n\033[32mTermo exluido com sucesso!\033[0m')

        if foiEncontrado is False:
            print('\n\033[31mTermo nao encontrado!\033[0m')
    else:
        print('\n\033[31mNenhuma palavra cadastrada!\033[0m')


def excluirSinonimo():
    foiEncontrado = False

    sinExcl = input('Digite o sinonimo que dejesa excluir: ').capitalize()
    if len(main) != 0:
        for x in main:
            for y in x.sinonimos:
                if y == sinExcl:
                    x.sinonimos.remove(y)
                    foiEncontrado = True
                    print('\n\033[32mSinonimo exluido com sucesso!\033[0m')

        if foiEncontrado is False:
            print('\n\033[31mSinonimo nao encontrado!\033[0m')
    else:
        print('\n\033[31mNenhuma palavra cadastrada!\033[0m')


while True:
    menu()
    op = int(input('\033[30mDigite a opcao desejada: \033[0m'))

    if op == 0:
        print('Ate logo!')
        break

    elif op == 1:
        cadastro()

    elif op == 2:
        listar()

    elif op == 3:
        novoSinonimo()

    elif op == 4:
        maisSinonimos()

    elif op == 5:
        buscaPorClasse()

    elif op == 6:
        excluirTermo()

    elif op == 7:
        excluirSinonimo()

    else:
        print('Selecione uma opcao disponivel!')
