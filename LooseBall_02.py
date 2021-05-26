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
     win = GraphWin("Loose Ball", 600, 600)
     win.setBackground("green")

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

     time.sleep(.01)
     ball.move(dx, dy)
     key = win.checkKey()

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
         if ball.getCenter().getY() <= figure.getCenter().getY() and ball.getCenter().getX() >= figure.getCenter().getX():
             text = Text(Point(300, 300), "GAME OVER !!!!")
             text.draw(win)
             break
     win.getMouse()
     win.close()
     return win, figure, ball

    
    

def main():

    window()
   
       
       
main()
     
