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
tart   = turtle.Turtle()
global tart
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
    
     
def desenha_traco(palavra):  
    x = len(palavra)
    escolha = palavra
    tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
    tartaruga.speed(5)  # define a velocidade
    tartaruga.penup()       # Remova e veja o que acontece
    tartaruga.setpos(-300,0)
    tartaruga.pendown()
    tartaruga.color("orange")   
    for i in range(x):    
        tartaruga.left(angulo)  
        if escolha[i] == " ":
            tartaruga.penup()
        tartaruga.forward(dist)
        tartaruga.hideturtle()    
        tartaruga.penup()
        tartaruga.forward(12)
        tartaruga.pendown()
        tartaruga.forward(dist)  
    return tartaruga

window = turtle.Screen()
window.bgcolor("lightblue")
def desenhar_forca():
    
    tart4   = turtle.Turtle()
    tart4.speed(5)
    tart4.hideturtle()
    tart4.penup()
    tart4.setpos(-300,0)
    tart4.pendown()
    tart4.color("orange")
    angulo = 90
    tart4.left(180)
    tart4.right(angulo)  # Vira o angulo pedido
    tart4.forward(300) # Avança a distancia pedida
    tart4.right(angulo)
    tart4.forward(100)
    tart4.right(angulo)
    tart4.forward(100)

#tartaruga = desenhar_forca()
tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(-300,0)
tartaruga.pendown()
tartaruga.color("orange")

dist = 10
angulo = 0

arquivo = open("entrada.txt",encoding="utf-8")
conteudo = arquivo.readlines()
escolha = random.choice(conteudo).lower().strip()
print(escolha)
x = len(escolha)
print(x)
desenhar_forca()
desenha_traco(escolha)

for i in range(x):
    
    tartaruga.left(angulo)  
    if escolha[i] == " ":
        tartaruga.penup()
    tartaruga.forward(dist)
    tartaruga.hideturtle()    
    tartaruga.penup()
    tartaruga.forward(12)
    tartaruga.pendown()
    tartaruga.forward(dist)


tart1   = turtle.Turtle()  # Cria um objeto "desenhador"
tart1.speed(5)  # define a velocidade
tart1.penup()       # Remova e veja o que acontece
tart1.setpos(200,250)
tart1.pendown()
tart1.color("black")
tart1.write("PLACAR:")

tart2   = turtle.Turtle()  # Cria um objeto "desenhador"
tart2.speed(5)  # define a velocidade
tart2.penup()       # Remova e veja o que acontece
tart2.setpos(200,200)
tart2.pendown()
tart2.color("black")
tart2.write("LETRAS ERRADAS: %d" % erro)

tart3   = turtle.Turtle()  # Cria um objeto "desenhador"
tart3.speed(5)  # define a velocidade
tart3.penup()       # Remova e veja o que acontece
tart3.setpos(200,150)
tart3.pendown()
tart3.color("black")
tart3.write("LETRAS CERTAS: %d" % acertos)



while True:
    letra=str(window.textinput("Jogo da forca", "Insira uma letra").lower().strip()) 
    ctn = escolha.count(letra)  
    desenhar_forca()
    
    if letra in escolha:
        for i in range(len(escolha)):
            if letra ==  escolha[i]:
                turtle.penup()             
                turtle.setpos(-300 + 31*i,0)
                turtle.write(letra,font = ("Arial",24,"normal"))
                acertos += 1
            #elif letra == "a" and escolha[i] == "ã":
                #turtle.write(escolha[i],font = ("Arial",24,"normal"))
                
            
            
    
    else:
        erro += 1  
        funçãodeerro(erro)
    
    if len(letra) > 1:
         print("Voce digitou errado, insira apenas uma letra!")
         
    while erro == 6 or acertos == (len(escolha)):  
        confirm=str(window.textinput("Deseja jogar novamente?","Responda com sim ou não:" ).lower().strip())
        tartaruga.clear()
        tart.clear()
        turtle.clear()
        if confirm == "sim":
            erro = 0
            acertos = 0
            desenhar_forca()
            arquivo = open("entrada.txt",encoding="utf-8")
            conteudo = arquivo.readlines()
            escolha = random.choice(conteudo)
            desenha_traco(escolha)
            for i in range(len(escolha)):
               if letra ==  escolha[i]:
                   
                   turtle.penup()             
                   turtle.setpos(-300 + 31*i,0)
                   turtle.write(letra,font = ("Arial",24,"normal"))
                   acertos += 1
               else:
                   erro += 1  
                   funçãodeerro(erro)
        if confirm == "não":
            break
         
          #elif letra == "a" and escolha[i] == "ã":
                #turtle.write(escolha[i],font = ("Arial",24,"normal"))