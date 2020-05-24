import random
from tkinter import *
from Interface import *
from Tabela import *

__all__ = ['jogar_Dados', 'window2', 'confCanvas2']

'''
def selecionar_Jogada():
def soma_Dados():
def proximo_Jogador():
def manter_Dados():
'''

root = window()
w = confCanvas()

x_mouse = 0
y_mouse = 0

dados = [0,0,0,0,0]
dadosMantidos = [0,0,0,0,0]
jogadasFeitas = 0

img = [PhotoImage(file="dado_1.png"), PhotoImage(file="dado_2.png"), PhotoImage(file="dado_3.png"),
           PhotoImage(file="dado_4.png"), PhotoImage(file="dado_5.png"), PhotoImage(file="dado_6.png")]

def window2():
    global root
    return root

def confCanvas2():
    global w
    return w

def callback(event):
    global dadosMantidos
    global x_mouse
    global y_mouse
    
    x_mouse = event.x
    y_mouse = event.y
    
    if x_mouse > 180 and x_mouse < 212 and y_mouse>600 and y_mouse<632:
        if dadosMantidos[0] == 0:
            dadosMantidos[0] = 1
        else:
            dadosMantidos[0] = 0
    
    if x_mouse > 220 and x_mouse < 252 and y_mouse>600 and y_mouse<632:
        if dadosMantidos[1] == 0:
            dadosMantidos[1] = 1
        else:
            dadosMantidos[1] = 0
    
    if x_mouse > 260 and x_mouse < 292 and y_mouse>600 and y_mouse<632:
        if dadosMantidos[2] == 0:
            dadosMantidos[2] = 1
        else:
            dadosMantidos[2] = 0
    
    if x_mouse > 300 and x_mouse < 332 and y_mouse>600 and y_mouse<632:
        if dadosMantidos[3] == 0:
            dadosMantidos[3] = 1
        else:
            dadosMantidos[3] = 0
    
    if x_mouse > 340 and x_mouse < 372 and y_mouse>600 and y_mouse<632:
        if dadosMantidos[4] == 0:
            dadosMantidos[4] = 1
        else:
            dadosMantidos[4] = 0
        
    print("Coordenadas: ", event.x, event.y, "\n")



def desenha_dado_iniciais():
    global img
    global root
    global dados
    global w
    x = 180
    for el in dados:
        w.create_image(x, 600, anchor=NW, image=img[el - 1])
        x = x + 40
    return


def manterDados():
    global dados
    global dadosMantidos
    global jogadasFeitas
    if jogadasFeitas < 3:
        for i, k in enumerate(dados):
            if dadosMantidos[i] == 1:
                dados[i] = random.randint(1, 6)
        desenha_dado_iniciais()
        jogadasFeitas += 1
    else:
        print("Numero de jogadas maximas atingido")
    print(dadosMantidos)
    dadosMantidos = [0,0,0,0,0]
    return 
    
def jogar_Dados():
    global dados
    global root
    global w
    global jogadasFeitas
    
    jogadasFeitas = 0
    for i, k in enumerate(dados):
        dados[i] = random.randint(1, 6)
    desenha_dado_iniciais()
    b1 = Button(root,text='Manter Dados',command=manterDados)
    b1.place(x = 30, y = 30)
    w.bind("<Button 1>", callback)
    return dados
