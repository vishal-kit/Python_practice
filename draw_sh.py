#!/usr/bin/env python

import turtle

def draw_triangle(some_turtle):
	for i in range (3):
		some_turtle.forward(100)
		some_turtle.right(120)

def draw_art():
	window = turtle.Screen()
	window.bgcolor('red')
	
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("green")
	brad.speed(120)
	for i in range (1,360):
		draw_triangle(brad)
		brad.right(10)
	brad.right(100)
	brad.forward(200)
	window.exitonclick()

draw_art()
