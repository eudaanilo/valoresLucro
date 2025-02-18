def calcular_valores():

    num_itens = int(input("Quantos itens você deseja calcular? "))

    valores = []

    for i in range(num_itens):
        valor = float(input(f"Digite o valor do item {i+1}: "))
        valores.append(valor)

    fatores = [2.7, 2.5, 2.25]
    resultados = []

    for valor in valores:
        resultado = []
        for fator in fatores:
            resultado.append(valor * fator)
        resultados.append(resultado)

    print("\nTabela de Valores:")
    print("------------------------")
    print("Item\tValor Inserido\tValor x 2.7\tValor x 2.5\tValor x 2.25")
    print("------------------------")

    for i, (valor, resultado) in enumerate(zip(valores, resultados)):
        print(f"{i+1}\t{valor:.2f}\t\t{resultado[0]:.2f}\t\t{resultado[1]:.2f}\t\t{resultado[2]:.2f}")

calcular_valores()