import tkinter as tk
from tkinter import messagebox

def calcular_valores():
    try:
        num_itens = int(entrada_num_itens.get())
        if num_itens <= 0:
            messagebox.showerror("Erro", "Por favor, insira um número de itens positivo.")
            return
        valores = []
        resultados = []
        for i in range(num_itens):
            valor = float(entradas_valores[i].get().replace(',', '.'))
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

def criar_entradas_valores():
    for widget in frame_valores.winfo_children():
        widget.destroy()
    num_itens = int(entrada_num_itens.get())
    entradas_valores.clear()
    for i in range(num_itens):
        label_valor = tk.Label(frame_valores, text=f"Item {i+1}:", font=("Arial", 12))
        label_valor.pack()
        entrada_valor = tk.Entry(frame_valores, font=("Arial", 12), width=10)
        entrada_valor.pack()
        entradas_valores.append(entrada_valor)

def atualizar_entradas_valores():
    criar_entradas_valores()

janela = tk.Tk()
janela.title("Calculadora de Valores")

# Criação do frame superior
frame_superior = tk.Frame(janela, bg="#f0f0f0")
frame_superior.pack(padx=10, pady=10)

# Criação do label e entrada para o número de itens
label_num_itens = tk.Label(frame_superior, text="Quantos itens você deseja calcular?", font=("Arial", 12))
label_num_itens.pack()
entrada_num_itens = tk.Entry(frame_superior, font=("Arial", 12), width=5)
entrada_num_itens.pack()

# Criação do botão para atualizar as entradas de valores
botao_atualizar = tk.Button(frame_superior, text="Atualizar", command=atualizar_entradas_valores, font=("Arial", 12), bg="#4CAF50", fg="#ffffff", relief="flat")
botao_atualizar.pack(pady=5)

# Criação do frame para as entradas de valores
frame_valores = tk.Frame(janela, bg="#f0f0f0")
frame_valores.pack(padx=10, pady=10)

# Criação do botão para calcular os valores
botao_calcular = tk.Button(janela, text="Calcular", command=calcular_valores, font=("Arial", 12), bg="#2196F3", fg="#ffffff", relief="flat")
botao_calcular.pack(pady=10)

# Criação do frame para o resultado
frame_resultado = tk.Frame(janela, bg="#f0f0f0")
frame_resultado.pack(padx=10, pady=10)

# Criação do texto para o resultado
texto_resultados = tk.Text(frame_resultado, font=("Arial", 12), width=60, height=10)
texto_resultados.pack()

entradas_valores = []

janela.mainloop()