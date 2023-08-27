from vpython import *
import time

scene.width = 1250
scene.height = 690
scene.range = 2.5
scene.title = "Bouncing Ball"

ball = sphere(pos=vector(-4.4,0.0,0),radius=0.1,color=color.orange,make_trail=True)
ball.v = vector(0.2,6,0)
g = vector(0,-9.8,0)
dt = 0.005

while 1:
	rate(200)
	if(ball.pos.y > -2.4):
		ball.pos += (ball.v*dt + 0.5*g*dt**2)
		ball.v += g*dt
	else:
		ball.v.y = -(ball.v.y*0.935)
		ball.pos += (ball.v*dt + 0.5*g*dt**2)
		ball.pos += (ball.v*dt + 0.5*g*dt**2)
