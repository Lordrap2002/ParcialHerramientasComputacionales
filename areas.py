from math import *

def areaCua(x):
    x = x**2
    return x

def areaRec(b,a):
     y = b*a
     return y

#cuando se tienen dos lados y el angulo comprendido entre ellos
def areaTri1(l1,l2,angulo):
     z1 = (l1*l2*sin(radians(angulo)))/2
     return z1

#cuando se tiene base y altura
def areaTri2(a,b):    
     z2 = (a*b)/2
     return z2

def areaCir(r):
     w = pi*(r**2)
     return w

def impCua(x):
    print("el area del cuadrado es " + str(areaCua(x)))

def impRect(a,b):
    print("el area del rectangulo es " + str(areaRec(b,a)))

def impTri1(l1,l2,angulo):
    print("el area del triangulo es " + str(areaTri1(l1,l2,angulo)))

def impTri2(a,b):
    print("el area del triangulo es " + str(areaTri2(a,b)))
    
def impCir(r):
    print("el area del circulo es " + str(areaCir(r)))
    
