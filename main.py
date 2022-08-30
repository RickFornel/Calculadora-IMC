from cProfile import label
from tkinter import *
from tkinter import ttk



# cores

cor0 = '#4e80c7' # blue
cor1 = '#fafafa' # white
cor2 = '#0a0a0a' # black

# criando janela

janela = Tk()
janela.geometry('350x300')
janela.title('CALCULADORA DE IMC')
janela.resizable(width=FALSE, height=FALSE)
janela.config(bg=cor0)

# criando frame

frame_1 = Frame(janela, width=350, height=45, bg=cor1)
frame_1.grid(row=0, column=0)

frame_2 = Frame(janela, width=350, height=250, bg=cor1)
frame_2.place(x=0, y=55)

# funções

def calcular_imc():
    global mostrar_resultado, result_imc
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())

    resultado = peso / altura ** 2
    resultado = round(resultado, 1)
    mostrar_resultado = str(resultado)
    
    if resultado < 18.5:
        result_imc = 'Você está abaixo do peso ideal'
    elif resultado >= 18.5 and resultado < 25:
        result_imc = 'Você está dentro do peso ideal'
    elif resultado >= 25 and resultado < 30:
        result_imc = 'Você está acima do peso ideal'
    elif resultado >= 30 and resultado < 40:
        result_imc = 'Você está com obesidade grau I'
    elif resultado >= 40:
        result_imc = 'Você está com obesidade grau II'

    label_imc['text'] = result_imc
    label_saida_imc['text'] = mostrar_resultado
    label_saida_imc['bg'] = cor0
    
# criando labels

label_calc = Label(frame_1, text='Calculadora de IMC', relief='flat', bg=cor1, fg=cor0, anchor='center', font='Ivy 20 bold', width=20 )
label_calc.place(x=0, y=10)

label_peso = Label(frame_2, text='Insira seu peso', relief='flat', bg=cor1, fg=cor0, anchor='center', font='Ivy 10 bold')
label_peso.place(x=10, y=35 )

label_altura = Label(frame_2, text='Insira sua altura', relief='flat', bg=cor1, fg=cor0, anchor='center', font='Ivy 10 bold')
label_altura.place(x=10, y=75 )

label_imc = Label(frame_2, text="", relief='flat', bg=cor1, fg=cor0, anchor='center', font='Ivy 10 bold')
label_imc.place(x=70, y=145 )

label_saida_imc = Label(frame_2, text='0.0', relief='flat', bg=cor1, fg=cor1, anchor='center', font='Ivy 30 bold', padx=8, pady=5)
label_saida_imc.place(x=220, y=35 )

# entry

entry_peso = Entry(frame_2, text='',  width=10, relief='solid' )
entry_peso.place(x=135, y=35 )

entry_altura = Entry(frame_2,text='',  width=10, relief='solid' )
entry_altura.place(x=135, y=75 )

# butonn

button_calcular = Button(frame_2, command=calcular_imc,  width=40, height=1, text='Calcular', relief='ridge', overrelief='solid', font='Ivy 10 bold', bg=cor0, fg=cor1,)
button_calcular.place(x=7, y=190)




janela.mainloop()