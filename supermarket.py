import tkinter as tk
from tkinter import messagebox
import sqlite3

class SupermercadoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cadastro de Produtos")

        self.label_nome = tk.Label(master, text="Nome:")
        self.label_nome.grid(row=0, column=0)

        self.entry_nome = tk.Entry(master)
        self.entry_nome.grid(row=0, column=1)

        self.label_preco = tk.Label(master, text="Preço:")
        self.label_preco.grid(row=1, column=0)

        self.entry_preco = tk.Entry(master)
        self.entry_preco.grid(row=1, column=1)

        self.label_quantidade = tk.Label(master, text="Quantidade:")
        self.label_quantidade.grid(row=2, column=0)

        self.entry_quantidade = tk.Entry(master)
        self.entry_quantidade.grid(row=2, column=1)

        self.button_cadastrar = tk.Button(master, text="Cadastrar", command=self.cadastrar)
        self.button_cadastrar.grid(row=3, column=0, columnspan=2, pady=10)

        self.button_listar = tk.Button(master, text="Listar Produtos", command=self.listar_produtos)
        self.button_listar.grid(row=4, column=0, columnspan=2, pady=10)

        self.connection = sqlite3.connect("produtos.db")
        self.create_table()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                            id INTEGER PRIMARY KEY,
                            nome TEXT NOT NULL,
                            preco REAL NOT NULL,
                            quantidade INTEGER NOT NULL
                          )''')
        self.connection.commit()

    def cadastrar(self):
        nome = self.entry_nome.get()
        preco = float(self.entry_preco.get())
        quantidade = int(self.entry_quantidade.get())

        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)", (nome, preco, quantidade))
        self.connection.commit()

        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso.")

        self.entry_nome.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)

    def listar_produtos(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

        if not produtos:
            messagebox.showinfo("Aviso", "Nenhum produto cadastrado.")
        else:
            lista_produtos = "Lista de Produtos:\n"
            for produto in produtos:
                lista_produtos += f"Nome: {produto[1]} - Preço: R${produto[2]} - Quantidade: {produto[3]}\n"
            messagebox.showinfo("Produtos", lista_produtos)


if __name__ == "__main__":
    root = tk.Tk()
    gui = SupermercadoGUI(root)
    root.mainloop()