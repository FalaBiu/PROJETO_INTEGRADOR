from pickle import FRAME
from tkinter import*
from tkcalendar import Calendar
from tkinter import Tk, StringVar, ttk 
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd
from turtle import bgcolor, left
from PIL import Image, ImageTk


#cores
co0 = "#2e2d2b" #Preto
co1 = "#feffff" #Branca
co2 = "#4fa882" #Verde
co3 = "#38576b" #Valor
co4 = "#403d3d" #letra
co5 = "#e06636" #Laranja
co6 = "#038cfc" #Azul
co7 = "#3fbfb9" #Verde 1
co8 = "#263738" #Verde +
co9 = "#e9edf5" #Cinza


#criando janela em branco
janela = Tk ()
janela.title("")
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

#criacao dos frames
frameCima = Frame(janela, width=1050, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1050, height=303, bg=co1, pady=20, relief="raised")
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW )

frameBaixo = Frame(janela, width=1050, height=300, bg=co1, relief="sunken")
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW )

#inserir imagem - icone
app_img = Image.open ('icone.png')
app_img = app_img.resize ((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label (frameCima, image=app_img, text=" Controle de Estoque Doméstico", width=900, 
                  compound=LEFT, relief=RAISED, anchor=NW, font= ('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)                 


# criando campos de entrada
l_nome = Label (frameMeio, text="Nome", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_nome.place(x=10, y=10)
e_nome = Entry (frameMeio, width=30, justify='left', relief="solid")
e_nome.place(x=130, y=11)

l_local = Label (frameMeio, text="Sala/Área", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_local.place(x=10, y=40)
e_local = Entry (frameMeio, width=30, justify='left', relief="solid")
e_local.place(x=130, y=41)

l_descricao = Label (frameMeio, text="Descrição", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_descricao.place(x=10, y=70)
e_descricao = Entry (frameMeio, width=30, justify='left', relief="solid")
e_descricao.place(x=130, y=71)

l_modelo = Label (frameMeio, text="Marca/Modelo", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_modelo.place(x=10, y=100)
e_modelo = Entry (frameMeio, width=30, justify='left', relief="solid")
e_modelo.place(x=130, y=101)

l_cal = Label (frameMeio, text="Data da Compra", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_cal.place(x=10, y=130)
e_cal = DateEntry (frameMeio, width=12, background='darkblue', foreground='white', borderwidth=2, year=2020)
e_cal.place(x=130, y=131)

janela.mainloop()

