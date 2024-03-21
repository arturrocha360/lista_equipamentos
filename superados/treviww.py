import tkinter as tk
from tkinter import ttk

root = tk.Tk()


tree = ttk.Treeview(root, columns=("Col1", "Col2", "Col3"))
tree.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
# Definindo o tamanho do Treeview
#tree.config(height=3)  # Define a altura do Treeview

# Adicionando cabeçalhos
tree.heading("#0", text="Nome")
tree.heading("Col1", text="Idade")
tree.heading("Col2", text="Sexo")

# Adicionando dados
tree.insert("", "end", text="Linha 1", values=("João", 30, "Masculino"))
tree.insert("", "end", text="Linha 2", values=("Maria", 25, "Feminino"))

tree.pack(fill=tk.BOTH)
root.mainloop()
