import tkinter as tk
from tkinter import messagebox

def calcular_valores():
    try:
        num_itens = int(entrada_num_itens.get())
        if num_itens <= 0:
            messagebox.showerror("Erro", "Por favor, insira um número de itens positivo.")
            return
        valores = []
        for i in range(num_itens):
            valor = float(entradas_valores[i].get().replace(',', '.'))
            if valor < 0:
                messagebox.showerror("Erro", "Por favor, insira um valor não negativo.")
                return
            valores.append(valor)
        
        porcentagens = []
        if var_porcentagem_3_0.get():
            porcentagens.append(3.0)
        if var_porcentagem_2_8.get():
            porcentagens.append(2.8)
        if var_porcentagem_2_7.get():
            porcentagens.append(2.7)
        if var_porcentagem_2_5.get():
            porcentagens.append(2.5)
        if var_porcentagem_2_25.get():
            porcentagens.append(2.25)
        
        if not porcentagens:
            messagebox.showerror("Erro", "Por favor, selecione pelo menos uma porcentagem.")
            return
        
        texto_resultados.config(state="normal")  # Habilita o campo de resultados
        texto_resultados.delete(1.0, tk.END)
        texto_resultados.insert(tk.END, "\t\t\tTabela de Preços:\n")
        texto_resultados.insert(tk.END, "---------------------------------------------------------------\n")
        texto_resultados.insert(tk.END, "Item | Valor Inserido | ")
        for porcentagem in porcentagens:
            texto_resultados.insert(tk.END, f"Valor x {porcentagem} | ")
        texto_resultados.insert(tk.END, "\n")
        texto_resultados.insert(tk.END, "---------------------------------------------------------------\n")
        
        for i, valor in enumerate(valores):
            texto_resultados.insert(tk.END, f"{i+1}\t{valor:.2f}\t")
            for porcentagem in porcentagens:
                texto_resultados.insert(tk.END, f"{valor * porcentagem:.2f}\t")
            texto_resultados.insert(tk.END, "\n")
        
        texto_resultados.config(state="disabled")  # Desabilita o campo de resultados
        texto_resultados.config(edit_modified=False)  # Desabilita a edição do campo de resultados
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
botao_calcular.pack(fill="x", pady=5)

frame_resultado = tk.Frame(janela, bg="#f0f0f0")
frame_resultado.pack(fill="both", expand=True, padx=10, pady=10)

barra_rolagem_resultado = tk.Scrollbar(frame_resultado)
barra_rolagem_resultado.pack(side="right", fill="y")

texto_resultados = tk.Text(frame_resultado, yscrollcommand=barra_rolagem_resultado.set)
texto_resultados.pack(fill="both", expand=True)
texto_resultados.config(state="disabled")

barra_rolagem_resultado.config(command=texto_resultados.yview)

frame_porcentagens = tk.Frame(janela, bg="#f0f0f0")
frame_porcentagens.pack(fill="x", padx=10, pady=10)

label_porcentagens = tk.Label(frame_porcentagens, text="Selecione as porcentagens:")
label_porcentagens.pack(fill="x")

var_porcentagem_3_0 = tk.BooleanVar()
var_porcentagem_2_8 = tk.BooleanVar()
var_porcentagem_2_7 = tk.BooleanVar()
var_porcentagem_2_5 = tk.BooleanVar()
var_porcentagem_2_25 = tk.BooleanVar()

checkbox_porcentagem_3_0 = tk.Checkbutton(frame_porcentagens, text="3.0%", variable=var_porcentagem_3_0)
checkbox_porcentagem_3_0.pack(fill="x")

checkbox_porcentagem_2_8 = tk.Checkbutton(frame_porcentagens, text="2.8%", variable=var_porcentagem_2_8)
checkbox_porcentagem_2_8.pack(fill="x")

checkbox_porcentagem_2_7 = tk.Checkbutton(frame_porcentagens, text="2.7%", variable=var_porcentagem_2_7)
checkbox_porcentagem_2_7.pack(fill="x")

checkbox_porcentagem_2_5 = tk.Checkbutton(frame_porcentagens, text="2.5%", variable=var_porcentagem_2_5)
checkbox_porcentagem_2_5.pack(fill="x")

checkbox_porcentagem_2_25 = tk.Checkbutton(frame_porcentagens, text="2.25%", variable=var_porcentagem_2_25)
checkbox_porcentagem_2_25.pack(fill="x")

entradas_valores = []

janela.mainloop()