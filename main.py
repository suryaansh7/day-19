from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
choice= screen.textinput(title="make ur bet",prompt="enter color of ur choice")
colour=["violet","indigo","blue","green","yellow","orange","red"]
race=[]
a=0
k=-70
def turt():
    global k
    global a

    timmy=Turtle()
    timmy.shape("turtle")
    timmy.color(colour[a])
    a+=1
    timmy.penup()
    timmy.goto(x=-230,y=k)
    timmy.pendown()
    k+=30
    race.append(timmy)
    timmy.speed(0)
for i in range(1,8):
    turt()
def steps():
    n= (random.randint(1,10))
    return n

j="true"
while (j=="true"):
    for i in race:
        k1=steps()
        i.forward(k1)

        if i.xcor()>=220:
            k=i.color()

            j="false"
            break


if k==choice:
    print("u win")
else:
    print("u lose,the",k[0],"turtle won")


screen.exitonclick()










