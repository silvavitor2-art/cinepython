import tkinter as tk
from tkinter import messagebox

filmes = {
    "Homem-Aranha": ["14:00", "16:30", "19:00"],
    "Toy Story": ["13:00", "15:00", "17:00"],
    "Vingadores": ["18:00", "20:30"],
    "Interestelar": ["16:00", "19:30"]
}


def mostrar_catalogo():
    frame_menu.pack_forget()
    frame_catalogo.pack()

def voltar_menu():
    frame_catalogo.pack_forget()
    frame_horarios.pack_forget()
    frame_menu.pack()

def voltar_catalogo():
    frame_horarios.pack_forget()
    frame_catalogo.pack()

def comprar_ingresso():
    messagebox.showinfo("Compra", "Função de compra em desenvolvimento! 🎟️")


def mostrar_horarios():
    selecionado = lista_filmes.curselection()

    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um filme primeiro!")
        return

    filme = lista_filmes.get(selecionado)
    horarios = filmes[filme]

    frame_catalogo.pack_forget()
    frame_horarios.pack()

    titulo_horarios.config(text=f"🎬 {filme}")

    lista_horarios.delete(0, tk.END)
    for h in horarios:
        lista_horarios.insert(tk.END, h)


janela = tk.Tk()
janela.title("Cinema IF - Sistema de Ingressos")
janela.geometry("400x400")


frame_menu = tk.Frame(janela)

titulo = tk.Label(frame_menu, text="🎬 Bem-vindo ao Cinema IF", font=("Arial", 16))
titulo.pack(pady=20)

botao_catalogo = tk.Button(frame_menu, text="Ver Catálogo", width=20, command=mostrar_catalogo)
botao_catalogo.pack(pady=10)

botao_comprar = tk.Button(frame_menu, text="Comprar Ingresso", width=20, command=comprar_ingresso)
botao_comprar.pack(pady=10)

botao_sair = tk.Button(frame_menu, text="Sair", width=20, command=janela.quit)
botao_sair.pack(pady=10)

frame_menu.pack()


frame_catalogo = tk.Frame(janela)

titulo_catalogo = tk.Label(frame_catalogo, text="🎬 Escolha um Filme", font=("Arial", 14))
titulo_catalogo.pack(pady=10)

lista_filmes = tk.Listbox(frame_catalogo, width=40)
lista_filmes.pack(pady=10)

for filme in filmes:
    lista_filmes.insert(tk.END, filme)

botao_ver_horarios = tk.Button(
    frame_catalogo, text="Ver Horários", width=20, command=mostrar_horarios
)
botao_ver_horarios.pack(pady=5)

botao_voltar_menu = tk.Button(
    frame_catalogo, text="⬅ Voltar ao Menu", width=20, command=voltar_menu
)
botao_voltar_menu.pack(pady=10)


frame_horarios = tk.Frame(janela)

titulo_horarios = tk.Label(frame_horarios, text="🎬 Horários", font=("Arial", 14))
titulo_horarios.pack(pady=10)

lista_horarios = tk.Listbox(frame_horarios, width=30)
lista_horarios.pack(pady=10)

botao_comprar_horario = tk.Button(
    frame_horarios, text="Comprar Nesse Horário", width=25, command=comprar_ingresso
)
botao_comprar_horario.pack(pady=5)

botao_voltar_catalogo = tk.Button(
    frame_horarios, text="⬅ Voltar ao Catálogo", width=25, command=voltar_catalogo
)
botao_voltar_catalogo.pack(pady=10)


janela.mainloop()
