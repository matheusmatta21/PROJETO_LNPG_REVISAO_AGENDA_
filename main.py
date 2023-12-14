from tkinter import *
from tkinter.ttk import Combobox
import math 

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


def escreverDados():
    arquivo = open("contatos.txt", "a", encoding="utf-8")
    arquivo.write(f"{inputNome.get()},{inputNumero.get()},{inputEmail.get()},{comboboxPreferencial.get()}\n")
    arquivo.close()

def lerDados():
    windowTwo = Tk() #passivel de erro
    windowTwo.title("Lista de contatos")
    windowTwo.geometry("1000x500")

    arquivo = open("contatos.txt", "r", encoding="utf-8")
    for linha in arquivo.readlines():
        contato = linha.split(",")
        labelContatos = Label(windowTwo, text=f"contato:{contato[0]},{contato[1]},{contato[2]},{contato[3]}")
        labelContatos.pack()

def limpar_arquivo():
    arquivo = open('contatos.txt','w',encoding='utf-8')
    arquivo.write("")
    arquivo.close()




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
labelpreferencial = Label(window,text="Preferencial:")
labelpreferencial.pack()
comboboxPreferencial = Combobox(window, values=valores)
comboboxPreferencial.pack()

#Botões de enviar e limpar e ver contatos
btn = Button(window,text="Enviar", command=escreverDados)
btn.pack()

btn2 = Button(window,text="Limpar", command=limpar_arquivo)
btn2.pack()

btn3 = Button(window,text="Ver contatos",command=lerDados)
btn3.pack()


# text_box = Text(chars="utf-8")
# text_box.pack()



window.mainloop()
