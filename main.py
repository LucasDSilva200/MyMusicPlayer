from tkinter import *

#importando o pillow
from PIL import Image,ImageTk

#importando o pygame
import pygame
from pygame import mixer

import os
import random

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#2e2d2c"  # black
co4 = "#403d3d"   # letra
co5 = "#4a88e8"  # Azul 


#Criação da janela

janela = Tk()
janela.title("MySound")
janela.geometry('372x255')
janela.configure(background=co1)
janela.resizable(width=FALSE,height=FALSE)


frame_esquerda = Frame(janela,width=170,height=150,bg=co3)
frame_esquerda.grid(row=0,column=0,pady=1,padx=1,sticky=NSEW)

frame_direita = Frame(janela,width=270,height=150,bg=co3)
frame_direita.grid(row=0,column=1,pady=1,padx=0,sticky=NSEW)


frame_baixo = Frame(janela,width=423,height=100,bg=co3)
frame_baixo.grid(row=1,column=0,columnspan=3,pady=1,padx=0,sticky=NSEW)

#configurando o frame do lado esquerdo

img_1 = Image.open('res/icon1.png')
img_1 = img_1.resize((130,130))
img_1 = ImageTk.PhotoImage(img_1)

l_logo = Label(frame_esquerda, height=130,image=img_1,compound=LEFT,padx=0,anchor='nw',font=('ivy 16 bold'), bg=co3,fg=co3)
l_logo.place(x=8,y=12)

#criando funcoes

#Musica anterior
def previous_music():
    tocando = l_rodando['text'] 
    index = musicas.index(tocando)
    novo_index = index-1
    tocando = musicas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()
    listbox.delete(0,END)
    mostrar()
    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_rodando['text'] = tocando
    
#Randomizando as musicas
def random_music():
    r = random.choice(musicas)
    novo_index = musicas.index(r)

    tocando = musicas[novo_index]
    
    mixer.music.load(tocando)
    mixer.music.play()

    #deletando os elementos na playlist
    listbox.delete(0,END)

    mostrar()

    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_rodando['text'] = tocando
    
#Proxima Musica
def next_music():
    tocando = l_rodando['text'] 
    index = musicas.index(tocando)

    novo_index = index+1

    tocando = musicas[novo_index]
    
    mixer.music.load(tocando)
    mixer.music.play()

    #deletando os elementos na playlist
    listbox.delete(0,END)

    mostrar()

    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_rodando['text'] = tocando
    

#Tocar musica
def play_music():
    rodando = listbox.get(ACTIVE)
    l_rodando['text'] = rodando
    mixer.music.load(rodando)
    mixer.music.play()

#Pausar musica
def pause_music():
    mixer.music.pause()
#continuar musica
def continue_music():
    mixer.music.unpause()
#Parar musica
def stop_music():
    mixer.music.stop()

#Configurando o frame do lado direito

lista = ['joao','lucas','andreia','joao','lucas','andreia','joao','lucas','andreia','joao','lucas','andreia','joao','lucas','andreia']
listbox = Listbox(frame_direita, width=22, height=10, selectmode=SINGLE, font=('arial 9 bold') , bg=co3, fg=co1)
listbox.grid(row=0,column=0)

s = Scrollbar(frame_direita)
s.grid(row=0,column=1,sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)


#Configurando o frame de baixo

l_rodando = Label(frame_baixo,text='Escolha uma musica na lista',width=44,justify=LEFT,anchor='nw',font=('ivy 10'), bg=co1,fg=co4)
l_rodando.place(x=0,y=1)

img_2 = Image.open('res/2.png')
img_2 = img_2.resize((30,30))
img_2 = ImageTk.PhotoImage(img_2)
b_anterior = Button(frame_baixo,command=previous_music,width=40,height=40,image=img_2,font=('ivy 10 bold'),relief=RAISED,overrelief=RIDGE, bg=co3,fg=co1)
b_anterior.place(x=38,y=35)



img_3 = Image.open('res/3.png')
img_3 = img_3.resize((30,30))
img_3 = ImageTk.PhotoImage(img_3)
b_play = Button(frame_baixo,command=play_music,width=40,height=40,image=img_3,font=('ivy 10 bold'),relief=RAISED,overrelief=RIDGE, bg=co3,fg=co1)
b_play.place(x=84,y=35)



img_4 = Image.open('res/4.png')
img_4 = img_4.resize((30,30))
img_4 = ImageTk.PhotoImage(img_4)
b_proxima = Button(frame_baixo,command=next_music,width=40,height=40,image=img_4,font=('ivy 10 bold'),relief=RAISED,overrelief=RIDGE, bg=co3,fg=co1)
b_proxima.place(x=130,y=35)



img_5 = Image.open('res/5.png')
img_5 = img_5.resize((30,30))
img_5 = ImageTk.PhotoImage(img_5)
b_pausar = Button(frame_baixo,command=pause_music,width=40,height=40,image=img_5,font=('ivy 10 bold'),relief=RAISED,overrelief=RIDGE, bg=co3,fg=co1)
b_pausar.place(x=176,y=35)



img_6 = Image.open('res/6.png')
img_6 = img_6.resize((30,30))
img_6 = ImageTk.PhotoImage(img_6)
b_continuar = Button(frame_baixo,command=continue_music,width=40,height=40,image=img_6,font=('ivy 10 bold'),relief=RAISED,overrelief=RIDGE, bg=co3,fg=co1)
b_continuar.place(x=222,y=35)



img_7 = Image.open('res/7.png')
img_7 = img_7.resize((30,30))
img_7 = ImageTk.PhotoImage(img_7)
b_stop = Button(frame_baixo,command=stop_music,width=40,height=40,image=img_7,font=('ivy 10 bold'),relief=RAISED,overrelief=RIDGE, bg=co3,fg=co1)
b_stop.place(x=268,y=35)

img_8 = Image.open('res/8.png')
img_8 = img_8.resize((30,30))
img_8 = ImageTk.PhotoImage(img_8)
b_random = Button(frame_baixo,command=random_music,width=40,height=40,image=img_8,font=('ivy 10 bold'),relief=RAISED,overrelief=RIDGE, bg=co3,fg=co1)
b_random.place(x=314,y=35)


os.chdir(r'C:/Users/lucas/OneDrive/Documentos/Musicas')
musicas = os.listdir()

def mostrar():
    for i in musicas:
        listbox.insert(END,i)


mostrar()

#Inicando mixer
mixer.init()




janela.mainloop()
