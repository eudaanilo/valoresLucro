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
        texto_resultados.insert(tk.END, "\t\t\tTabela de Preços:\n")
        texto_resultados.insert(tk.END, "---------------------------------------------------------------\n")
        texto_resultados.insert(tk.END, "Item | Valor Inserido | Valor x 2.7 | Valor x 2.5 | Valor x 2.25\n")
        texto_resultados.insert(tk.END, "---------------------------------------------------------------\n")
        for i, (valor, resultado) in enumerate(zip(valores, resultados)):
            texto_resultados.insert(tk.END, f"{i+1}\t{valor:.2f}\t\t{resultado[0]:.2f}\t\t{resultado[1]:.2f}\t\t{resultado[2]:.2f}\n")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

def criar_entradas_valores(event=None):
    for widget in frame_entradas_valores.winfo_children():
        widget.destroy()
    num_itens = int(entrada_num_itens.get())
    entradas_valores.clear()
    for i in range(num_itens):
        label_valor = tk.Label(frame_entradas_valores, text=f"Item {i+1}:")
        label_valor.pack(fill="x")
        entrada_valor = tk.Entry(frame_entradas_valores)
        entrada_valor.pack(fill="x")
        entradas_valores.append(entrada_valor)
    frame_entradas_valores.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def atualizar_entradas_valores():
    criar_entradas_valores()

janela = tk.Tk()
janela.title("Calculadora de Valores")

frame_superior = tk.Frame(janela, bg="#f0f0f0")
frame_superior.pack(fill="x", padx=10, pady=10)

label_num_itens = tk.Label(frame_superior, text="Quantos itens você deseja calcular?")
label_num_itens.pack(fill="x")
entrada_num_itens = tk.Entry(frame_superior)
entrada_num_itens.pack(fill="x")
entrada_num_itens.bind("<Return>", criar_entradas_valores)

botao_atualizar = tk.Button(frame_superior, text="Atualizar", command=atualizar_entradas_valores, bg="#4CAF50", fg="#ffffff", relief="flat")
botao_atualizar.pack(fill="x", pady=5)

frame_valores = tk.Frame(janela, bg="#f0f0f0")
frame_valores.pack(fill="both", expand=True, padx=10, pady=10)

barra_rolagem = tk.Scrollbar(frame_valores)
barra_rolagem.pack(side="right", fill="y")

canvas = tk.Canvas(frame_valores, yscrollcommand=barra_rolagem.set)
canvas.pack(side="left", fill="both", expand=True)
barra_rolagem.config(command=canvas.yview)

frame_entradas_valores = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame_entradas_valores, anchor='nw')

botao_calcular = tk.Button(janela, text="Calcular", command=calcular_valores, bg="#2196F3", fg="#ffffff", relief="flat")
botao_calcular.pack(fill="x", pady=10)

frame_resultado = tk.Frame(janela, bg="#f0f0f0")
frame_resultado.pack(fill="both", expand=True, padx=10, pady=10)

barra_rolagem_resultado = tk.Scrollbar(frame_resultado)
barra_rolagem_resultado.pack(side="right", fill="y")

texto_resultados = tk.Text(frame_resultado, yscrollcommand=barra_rolagem_resultado.set)
texto_resultados.pack(fill="both", expand=True)

barra_rolagem_resultado.config(command=texto_resultados.yview)

entradas_valores = []

janela.mainloop()