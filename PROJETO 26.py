# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:28:58 2015

@author: vitor_000
"""

    if letra in escolha:
        for i in range(len(escolha)):
            if letra ==  escolha[i]:
                leonardo.penup()             
                leonardo.setpos(-300 + 31*i,0)
                leonardo.write(letra,font = ("Arial",24,"normal"))
                acertos += 1
            elif letra == "a" and escolha[i] == "ã":
                leonardo.penup()             
                leonardo.setpos(-300 + 31*i,0)
                leonardo.write(escolha[i],font = ("Arial",24,"normal"))
            elif letra == "i" and escolha[i] == "í":
                leonardo.penup()             
                leonardo.setpos(-300 + 31*i,0)
                leonardo.write(escolha[i],font = ("Arial",24,"normal"))
            elif letra == "o" and escolha[i] == "ô":
                leonardo.penup()             
                leonardo.setpos(-300 + 31*i,0)
                leonardo.write(escolha[i],font = ("Arial",24,"normal"))
            elif letra == "o" and escolha[i] == "ó":
                leonardo.penup()             
                leonardo.setpos(-300 + 31*i,0)
                leonardo.write(escolha[i],font = ("Arial",24,"normal"))
            