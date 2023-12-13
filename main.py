from tkinter import *
from tkinter.ttk import Combobox
import math 

#combobox para ver se o contato é preferencial ou nâo
#um botao para adicionar o contato e outro pra limpar o formulário  

#A interface deve conter campos para inserir nome, número de telefone, e-mail e um campo de seleção se o contato é preferencial ou não. Um botão para adicionar o contato e outro botão para limpar o formulário.

#Adicione um recurso para visualizar a lista de contatos na interface.

#def para validação dos valores
def validacao():
    try:
        nome = inputNome.get()
        numero = int(inputNumero.get())
        email = inputEmail.get() 
        preferencial = comboboxPreferencial.get()
    except Exception as e:
        labelerrorgeral = Label(window,text='Ocorreu um erro! Preencha os dados corretamente.')
        labelerrorgeral.pack()
    if nome  ==  "":
        labelerrorgeral = Label(window,text='Ocorreu um erro! Preencha os dados corretamente.')
        labelerrorgeral.pack()
    if math.isnan(numero) == True: #ver dps quando o numero nn for nada
        labelerrorgeral = Label(window,text='Ocorreu um erro! Preencha os dados corretamente.')
        labelerrorgeral.pack()
    if email not in ["@","."]:
        labelerrorgeral = Label(window,text='Ocorreu um erro! Preencha os dados corretamente.')
        labelerrorgeral.pack()
    if preferencial == "":
        labelerrorgeral = Label(window,text='Ocorreu um erro! Preencha os dados corretamente.')
        labelerrorgeral.pack()
    





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
inputNumero = Entry(window, bd=2)
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
btn = Button(window,text="Enviar", command=validacao)
btn.pack()

btn2 = Button(window,text="Limpar", command='')
btn2.pack()

btn3 = Button(window,text="Ver contatos",command='')
btn3.pack()

# text_box = Text(chars="utf-8")
# text_box.pack()



window.mainloop()
