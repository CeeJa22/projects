from turtle import Turtle, Screen

tim  = Turtle()
tim.shape('turtle')
screen = Screen()


def move_forwards():
    tim.fd(10)


def r_turn():
    tim.rt(10)

    
 
def l_turn():
    tim.lt(10)   



def backwards():
    tim.backward(10)
    
    
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    

screen.listen()
screen.onkey(key = 'w', fun = move_forwards)
screen.onkey(key = 'd', fun = r_turn)
screen.onkey(key = 'a', fun = l_turn)
screen.onkey(key = 's', fun = backwards)
screen.onkey(key = 'c', fun = clear)

screen.exitonclick()