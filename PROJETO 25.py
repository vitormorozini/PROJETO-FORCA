# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:39:28 2015

@author: vitor_000
"""
#VitorMorozini
#tartaruga.setpos
erro = 0
acertos = 0
import random  
import turtle
#import tkinter

def funçãodeerro(erro):
    if erro == 1:
       tart.right(90)
       tart.circle(15)
    
    if erro == 2:
       tart.right(270)       
       tart.penup()
       tart.forward(30)
       tart.pendown()
       tart.forward(75)
       
    if erro == 3:
        tart.right(45)
        tart.forward(30)
        
    if erro == 4:
        tart.right(180)
        tart.forward(30)
        tart.right(90)
        tart.forward(30)
        
    if erro == 5:
        tart.right(180)
        tart.forward(30)
        tart.right(45)
        tart.forward(50)
        tart.right(135)
        tart.forward(30)
        
    if erro == 6:
        tart.right(180)
        tart.forward(30)
        tart.left(90)
        tart.forward(30)
    
     
       
       
recomeçar = "sim"
while (recomeçar == "sim"):
    
    window = turtle.Screen()
    window.bgcolor("lightblue")
    tart   = turtle.Turtle()
    def desenhar_forca():
        global tart
        tart   = turtle.Turtle()
        tart.speed(5)
        tart.hideturtle()
        tart.penup()
        tart.setpos(-300,0)
        tart.pendown()
        tart.color("orange")
        angulo = 90
        tart.left(180)
        tart.right(angulo)  # Vira o angulo pedido
        tart.forward(300) # Avança a distancia pedida
        tart.right(angulo)
        tart.forward(100)
        tart.right(angulo)
        tart.forward(100)

    desenhar_forca()
    tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
    tartaruga.speed(5)  # define a velocidade
    tartaruga.penup()       # Remova e veja o que acontece
    tartaruga.setpos(-300,0)
    tartaruga.pendown()
    tartaruga.color("blue")
    global tartaruga
        
        #dist = 10
    angulo = 0
        
    arquivo = open("entrada.txt",encoding="utf-8")
    conteudo = arquivo.readlines()
    escolha = random.choice(conteudo).lower().strip()
    print(escolha)
    x = len(escolha)
    print(x)

    for i in range(x):
        tartaruga.left(angulo)  
        if escolha[i] == " ":
            tartaruga.penup()
            tartaruga.forward(20)
            tartaruga.hideturtle()    
            tartaruga.penup()
            tartaruga.forward(12)
            tartaruga.pendown()



    tartaruga1   = turtle.Turtle()  # Cria um objeto "desenhador"
    tartaruga1.speed(5)  # define a velocidade
    tartaruga1.penup()       # Remova e veja o que acontece
    tartaruga1.setpos(200,250)
    tartaruga1.pendown()
    tartaruga1.color("black")
    tartaruga1.write("PLACAR:")

    tartaruga2   = turtle.Turtle()  # Cria um objeto "desenhador"
    tartaruga2.speed(5)  # define a velocidade
    tartaruga2.penup()       # Remova e veja o que acontece
    tartaruga2.setpos(200,200)
    tartaruga2.pendown()
    tartaruga2.color("black")
    tartaruga2.write("LETRAS ERRADAS: %d" %erro)

    tartaruga3   = turtle.Turtle()  # Cria um objeto "desenhador"
    tartaruga3.speed(5)  # define a velocidade
    tartaruga3.penup()       # Remova e veja o que acontece
    tartaruga3.setpos(200,150)
    tartaruga3.pendown()
    tartaruga3.color("black")
    tartaruga3.write("LETRAS CERTAS: %d" %acertos)




    while True:
         letra=str(window.textinput("Jogo da forca", "Insira uma letra").lower().strip()) 
        ctn = escolha.count(letra)
          
        if letra in escolha:
            for i in range(len(escolha)):
                if letra ==  escolha[i]:
                    turtle.penup()             
                    turtle.setpos(-300 + 31*i,0)
                    turtle.write(letra,font = ("Arial",24,"normal"))
                    acertos += 1
                elif letra == "a" and escolha[i] == "ã":
                    turtle.penup()             
                    turtle.setpos(-300 + 31*i,0)
                    turtle.write(escolha[i],font = ("Arial",24,"normal"))
                elif letra == "i" and escolha[i] == "í":
                    turtle.penup()             
                    turtle.setpos(-300 + 31*i,0)
                    turtle.write(escolha[i],font = ("Arial",24,"normal"))
                elif letra == "o" and escolha[i] == "ô":
                    turtle.penup()             
                    turtle.setpos(-300 + 31*i,0)
                    turtle.write(escolha[i],font = ("Arial",24,"normal"))
                elif letra == "o" and escolha[i] == "ó":
                    turtle.penup()             
                    turtle.setpos(-300 + 31*i,0)
                    turtle.write(escolha[i],font = ("Arial",24,"normal"))

    
        else:
            erro += 1  
            funçãodeerro(erro)
    
        if len(letra) > 1:
            print("Voce digitou errado, insira apenas uma letra!")
         
        if erro == 6 or acertos == (len(escolha)-escolha.count(" ")):  
            tartaruga.clear()
            recomecar=str(window.textinput("Deseja jogar novamente?","Responda com sim ou não:" ).lower().strip())

        
        
        
'''
       if confirm == "sim":
            erro = 0
            acertos = 0
            tart.clear()
            turtle.clear()
            desenhar_forca()
            arquivo = open("entrada.txt",encoding="utf-8")
            conteudo = arquivo.readlines()
            escolha = random.choice(conteudo)
            for i in range(x):
                 global tartaruga
                 tartaruga.left(angulo)
                 tartaruga.setpos(-300,0)
                 if escolha[i] == " ":
                      tartaruga.penup()
                 tartaruga.forward(dist)
                 tartaruga.hideturtle()    
                 tartaruga.penup()
                 tartaruga.forward(12)
                 tartaruga.pendown()
                 tartaruga.forward(dist) 
            if letra in escolha:
                for i in range(len(escolha)):
                    if letra ==  escolha[i]:
                       turtle.penup()             
                       turtle.setpos(-300 + 31*i,0)
                       turtle.write(letra,font = ("Arial",24,"normal"))
                       acertos += 1
                       continue
   '''
