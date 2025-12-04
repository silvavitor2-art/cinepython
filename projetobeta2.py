import tkinter as tk
from tkinter import messagebox


# ----------------------------
# LEITURA DOS FILMES DO ARQUIVO
# ----------------------------
def carregar_filmes():
    filmes = {}
    try:
        with open("filmes.txt.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    filme, horarios = linha.split("|")
                    filmes[filme] = horarios.split(",")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo 'filmes.txt.txt' não encontrado!")
    return filmes


filmes = carregar_filmes()

filme_selecionado = ""
horario_selecionado = ""
assento_selecionado = ""


# ----------------------------
# CONTROLE DE TELAS
# ----------------------------
def mostrar_catalogo():
    frame_menu.pack_forget()
    frame_catalogo.pack()

def voltar_menu():
    frame_catalogo.pack_forget()
    frame_horarios.pack_forget()
    frame_assentos.pack_forget()
    frame_pagamento.pack_forget()
    frame_menu.pack()

def voltar_catalogo():
    frame_horarios.pack_forget()
    frame_catalogo.pack()

def voltar_horarios():
    frame_assentos.pack_forget()
    frame_horarios.pack()

def voltar_assentos():
    frame_pagamento.pack_forget()
    frame_assentos.pack()


# ----------------------------
# MOSTRAR HORÁRIOS
# ----------------------------
def mostrar_horarios():
    global filme_selecionado

    selecionado = lista_filmes.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um filme!")
        return

    filme_selecionado = lista_filmes.get(selecionado)
    horarios = filmes[filme_selecionado]

    frame_catalogo.pack_forget()
    frame_horarios.pack()

    titulo_horarios.config(text=f"🎬 {filme_selecionado}")

    lista_horarios.delete(0, tk.END)
    for h in horarios:
        lista_horarios.insert(tk.END, h)


# ----------------------------
# IR PARA ASSENTOS
# ----------------------------
def ir_assentos():
    global horario_selecionado

    selecionado = lista_horarios.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um horário!")
        return

    horario_selecionado = lista_horarios.get(selecionado)

    frame_horarios.pack_forget()
    frame_assentos.pack()

    resumo_assento.config(text=f"{filme_selecionado} - {horario_selecionado}")
    criar_assentos()


# ----------------------------
# CRIAR ASSENTOS
# ----------------------------
def criar_assentos():
    for widget in frame_assentos_botoes.winfo_children():
        widget.destroy()

    for i in range(5):
        for j in range(5):
            assento = f"{chr(65+i)}{j+1}"
            botao = tk.Button(
                frame_assentos_botoes,
                text=assento,
                width=4,
                command=lambda a=assento: selecionar_assento(a)
            )
            botao.grid(row=i, column=j, padx=5, pady=5)


# ----------------------------
# SELECIONAR ASSENTO
# ----------------------------
def selecionar_assento(assento):
    global assento_selecionado
    assento_selecionado = assento
    ir_pagamento()


# ----------------------------
# IR PARA PAGAMENTO
# ----------------------------
def ir_pagamento():
    frame_assentos.pack_forget()
    frame_pagamento.pack()

    resumo_pagamento.config(
        text=f"Filme: {filme_selecionado}\nHorário: {horario_selecionado}\nAssento: {assento_selecionado}\nValor: R$ 20,00"
    )


# ----------------------------
# CONFIRMAR PAGAMENTO
# ----------------------------
def confirmar_pagamento():
    forma = forma_pagamento.get()

    if forma == "":
        messagebox.showwarning("Aviso", "Escolha a forma de pagamento!")
        return

    messagebox.showinfo(
        "Compra Confirmada",
        f"Compra realizada com sucesso!\n\n"
        f"Filme: {filme_selecionado}\n"
        f"Horário: {horario_selecionado}\n"
        f"Assento: {assento_selecionado}\n"
        f"Pagamento: {forma}"
    )

    voltar_menu()


# ----------------------------
# JANELA PRINCIPAL
# ----------------------------
janela = tk.Tk()
janela.title("Cinema IF - Sistema de Ingressos")
janela.geometry("450x480")


# ----------------------------
# MENU
# ----------------------------
frame_menu = tk.Frame(janela)

tk.Label(frame_menu, text="🎬 Bem-vindo ao Cinema IF", font=("Arial", 16)).pack(pady=20)

tk.Button(frame_menu, text="Ver Catálogo", width=20, command=mostrar_catalogo).pack(pady=10)
tk.Button(frame_menu, text="Sair", width=20, command=janela.quit).pack(pady=10)

frame_menu.pack()


# ----------------------------
# CATÁLOGO
# ----------------------------
frame_catalogo = tk.Frame(janela)

tk.Label(frame_catalogo, text="🎬 Escolha um Filme", font=("Arial", 14)).pack(pady=10)

lista_filmes = tk.Listbox(frame_catalogo, width=40)
lista_filmes.pack(pady=10)

for filme in filmes:
    lista_filmes.insert(tk.END, filme)

tk.Button(frame_catalogo, text="Ver Horários", width=20, command=mostrar_horarios).pack(pady=5)
tk.Button(frame_catalogo, text="⬅ Voltar", width=20, command=voltar_menu).pack(pady=10)


# ----------------------------
# HORÁRIOS
# ----------------------------
frame_horarios = tk.Frame(janela)

titulo_horarios = tk.Label(frame_horarios, text="🎬 Horários", font=("Arial", 14))
titulo_horarios.pack(pady=10)

lista_horarios = tk.Listbox(frame_horarios, width=30)
lista_horarios.pack(pady=10)

tk.Button(frame_horarios, text="Escolher Assento", width=25, command=ir_assentos).pack(pady=5)
tk.Button(frame_horarios, text="⬅ Voltar", width=25, command=voltar_catalogo).pack(pady=10)


# ----------------------------
# ASSENTOS
# ----------------------------
frame_assentos = tk.Frame(janela)

tk.Label(frame_assentos, text="🎟️ Escolha um Assento", font=("Arial", 14)).pack(pady=10)

resumo_assento = tk.Label(frame_assentos, text="")
resumo_assento.pack()

frame_assentos_botoes = tk.Frame(frame_assentos)
frame_assentos_botoes.pack(pady=10)

tk.Button(frame_assentos, text="⬅ Voltar", width=25, command=voltar_horarios).pack(pady=10)


# ----------------------------
# PAGAMENTO
# ----------------------------
frame_pagamento = tk.Frame(janela)

tk.Label(frame_pagamento, text="💳 Pagamento", font=("Arial", 14)).pack(pady=10)

resumo_pagamento = tk.Label(frame_pagamento, text="")
resumo_pagamento.pack(pady=10)

forma_pagamento = tk.StringVar()

tk.Radiobutton(frame_pagamento, text="Pix", variable=forma_pagamento, value="Pix").pack()
tk.Radiobutton(frame_pagamento, text="Cartão", variable=forma_pagamento, value="Cartão").pack()
tk.Radiobutton(frame_pagamento, text="Dinheiro", variable=forma_pagamento, value="Dinheiro").pack()

tk.Button(frame_pagamento, text="Confirmar Pagamento", width=25, command=confirmar_pagamento).pack(pady=10)
tk.Button(frame_pagamento, text="⬅ Voltar", width=25, command=voltar_assentos)

janela.mainloop()