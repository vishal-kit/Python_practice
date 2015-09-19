#!/usr/bin/env python
import turtle

def draw_square():
	window=turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(0.9)
	
	for i in range(4):
		brad.forward(100)
		brad.right(90)
	window.exitonclick()

def draw_triangle():
	window=turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(0.9)

	for i in range(3):
			brad.forward(100)
			brad.right(120)
	window.exitonclick()

def draw_circle():
	window=turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(0.9)
	brad.circle(100)
	window.exitonclick()

def main():
	shape='circle'
	if (shape=='square'):
		draw_square()
	elif (shape=='circle'):
		draw_circle()
	else: # (shape=='triangle'):
		draw_triangle()
#draw_shape(shape)
main()
