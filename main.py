from pickle import FRAME
from tkinter import*
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd
from turtle import bgcolor

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
#janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

#criacao dos frames
frameCima = Frame(janela, width=1050, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1050, height=303, bg=co1, pady=20, relief="raised")
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW )

frameBaixo = Frame(janela, width=1050, height=300, bg=co1, relief="sunken")
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW )

janela.mainloop()