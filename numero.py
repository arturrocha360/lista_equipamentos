import tkinter as tk

# Função chamada quando um item é selecionado no listbox
def on_select(event):
   
    # Verifica se há alguma seleção no listbox
    if listbox.curselection():
        # Se houver uma seleção, habilita o botão
        button.config(state=tk.NORMAL)
    else:
        # Se não houver seleção, desabilita o botão
        button.config(state=tk.DISABLED)

# Função chamada quando o botão é clicado
def on_button_click():
    # Obtém o índice do item selecionado no listbox
    selected_index = listbox.curselection()
    if selected_index:
        # Obtém o texto do item selecionado no listbox
        selected_item = listbox.get(selected_index)
        # Imprime o item selecionado (pode ser substituído por lógica para avançar)
        print("Item selecionado:", selected_item)

# Criação da janela principal
root = tk.Tk()
root.title("Seleção de Item")

# Criação do listbox
listbox = tk.Listbox(root)
listbox.pack(padx=10, pady=10)
# Insere alguns itens no listbox
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")
# Associa a função on_select ao evento de seleção no listbox
listbox.bind('<<ListboxSelect>>', on_select)

# Criação do botão
button = tk.Button(root, text="Avançar", state=tk.DISABLED, command=on_button_click)
button.pack(pady=10)

# Inicia o loop principal da aplicação
root.mainloop()
