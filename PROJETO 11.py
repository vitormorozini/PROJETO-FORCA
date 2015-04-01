# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:39:28 2015

@author: vitor_000
"""
#VitorMorozini
#tartaruga.setpos
erro = 0
import random  
import turtle

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
    
     
       
       

window = turtle.Screen()
window.bgcolor("lightblue")
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


tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(-300,0)
tartaruga.pendown()
tartaruga.color("orange")

dist = 20
angulo = 0

arquivo = open("entrada.txt",encoding="utf-8")
conteudo = arquivo.readlines()
escolha = random.choice(conteudo)
print(escolha)
x = len(escolha)
print(x)

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


tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(200,250)
tartaruga.pendown()
tartaruga.color("black")
tartaruga.write("PLACAR:")

tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(200,200)
tartaruga.pendown()
tartaruga.color("black")
tartaruga.write("PALAVRAS ERRADAS")

tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(200,150)
tartaruga.pendown()
tartaruga.color("black")
tartaruga.write("PALAVRAS CERTAS")




while True:
    letra=str(window.textinput("Jogo da forca", "Insira uma letra").lower().strip()) 
    ctn = escolha.count(letra)  
          
    if letra in escolha:
        for i in range(len(escolha)):
            if letra ==  escolha[i]:
                
                turtle.setpos(-300 + 32*i,0)
                turtle.write(letra,font = ("Arial",24,"normal"))
    
    else:
        erro += 1  
        funçãodeerro(erro)
    
    if len(letra) > 1:
         print("Voce digitou errado, insira apenas uma letra!")
    
#digitadas = []
#acertos = []
#erros = 0
#while True:
#    senha=""
#    for letra in palavra:
#        senha += letra if letra in acertos else "."
#    print(senha)
#    if senha == palavra:
#        print("Você acertou!")
#        break
#    tentativa = input("Digite uma letra:").lower().strip()
#    if tentativa in digitadas:
#        print("Você já tentou esta letra!")
#        continue
#    else:
#        digitadas += tentativa
#        if tentativa in palavra:
#            acertos += tentativa
#        else:
#            erros += 1
#            print("Você errou!")
#        print("X==:==\nX  :  ")
#        print("X  0  " if erros >= 1 else "X")
#        linha2 =""
#        if erros == 2:
#            linha2= "  I  "
#        elif erros == 3:
#            linha2 == " \I/ "
#        elif erros >=4:
#            linha2 == "\I/"
#        print("X%s" % linha2)
#        linha3=""
#        if erros == 5:
#            linha3+= " /  "
#        elif erros >=6:
#            linha3+=" / \ "
#        print("X%s" % linha3)
#        print("X\n========")
#        if erros == 6:
#            print("Enforcado!")
#            break