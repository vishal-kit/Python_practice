#!/usr/bin/env python
import turtle

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
draw_triangle()
