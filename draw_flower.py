#!/usr/bin/env python
import turtle

def draw_circle(brad,radius):
	brad.speed(0)
	brad.circle(radius)
	

def main():
	window=turtle.Screen()
	window.bgcolor("green")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("white")
		
	for i in range (4):
		#brad.right(60)
		for j in range (70):
			draw_circle(brad,j)
		brad.right(90)
	brad.right(90)
	brad.forward(250)
	brad.penup()
	brad.home()
	brad.goto(250,0)
	brad.speed(3)
	brad.pendown()
	brad.right(60)
	brad.forward(100)
	brad.left(120)
	brad.forward(100)

	brad.penup()
	brad.home()
	brad.goto(400,0)
	brad.speed(3)
	brad.pendown()
	brad.left(180)
	brad.circle(45,180)
	brad.left(90)
	brad.forward(25)
	brad.left(90)
	brad.forward(15)
	window.exitonclick()
main()
