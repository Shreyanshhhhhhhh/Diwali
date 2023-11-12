from turtle import *
import time
speed(0)

window=Screen()
carver=Turtle()

#function for curve
def curve01(a,d):
    for i in range(d):
        right(a)
        fd(1)
def curve02(a,d):
    for i in range(d):
        left(a)
        fd(1)

penup()
goto(-120,-200)
pendown()


#Making Diya
left(150)
fillcolor("black")
begin_fill()
curve01(0.25,225)
right(124)
curve02(0.37,275)
right(142)
curve02(0.37,275)
right(125)
curve01(0.248,460)
end_fill()

penup()
home()
left(98)
forward(70)
right(78)
pendown()

def sujal(colour,sd):
    carver.color(colour)
    bgcolor(sd)

# flame
begin_poly()
curve02(0.4,200)
curve02(0.18,190)
left(90)
curve02(0.18,190)
curve02(0.39,200)
end_poly()
pairs = get_poly()
register_shape("new_shape", pairs)
carver.shape("new_shape")
carver.left(90)
sujal("yellow","black")
hideturtle()

#Loop For changing colors
start = time.time()
count = 0
colours = "#FFDE59", "#FFD21B", "#FAFF00", "#FF4500", "#FD632A", "#FF9C78"
bg="#FF4500","#FD632A","#FF9C78","#FFDE59","#FFD21B","#FAFF00"    
  
while True:
   if time.time() - start > 1:
        sujal(colours[count % 6],bg[count % 6])
        window.update()
        count += 1
        start = time.time()