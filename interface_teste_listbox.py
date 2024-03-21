import tkinter as tk

def on_select(event):
    index = listbox.curselection()[0]
    selected_item = listbox.get(index)
    label.config(text="Item selecionado: " + selected_item)

def print_selected():
    index = listbox.curselection()[0]
    selected_item = listbox.get(index)
    print( selected_item)

window = tk.Tk()
window.title("Listbox Example")

listbox = tk.Listbox(window)
listbox.grid(row=0, column=0, padx=10, pady=10)

for item in ['Amador Bueno', 'Antônio João', 'Autódromo', 'Barueri', 'Berrini', 'Brás', 'Carapicuíba', 'Ceasa', 'Cidade Jardim', 'Cidade Universitária', 'Comandante Sampaio', 'Domingos de Moraes', 'Engenheiro Cardoso', 'General Miguel Costa', 'Grajaú', 'Granja Julieta', 'Hebraica–Rebouças', 'Imperatriz Leopoldina', 'Itapevi', 'Jandira', 'Jardim Belval', 'Jardim Silveira', 'João Dias', 'Jurubatuba', 'Júlio Prestes', 'Lapa', 'Mendes–Vila Natal', 'Morumbi', 'Osasco', 'Palmeiras–Barra Funda', 'Patio Presidente Altino', 'Pinheiros', 'Presidente Altino', 'Primavera–Interlagos', 'Quitaúna', 'Sagrado Coração', 'Santa Rita', 'Santa Terezinha', 'Santo Amaro', 'Socorro', 'Varginha', 'Vila Lobos–Jaguaré', 'Vila Olímpia']:
    listbox.insert(tk.END, item)




label = tk.Label(window, text="")
label.grid(row=1, column=0, padx=10, pady=10)

listbox.bind('<<ListboxSelect>>', on_select)

button = tk.Button(window, text="Imprimir Selecionado", command=print_selected)
button.grid(row=2, column=0, padx=10, pady=10)

window.mainloop()
