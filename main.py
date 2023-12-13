from tkinter import *
from tkinter.ttk import Combobox

#combobox para ver se o contato é preferencial ou nâo
#um botao para adicionar o contato e outro pra limpar o formulário  

#A interface deve conter campos para inserir nome, número de telefone, e-mail e um campo de seleção se o contato é preferencial ou não. Um botão para adicionar o contato e outro botão para limpar o formulário.

#Adicione um recurso para visualizar a lista de contatos na interface.

#def para validação dos valores
def validacao():
    nome = inputNome.get()
    numero = int(inputNumero.get())
    email = inputEmail.get() 
    preferencial = comboboxPreferencial.get()
    if nome  ==  "":
        text_box.insert("Nome vazio")
    elif numero != int:
        text_box.insert("Digite um número inteiro")
    elif email 






window = Tk()
window.title("Sistema de Agenda de Contatos")
window.geometry("600x300")

#nome

lblNome = Label(window, text="Nome:")
lblNome.pack()
inputNome = Entry(window, text="Nome", bd=2)
inputNome.pack()

#numero

lblNumero = Label(window, text="Número de telefone:")
lblNumero.pack()
inputNumero = Entry(window, text="Numero", bd=2)
inputNumero.pack()

#email

lblEmail = Label(window, text="Endereço de e-mail:")
lblEmail.pack()
inputEmail = Entry(window, text="Email", bd=2)
inputEmail.pack()

#preferencial

v0 = StringVar()
valores = ("Sim", "Nâo")
comboboxPreferencial = Combobox(window, values=valores)
comboboxPreferencial.pack()

#Botões de enviar e limpar e ver contatos
btn = Button(window,text="Enviar", command="")
btn.pack()

btn2 = Button(window,text="Limpar", command='')
btn2.pack()

btn3 = Button(window,text="Ver contatos",command='')
btn3.pack()

text_box = Text()



window.mainloop()
