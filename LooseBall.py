# Universidad Politecnica de Puerto Rico recinto San Juan
#Proyecto 01: Simple Game
#Estudiante: Jonathan D Ortiz Couverthier #84792
#Profesor: Edwin Florez Gomez
#Clase: CECS 3210 Advanced Programming


##Proyect:
# El siguiente proyecto tiene como nombre LOOSE BALL el mismo fue creado utilizando solo la libreria Graphic.py en Python.
# El juego consiste en dos objetos creados uno es tipo rectangulo y el otro es un circulo que en este caso simula lo que es el balon.
# El balon en este caso el circulo se programo para que rebotara en los limites mientras que el cuadrado seria el usuario el cual se puede mover
# para diferentes puntos. Lo que se trato de hacer es que si el balon toca el cuadrado perderas el juego basicamente en eso se basa el juego de LOOSE BALL


##Conclusion del proyecto:
# Los Objetos funcionan perfectamente se enfrento dificurtad al tratar de crear el choque entre el circulo y el cuadrado. Si se fijan tuve que 
# manejar o cambiar la medida de la pantalla en el cual parece que arreglo parte del problema. El problema seria el siguente: Mientras el objeto
# tipo circula pasa por el lado sur de la figura tipo rectango y no la toca esta todo perfecto y si la toca por el lado sur GAME OVER tambien esta perfecto.
# Pero cuando el objeto tipo circulo pasa por el lado norte sin tocar el objeto tipo rectangulo se ACTIVA RAPIDAMENTE EL GAME OVER!!!
# Ese es el unico defecto del juego el cual no he podido resolver.




from graphics import *


def figure_left(figure):
    figure.move(-15, 0)

def figure_right(figure):
    figure.move(15, 0)

def figure_up(figure):
    figure.move(0, -15)

def figure_down(figure):
    figure.move(0, 15)

def window():
    #Window
     win = GraphWin("Loose Ball", 600, 600)
     win.setBackground("green")
     return win
    
 
    
         
def main():
     win = window()

     figure = Rectangle(Point(100, 100), Point(100, 100))
     figure.setOutline("blue")
     figure.setFill("blue")
     figure.draw(win)
     figure.move(9, 9)
     figure.setWidth(40)


     #Ball
     radius = 40
     ball = Circle(Point(400, 300), radius)
     ball.setOutline("red")
     ball.setFill("red")
     ball.draw(win)
     dx = 3
     dy = 3
     yFloor = radius
     yCieling = win.getHeight() - radius
     xFloor = radius
     xCieling = win.getHeight() - radius
     
     


     
     while True:
         time.sleep(.01)
         ball.move(dx, dy)
         key = win.checkKey()
         
         if key == "Left":
             figure_left(figure)
         if key == "Right":
             figure_right(figure)
         if key == "Up":
             figure_up(figure)
         if key == "Down":
             figure_down(figure)
     #Move Ball
         if ball.getCenter().getY() <= yFloor or ball.getCenter().getY() >= yCieling:
             dy = -dy
         if ball.getCenter().getX() <= xFloor or ball.getCenter().getX() >= xCieling:
             dx = -dx

     #Ball Collision with figure
         if ball.getCenter().getY() <= figure.getCenter().getY() and ball.getCenter().getX() >= figure.getCenter().getX():
             
             text = Text(Point(300, 300), "GAME OVER !!!!")
             text.draw(win)
             break


          
     win.getMouse()
     win.close()        
main()
     

