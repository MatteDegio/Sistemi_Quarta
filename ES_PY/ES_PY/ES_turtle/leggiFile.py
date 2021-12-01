import turtle

snow = turtle.Turtle() 
finestra = turtle.Screen() 
snow.speed(40)

f = open("scriviFile.txt", "r")
righe = f.readlines()

for riga in righe:
    lista = riga.split(":")
    if(lista[0]=="forward"):
        snow.forward(int(lista[1][:-1]))
    elif(lista[0]=="right"):
        snow.right(int(lista[1][:-1]))
    elif(lista[0]=="left"):
        snow.left(int(lista[1][:-1]))

finestra.exitonclick()
f.close()#chiude file