from tkinter import *

raiz=Tk()
raiz.iconbitmap('calculadora.ico')
raiz.geometry('235x310')
raiz.title('Calculadora')
raiz.config(bg='black')
raiz.resizable(False,False)

#Frames
frame_1=Frame(raiz, width=235,height=50,bg='#7788a6')
frame_1.grid(row=0,column=0)

frame_2=Frame(raiz,width=235,height=260,bg='black')
frame_2.grid(row=1,column=0)

valor=''
valor_texto=StringVar()

#Funções
def entrada(event):
    global valor
    valor+=str(event)
    valor_texto.set(valor)

    pass

def limpa_tela():
    global valor
    valor=""
    valor_texto.set("")

def calcular():
    global valor
    resultado=eval(valor)
    valor_texto.set(resultado)
    valor=str(resultado)


#Label
label_tela=Label(frame_1,textvariable=valor_texto,font=('Ivy 18'), width=16,height=2,padx=7,justify=RIGHT,bg='#7788a6',anchor='e',relief=FLAT)
label_tela.place(x=0,y=0)

#Botões


#Primeira linha
b_limpar=Button(frame_2,text='C',width=11,height=2,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=limpa_tela)
b_limpar.place(x=0,y=0)
b_percent=Button(frame_2,text='%',width=5,height=2,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= lambda :entrada('%'))
b_percent.place(x=118,y=0)
b_dividir=Button(frame_2,text='/',width=5,height=2,bg='orange',fg='white',font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= lambda :entrada('/'))
b_dividir.place(x=177,y=0)

#Segunda Linha
b_7=Button(frame_2,text='7',width=5,height=2,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= lambda :entrada('7'))
b_7.place(x=0,y=52)
b_8=Button(frame_2,text='8',width=5,height=2,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= lambda :entrada('8'))
b_8.place(x=59,y=52)
b_9=Button(frame_2,text='9',width=5,height=2,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= lambda :entrada('9'))
b_9.place(x=118,y=52)
b_multiplicar=Button(frame_2,text='*',width=5,height=2,bg='orange',fg='white',font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= lambda :entrada('*'))
b_multiplicar.place(x=177,y=52)

#Terceira Linha
b_4=Button(frame_2,text='4',width=5,height=2,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= lambda :entrada('4'))
b_4.place(x=0,y=104)
b_5=Button(frame_2,text='5',width=5,height=2,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= lambda :entrada('5'))
b_5.place(x=59,y=104)
b_6=Button(frame_2,text='6',width=5,height=2,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= lambda :entrada('6'))
b_6.place(x=118,y=104)
b_subtrair=Button(frame_2,text='-',width=5,height=2,bg='orange',fg='white',font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= lambda :entrada('-'))
b_subtrair.place(x=177,y=104)

#Quarta Linha
b_3=Button(frame_2,text='3',width=5,height=2,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= lambda :entrada('3'))
b_3.place(x=0,y=156)
b_2=Button(frame_2,text='2',width=5,height=2,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= lambda :entrada('2'))
b_2.place(x=59,y=156)
b_1=Button(frame_2,text='1',width=5,height=2,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= lambda :entrada('1'))
b_1.place(x=118,y=156)
b_adicionar=Button(frame_2,text='+',width=5,height=2,bg='orange',fg='white',font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= lambda :entrada('+'))
b_adicionar.place(x=177,y=156)

#Quinta Linha
b_0=Button(frame_2,text='0',width=11,height=2,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= lambda :entrada('0'))
b_0.place(x=0,y=208)
b_ponto=Button(frame_2,text='.',width=5,height=2,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= lambda :entrada('.'))
b_ponto.place(x=118,y=208)
b_igualdade=Button(frame_2,text='=',width=5,height=2,bg='orange',fg='white',font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE, command= calcular)
b_igualdade.place(x=177,y=208)




raiz.mainloop()