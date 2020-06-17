from tkinter import *
from tkinter import messagebox


class Calculadora:
    def __init__(self, master):

        # Frame para mensagem
        self.frame1 = Frame(master)
        self.frame1.pack()

        # Frame para valores
        self.frame2 = Frame(master)
        self.frame2.pack()

        # Frame para botões
        self.frame3 = Frame(master)
        self.frame3.pack()

        self.msg = Label(self.frame1, text='\nCalculadora\n', bg='#5D809A')
        self.msg['font'] = ('ariel', '10', 'bold')
        self.msg.pack()

        self.barra_valor = Entry(self.frame2, width=38, bd=9, bg='#c0c0c0', border='5px')
        self.barra_valor.pack(padx=20, pady=20)

        # Adicionando botões de operação
        self.Clear = Button(self.frame3, bd=4, width=8, text='C', bg='#808080', foreground='white')
        self.Clear['command'] = self.Clear_limpar
        self.Clear.grid(row=4, column=3)

        self.Sub = Button(self.frame3, bd=4, width=8, text='-', bg='#808080', foreground='white')
        self.Sub['command'] = lambda: self.operacoes('-')
        self.Sub.grid(row=3, column=4)

        self.Mult = Button(self.frame3, bd=4, width=8, text='*', bg='#808080', foreground='white')
        self.Mult['command'] = lambda: self.operacoes("*")
        self.Mult.grid(row=2, column=4)

        self.Div = Button(self.frame3, bd=4, width=8, text='/', bg='#808080', foreground='white')
        self.Div['command'] = lambda: self.operacoes("/")
        self.Div.grid(row=1, column=4)

        self.Som = Button(self.frame3, bd=4, width=8, text='+', bg='#808080', foreground='white')
        self.Som['command'] = lambda: self.operacoes('+')
        self.Som.grid(row=4, column=4)

        self.Result = Button(self.frame3, bd=4, width=8, text='=', bg='#808080', foreground='white')
        self.Result['command'] = self.Igual
        self.Result.grid(row=4, column=1)

        # Adicionando botões dos numeros
        self.Num7 = Button(self.frame3, bd=4, width=8, text='7', bg='#808080', foreground='white')
        self.Num7['command'] = lambda: self.operacoes(7)
        self.Num7.grid(row=1, column=1)

        self.Num8 = Button(self.frame3, bd=4, width=8, text='8', bg='#808080', foreground='white')
        self.Num8['command'] = lambda: self.operacoes(8)
        self.Num8.grid(row=1, column=2)

        self.Num9 = Button(self.frame3, bd=4, width=8, text='9', bg='#808080', foreground='white')
        self.Num9['command'] = lambda: self.operacoes(9)
        self.Num9.grid(row=1, column=3)

        self.Num4 = Button(self.frame3, bd=4, width=8, text='4', bg='#808080', foreground='white')
        self.Num4['command'] = lambda: self.operacoes(4)
        self.Num4.grid(row=2, column=1)

        self.Num5 = Button(self.frame3, bd=4, width=8, text='5', bg='#808080', foreground='white')
        self.Num5['command'] = lambda: self.operacoes(5)
        self.Num5.grid(row=2, column=2)

        self.Num6 = Button(self.frame3, bd=4, width=8, text='6', bg='#808080', foreground='white')
        self.Num6['command'] = lambda: self.operacoes(6)
        self.Num6.grid(row=2, column=3)

        self.Num1 = Button(self.frame3, bd=4, width=8, text='1', bg='#808080', foreground='white')
        self.Num1['command'] = lambda: self.operacoes(1)
        self.Num1.grid(row=3, column=1)

        self.Num2 = Button(self.frame3, bd=4, width=8, text='2', bg='#808080', foreground='white')
        self.Num2['command'] = lambda: self.operacoes(2)
        self.Num2.grid(row=3, column=2)

        self.Num3 = Button(self.frame3, bd=4, width=8, text='3', bg='#808080', foreground='white')
        self.Num3['command'] = lambda: self.operacoes(3)
        self.Num3.grid(row=3, column=3)

        self.Num0 = Button(self.frame3, bd=4, width=8, text='0', bg='#808080', foreground='white')
        self.Num0['command'] = lambda: self.operacoes(0)
        self.Num0.grid(row=4, column=2)

    # Entrada dos numeros
    def operacoes(self, num):
        self.barra_valor.insert(END, num)

    # Quando o botão limpar estiver pressionado
    def Clear_limpar(self):
        self.barra_valor.delete(0, END)

    # Quando o botão resultado for pressionado
    def Igual(self):
        try:
            resultado = eval(self.barra_valor.get())
            self.barra_valor.delete(0, END)
            self.barra_valor.insert(END, str(resultado))

        except:
            messagebox.showerror(title='Calculo Error', message='Error, Tente novamente')


root = Tk()
root.geometry('300x300')
root.title('calculadora')
root['bg'] = '#5D809A'
Calculadora(root)
# root.wm_iconbitmap('icone.ico') Mudar icone
root.mainloop()
