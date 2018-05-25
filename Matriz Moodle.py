def matrizImparPar():
    matriz = []

    for i in range(1, 9):
        linha = []

        for j in range(1, 9):
            if i % 2 == 0:
                valor = 1

            else:
                valor = 0

            linha.append(valor)

        matriz.append(linha)

    for i in range(8):
        print(matriz[i])


matrizImparPar()
print("="*55)
