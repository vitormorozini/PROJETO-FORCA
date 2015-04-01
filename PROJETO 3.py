# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:39:28 2015

@author: vitor_000
"""
#VitorMorozini
import random  
import turtle
window = turtle.Screen()
window.bgcolor("lightblue")
tartaruga   = turtle.Turtle()
tartaruga.speed(5)
tartaruga.penup()
tartaruga.setpos(-300,0)
tartaruga.pendown()
tartaruga.color("orange")
angulo = 90
tartaruga.left(180)
tartaruga.right(angulo)  # Vira o angulo pedido
tartaruga.forward(300) # Avança a distancia pedida
tartaruga.right(angulo)
tartaruga.forward(100)
tartaruga.right(angulo)
tartaruga.forward(100)

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
    tartaruga.forward(dist)
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
tartaruga.setpos(200,150)
tartaruga.pendown()
tartaruga.color("black")
tartaruga.write("PLACAR:")

letra=str(window.textinput("Insira uma letra", "Jogo da forca").lower().strip())
if letra in escolha:
    turtle.write(letra)
    
else:
    print("Letra incompativel.Digite outra letra novamente")

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