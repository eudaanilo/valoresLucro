import tkinter as tk
from tkinter import messagebox

def calcular_valores():
    try:
        num_itens = int(entrada_num_itens.get())
        valores = []
        resultados = []

        for i in range(num_itens):
            valor = float(entradas_valores[i].get())
            valores.append(valor)

        fatores = [2.7, 2.5, 2.25]

        for valor in valores:
            resultado = []
            for fator in fatores:
                resultado.append(valor * fator)
            resultados.append(resultado)

        texto_resultados.delete(1.0, tk.END)
        texto_resultados.insert(tk.END, "Tabela de Valores:\n")
        texto_resultados.insert(tk.END, "------------------------\n")
        texto_resultados.insert(tk.END, "Item\tValor Inserido\tValor x 2.7\tValor x 2.5\tValor x 2.25\n")
        texto_resultados.insert(tk.END, "------------------------\n")

        for i, (valor, resultado) in enumerate(zip(valores, resultados)):
            texto_resultados.insert(tk.END, f"{i+1}\t{valor:.2f}\t\t{resultado[0]:.2f}\t\t{resultado[1]:.2f}\t\t{resultado[2]:.2f}\n")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

janela = tk.Tk()
janela.title("Calculadora de Valores")

label_num_itens = tk.Label(janela, text="Quantos itens você deseja calcular?")
label_num_itens.pack()

entrada_num_itens = tk.Entry(janela)
entrada_num_itens.pack()

botao_calcular = tk.Button(janela, text="Calcular", command=calcular_valores)
botao_calcular.pack()

label_valores = tk.Label(janela, text="Insira os valores dos itens:")
label_valores.pack()

entradas_valores = []

def criar_entradas_valores():
    for widget in frame_valores.winfo_children():
        widget.destroy()

    num_itens = int(entrada_num_itens.get())
    entradas_valores.clear()

    for i in range(num_itens):
        label_valor = tk.Label(frame_valores, text=f"Item {i+1}:")
        label_valor.pack()
        entrada_valor = tk.Entry(frame_valores)
        entrada_valor.pack()
        entradas_valores.append(entrada_valor)

frame_valores = tk.Frame(janela)
frame_valores.pack()

botao_criar_entradas = tk.Button(janela, text="Criar entradas para valores", command=criar_entradas_valores)
botao_criar_entradas.pack()

texto_resultados = tk.Text(janela)
texto_resultados.pack()

janela.mainloop()