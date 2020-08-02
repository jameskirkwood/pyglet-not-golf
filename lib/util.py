from math import *

def normv(angle):
	return (cos(radians(angle)),sin(-radians(angle)))

def addv(a,b):
	return (a[0]+b[0],a[1]+b[1])

def mult(k,a):
	return (k*a[0],k*a[1])

def dot(a,b):
	return a[0]*b[0]+a[1]*b[1]

def cmpt(a,b):
	return dot(a,b)/hypot(a[0],a[1])

def rot(p,angle):
	return ((p[0]*cos(radians(-angle))-p[1]*sin(radians(-angle))),(p[0]*sin(radians(-angle))+p[1]*cos(radians(-angle))))

def ang(v):
	if v[0]<0:
		return degrees(atan(-v[1]/v[0]))+180
	elif v[0]>0:
		if v[1]<=0:
			return degrees(atan(-v[1]/v[0]))
		else:
			return degrees(atan(-v[1]/v[0]))+360
	elif v[1]>0:
		return 270
	elif v[1]<0:
		return 90
	else:
		return 0