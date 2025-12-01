import tkinter as tk


def abrir_tela_filmes():
    data_selecionada = lista_datas.get(lista_datas.curselection())
    print("Data selecionada:", data_selecionada)
    


janela = tk.Tk()
janela.title("Cinema - Escolher Data")
janela.geometry("500x400")



tk.Label(janela, text="escolha a data:", font=("Arial", 12)).pack(pady=0)

lista_datas = tk.Listbox(janela,  height=5, width=20)
lista_datas.pack()
 

datas = ["10/03/2025", "11/03/2025", "12/03/2025", "13/03/2025", "14/03/2025"]
for d in datas:
    lista_datas.insert(tk.END, d)

tk.Button(janela, text="Próximo", command=abrir_tela_filmes).pack(pady=10)

janela.mainloop()