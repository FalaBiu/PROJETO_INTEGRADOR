from   pickle     import FRAME
from ssl import SSLCertVerificationError
from   statistics import quantiles
from   tkinter    import*
from   tkcalendar import Calendar, DateEntry
from   tkinter    import Tk, StringVar, ttk 
from   tkinter    import messagebox
from   tkinter    import filedialog as fd
from   turtle     import bgcolor, left, width
from   PIL        import Image, ImageTk
import tkinter.font as tkFont
from   view       import *

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

#variaveis globais
global tree
global imagem, imagem_string, l_imagem

#funcao inserir
def inserir():
    global imagem, imagem_string, l_imagem
    nome        = e_nome.get()
    local       = e_local.get()
    descricao   = e_descricao.get()
    modelo      = e_modelo.get()
    data        = e_cal.get()
    valor       = e_valor.get()
    serie       = e_serial.get()
    imagem      = imagem_string

    lista_inserir = [nome, local, descricao, modelo, data, valor, serie, imagem]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror ('Erro - ','Preencha todos os campos')
        return
        
    inserir_form(lista_inserir)
    messagebox.showinfo('Sucesso - ','Dados inseridos com sucesso') 

    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_modelo.delete(0, 'end')
    e_cal.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_serial.delete(0, 'end')

    for widget in frameMeio.winfo_children():
        widget.destroy()

    mostrar()

#funcao para escolher imagem
def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label (frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place (x=700, y=10)

#funcao para atualizar os dados
    

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
e_cal = DateEntry (frameMeio, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022)
e_cal.place(x=130, y=131)

l_valor = Label (frameMeio, text="Valor da Compra", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_valor.place(x=10, y=160)
e_valor = Entry (frameMeio, width=30, justify='left', relief="solid")
e_valor.place(x=130, y=161)

l_serial = Label (frameMeio, text="Número de Série", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_serial.place(x=10, y=190)
e_serial = Entry (frameMeio, width=30, justify='left', relief="solid")
e_serial.place(x=130, y=191)

### criacao dos botoes

l_carregar = Label (frameMeio, text="Imagem do Item", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place (x=10, y=220)
botao_carregar = Button(frameMeio, command=escolher_imagem, compound=CENTER, anchor=CENTER, text="CARREGAR".upper(), width=30, 
                 overrelief=RIDGE, font=('ivy 8'), bg=co1, fg=co0)
botao_carregar.place(x=130, y=221) 

#botao inserir
img_add = Image.open('add.png')
img_add = img_add.resize ((20,20))
img_add = ImageTk.PhotoImage(img_add)
botao_inserir = Button (frameMeio, command=inserir, image=img_add, compound=LEFT, anchor=NW, text="Inserir".upper(), width=95,
                        overrelief=RIDGE, font=('ivy 8'), bg=co1, fg=co0)
botao_inserir.place(x=330, y=10) 


#botao atualizar
img_update = Image.open('update.png')
img_update = img_update.resize ((20,20))
img_update = ImageTk.PhotoImage(img_update)
botao_atualizar = Button (frameMeio, image=img_update, compound=LEFT, anchor=NW, text="Atualizar".upper(), width=95,
                        overrelief=RIDGE, font=('ivy 8'), bg=co1, fg=co0)
botao_atualizar.place(x=330, y=50) 

#botao deletar
img_delete = Image.open('delete.png')
img_delete = img_delete.resize ((20,20))
img_delete = ImageTk.PhotoImage(img_delete)
botao_delete = Button (frameMeio, image=img_delete, compound=LEFT, anchor=NW, text="Deletar".upper(), width=95,
                        overrelief=RIDGE, font=('ivy 8'), bg=co1, fg=co0)
botao_delete.place(x=330, y=90) 

#botao ver item
img_item = Image.open('item.png')
img_item = img_item.resize ((20,20))
img_item = ImageTk.PhotoImage(img_item)
botao_item = Button (frameMeio, image=img_item, compound=LEFT, anchor=NW, text="Ver item".upper(), width=95,
                        overrelief=RIDGE, font=('ivy 8'), bg=co1, fg=co0)
botao_item.place(x=330, y=221) 

#labels quantidade total e valores
l_total = Label(frameMeio, width=14, height=3, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1, relief=FLAT)
l_total.place(x=450, y=15)
l_valor_total = Label (frameMeio, text="Valor Total de Todos os Itens", anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_valor_total.place(x=450, y=15)

l_qtd = Label(frameMeio, width=10, height=2, anchor=CENTER, font=('Ivy 25 bold'), bg=co7, fg=co1, relief=FLAT)
l_qtd.place(x=450, y=110)
l_qtd_itens = Label (frameMeio, text="Quantidade Total de Itens", anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_qtd_itens.place(x=450, y=114)


#criando a table view

def mostrar ():
    tabela_head = ['Item','Nome',  'Sala/Área','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']

    lista_itens = ver_form()

    # vertical scrollbar
    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,150,100,160,130,100,100, 100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


    quantidade = []

    for iten in lista_itens:
        quantidade.append(iten[10])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens

mostrar()

janela.mainloop()








