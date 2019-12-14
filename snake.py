import turtle
import time
import random

delay = 0.1

wn = turtle.Screen()
wn.bgcolor("green")
wn.setup(width=500,height=500)
wn.tracer(0)

#snake head
snake = turtle.Turtle()
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0,0)
snake.direction = "up"

#snake food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,90)

segment = []


#move

def go_up():
	snake.direction = "up"

def go_down():
	snake.direction = "down"	

def go_right():
	snake.direction = "right"

def go_left():
	snake.direction = "left"

def move():
	if snake.direction == "up":
		y = snake.ycor()
		snake.sety(y+20)

	if snake.direction == "down":
		y = snake.ycor()
		snake.sety(y-20)
	
	if snake.direction == "right":
		x = snake.ycor()
		snake.setx(x+20)
		
	if snake.direction == "left":
		y = snake.ycor()
		snake.setx(x-20)



#keypad

wn.listen
wn.onkeypress(go_up, "t")
wn.onkeypress(go_down, "v")
wn.onkeypress(go_right, "h")
wn.onkeypress(go_left, "d")

while True:
	wn.update()
	if snake.distance(food) < 20 :
		
	#move the food
		x = random.randint(-290,290)
		y = random.randint(-290,290)
		food.goto(x,y)
		
	#new segment
	new_segment = turtle.Turtle()
	new_segment.speed(0)
	new_segment.shape("square")
	new_segment.color("black")
	new_segment.penup()
	segment.append(new_segment)
	
#move new segment	
for index in range(len(segments)-1, 0, -1):
	x = segments[index-1].xcor()
	y = segments[index-1].ycor()
	segments[index].goto(x,y)

#move segment 0 to whare the head is
if len(segments) > 0:
	x = snake.xcor()
	y = snake.ycor()
	segments[0].goto(x,y)		
		
	move()
	
	time.sleep(delay)

wn.mainloop()