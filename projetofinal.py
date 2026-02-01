
import tkinter as tk
from tkinter import messagebox #### lembra de baixar as bibliotecas pelor amor de Deus 
from PIL import Image, ImageTk
import os 

CAMINHO_DADOS = "dados"
CAMINHO_IMAGENS = "imagens"

# LEITURA DOS ARQUIVOS

def carregar_filmes():
    filmes = {}
    try:
        with open(os.path.join(CAMINHO_DADOS, "filmes.txt"), "r", encoding="utf-8") as arq:
            for linha in arq:
                filme, horarios = linha.strip().split("|")
                filmes[filme] = [h.strip() for h in horarios.split(",")]
    except:
        messagebox.showerror("Erro", "Erro ao carregar filmes.txt")
    return filmes


def carregar_assentos():
    assentos = []
    try:
        with open(os.path.join(CAMINHO_DADOS, "assentos.txt"), "r", encoding="utf-8") as arq:
            for linha in arq:
                assentos.append([a.strip() for a in linha.split(",")])
    except:
        messagebox.showerror("Erro", "Erro ao carregar assentos.txt")
    return assentos


def carregar_pagamentos():
    formas = []
    try:
        with open(os.path.join(CAMINHO_DADOS, "pagamentos.txt"), "r", encoding="utf-8") as arq:
            for linha in arq:
                formas.append(linha.strip())
    except:
        messagebox.showerror("Erro", "Erro ao carregar pagamentos.txt")
    return formas


filmes = carregar_filmes()
assentos_matriz = carregar_assentos()
formas_pagamento_lista = carregar_pagamentos()


# VARIÁVEIS GERAIS

filme_selecionado = ""
horario_selecionado = ""
assentos_selecionados = []
tipo_ingresso = ""
VALOR_INTEIRA = 20
VALOR_MEIA = 10

# CONTROLE DE TELAS

def mostrar_catalogo():
    frame_menu.pack_forget()
    frame_catalogo.pack()

def voltar_menu():
    for f in [frame_catalogo, frame_horarios, frame_assentos, frame_pagamento]:
        f.pack_forget()
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

# HORÁRIOS

def mostrar_horarios():
    global filme_selecionado
    sel = lista_filmes.curselection()

    if not sel:
        messagebox.showwarning("Aviso", "Selecione um filme!")
        return

    filme_selecionado = lista_filmes.get(sel)
    lista_horarios.delete(0, tk.END)

    for h in filmes[filme_selecionado]:
        lista_horarios.insert(tk.END, h)

    frame_catalogo.pack_forget()
    frame_horarios.pack()
    titulo_horarios.config(text=filme_selecionado)


# ASSENTOS

def ir_assentos():
    global horario_selecionado, assentos_selecionados
    sel = lista_horarios.curselection()

    if not sel:
        messagebox.showwarning("Aviso", "Selecione um horário!")
        return

    horario_selecionado = lista_horarios.get(sel)
    assentos_selecionados.clear()

    criar_assentos()
    frame_horarios.pack_forget()
    frame_assentos.pack()
    resumo_assento.config(text=f"{filme_selecionado} - {horario_selecionado}")


def criar_assentos():
    for w in frame_assentos_botoes.winfo_children():
        w.destroy()

    for i, linha in enumerate(assentos_matriz):
        for j, assento in enumerate(linha):
            btn = tk.Button(
                frame_assentos_botoes,
                text=assento,
                width=4,
                command=lambda a=assento: selecionar_assento(a)
            )
            btn.grid(row=i, column=j, padx=5, pady=5)


def selecionar_assento(assento):
    if assento in assentos_selecionados:
        assentos_selecionados.remove(assento)
    else:
        assentos_selecionados.append(assento)

    selecionados_label.config(
        text="Selecionados: " + ", ".join(assentos_selecionados)
    )



# PAGAMENTO

def ir_pagamento():
    global tipo_ingresso

    if not assentos_selecionados:
        messagebox.showwarning("Aviso", "Selecione ao menos um assento!")
        return

    tipo_ingresso = tipo_var.get()

    if tipo_ingresso == "":
        messagebox.showwarning("Aviso", "Selecione o tipo de ingresso!")
        return

    valor_unit = VALOR_MEIA if tipo_ingresso == "Meia" else VALOR_INTEIRA
    total = valor_unit * len(assentos_selecionados)

    resumo_pagamento.config(
        text=f"Filme: {filme_selecionado}\n"
             f"Horário: {horario_selecionado}\n"
             f"Assentos: {', '.join(assentos_selecionados)}\n"
             f"Ingresso: {tipo_ingresso}\n"
             f"Total: R$ {total}"
    )

    frame_assentos.pack_forget()
    frame_pagamento.pack()



# CONFIRMAR PAGAMENTO
def confirmar_pagamento():
    forma = forma_pagamento.get()

    if forma == "":
        messagebox.showwarning("Aviso", "Selecione a forma de pagamento!")
        return

    messagebox.showinfo(
        "Compra Concluída",
        "Compra realizada com sucesso!"
    )

    voltar_menu()

# JANELA PRINCIPAL

janela = tk.Tk()
janela.title("Cinepython")
janela.geometry("500x520")

# MENU

frame_menu = tk.Frame(janela)
imagem_logo = Image.open(os.path.join(CAMINHO_IMAGENS, "logo2.png"))
imagem_logo = imagem_logo.resize((200, 150))   
logo_tk = ImageTk.PhotoImage(imagem_logo)

label_logo = tk.Label(frame_menu, image=logo_tk)
label_logo.image = logo_tk   # evitar que a imagem seja apagada
label_logo.pack(pady=10)

tk.Label(frame_menu, text=" Cinepython", font=("Arial", 60), ).pack(pady=50)
tk.Button(frame_menu, text="Ver Catálogo", font=("arial",20), width=20, height=2, bg="#F60515" ,fg="white", command=mostrar_catalogo).pack(pady=50)
tk.Button(frame_menu, text="Sair", width=15,height=2, font=("arial",15), bg="lightgray", fg="white", command=janela.quit).pack(pady=10)
frame_menu.pack()

# CATÁLOGO

frame_catalogo = tk.Frame(janela)

# frame principal
frame_conteudo = tk.Frame(frame_catalogo)
frame_conteudo.pack(expand=True)

# CARREGAR IMAGENS

img1 = ImageTk.PhotoImage(
    Image.open(os.path.join(CAMINHO_IMAGENS, "interstellar.png")).resize((120, 180))
)

img2 = ImageTk.PhotoImage(
    Image.open(os.path.join(CAMINHO_IMAGENS, "toy.png")).resize((120, 180))
)

img3 = ImageTk.PhotoImage(
    Image.open(os.path.join(CAMINHO_IMAGENS, "spideer.png")).resize((120, 180))
)

img4 = ImageTk.PhotoImage(
    Image.open(os.path.join(CAMINHO_IMAGENS, "vinagadores.png")).resize((120, 180))
    )


lbl_img1 = tk.Label(frame_conteudo, image=img1)
lbl_img1.image = img1
lbl_img1.grid(row=0, column=0, padx=20, pady=10)

lbl_img2 = tk.Label(frame_conteudo, image=img2)
lbl_img2.image = img2
lbl_img2.grid(row=1, column=0, padx=20, pady=10)

frame_centro = tk.Frame(frame_conteudo)
frame_centro.grid(row=0, column=1, rowspan=2)

tk.Label(frame_centro, text="Escolha um Filme", font=("Arial", 14)).pack(pady=5)

lista_filmes = tk.Listbox(frame_centro, width=30, height=6)
lista_filmes.pack()

for f in filmes:
    lista_filmes.insert(tk.END, f)

tk.Button(frame_centro, text="Ver Horários", command=mostrar_horarios).pack(pady=5)
tk.Button(frame_centro, text="⬅ Voltar", command=voltar_menu).pack()

lbl_img3 = tk.Label(frame_conteudo, image=img3)
lbl_img3.image = img3
lbl_img3.grid(row=0, column=2, padx=20, pady=10)

lbl_img4 = tk.Label(frame_conteudo, image=img4)
lbl_img4.image = img4
lbl_img4.grid(row=1, column=2, padx=20, pady=10)

# HORÁRIOS

frame_horarios = tk.Frame(janela)
titulo_horarios = tk.Label(frame_horarios, font=("Arial", 14))
titulo_horarios.pack(pady=10)

lista_horarios = tk.Listbox(frame_horarios)
lista_horarios.pack()

tk.Button(frame_horarios, text="Escolher Assentos", command=ir_assentos).pack(pady=5)
tk.Button(frame_horarios, text="⬅ Voltar", command=voltar_catalogo).pack()

# ASSENTOS

frame_assentos = tk.Frame(janela)
tk.Label(frame_assentos, text="Escolha os Assentos", font=("Arial", 14)).pack()

resumo_assento = tk.Label(frame_assentos)
resumo_assento.pack()

frame_assentos_botoes = tk.Frame(frame_assentos)
frame_assentos_botoes.pack()

selecionados_label = tk.Label(frame_assentos, text="")
selecionados_label.pack()

# INGRESSOS

tk.Label(frame_assentos, text="Tipo de Ingresso:").pack()
tipo_var = tk.StringVar()
tk.Radiobutton(frame_assentos, text="Inteira", variable=tipo_var, value="Inteira").pack()
tk.Radiobutton(frame_assentos, text="Meia", variable=tipo_var, value="Meia").pack()

tk.Button(frame_assentos, text="Ir para Pagamento", command=ir_pagamento).pack(pady=5)
tk.Button(frame_assentos, text="⬅ Voltar", command=voltar_horarios).pack()

# PAGAMENTO

frame_pagamento = tk.Frame(janela)
tk.Label(frame_pagamento, text="Pagamento", font=("Arial", 14)).pack(pady=10)

resumo_pagamento = tk.Label(frame_pagamento)
resumo_pagamento.pack(pady=10)

forma_pagamento = tk.StringVar()
for forma in formas_pagamento_lista:
    tk.Radiobutton(frame_pagamento, text=forma, variable=forma_pagamento, value=forma).pack()

tk.Button(frame_pagamento, text="Confirmar Compra", command=confirmar_pagamento).pack(pady=10)
tk.Button(frame_pagamento, text="⬅ Voltar", command=voltar_assentos).pack()


janela.mainloop()
