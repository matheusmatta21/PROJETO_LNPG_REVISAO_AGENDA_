from tkinter import *
from tkinter.ttk import Combobox
import math 

#combobox para ver se o contato é preferencial ou nâo
#um botao para adicionar o contato e outro pra limpar o formulário  

#A interface deve conter campos para inserir nome, número de telefone, e-mail e um campo de seleção se o contato é preferencial ou não. Um botão para adicionar o contato e outro botão para limpar o formulário.

#Adicione um recurso para visualizar a lista de contatos na interface.

#def para validação dos valores



def escreverDados(): #sem validação
        nome = inputNome.get()
        numero = int(inputNumero.get())
        email = inputEmail.get() 
        preferencial = comboboxPreferencial.get()
        arquivo = open("contatos.txt", "a", encoding="utf-8")
        arquivo.write(f"{nome},{numero},{email},{preferencial}\n")
        arquivo.close()
    

def escreverDados2(): ##com validacao incompleta
        nome = inputNome.get()
        if nome == '':
             labelerror2 = Label(window,text="Digite um nome!")
             labelerror2.pack()
        numero = inputNumero.get()
        if numero == "":
            labelErro = Label(window, text="Digite um número válido.")
            labelErro.pack() 
        email = inputEmail.get()
        if email == '':
            labelerror3 = Label(window,text="Insira um email!")
            labelerror3.pack()
        elif email not in ['@', '.']:
             labelerror4 = Label(window, text="Insira a formatação certa do email")
             labelerror4.pack()
        preferencial = comboboxPreferencial.get()
        if preferencial == "":
             labelerror5 = Label(window, text="Selecione uma opção da caixa")
             labelerror5.pack()
        arquivo = open("contatos.txt", "a", encoding="utf-8")
        arquivo.write(f"{nome},{numero},{email},{preferencial}\n")
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
btn = Button(window,text="Enviar", command=escreverDados2)
btn.pack()

btn2 = Button(window,text="Limpar", command=limpar_arquivo)
btn2.pack()

btn3 = Button(window,text="Ver contatos",command=lerDados)
btn3.pack()


# text_box = Text(chars="utf-8")
# text_box.pack()



window.mainloop()
