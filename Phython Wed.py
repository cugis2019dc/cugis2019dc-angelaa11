# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("hello")

import plotly

dir(plotly)
print("I am Angela")
print(5*2)
print(5/2)
print(5-2)
print(5**2)
print(8/9*3)
print("5*2")

def multiply(a,b):
    multiply=a*b

def sum(a,b):
    sum(a+b)
    print(sum)

def area(a,b,c):
    area=.5*13*24
    print(area)
    
def triArea(b,h):
    triArea=.5*b*h
    print("the area of the triangle with a base of ,'b', and a height of 'h, 'is', triArea)
    
triArea(1,2)


 tree = q +15
 print(tree)
 
def cadburychocoalte1 (c,a,b):
    cadburychocoalte1 = (c+a+b)
    print(cadburychocoalte1)
    
    
 def cadburychocolate (c,a,b):
     print(c,a,b)
     cadburychocolate('c','a','b')
     
print("Hello Kaya")

def hello(a):
    a= "Kaya"
    print("hello",a)
    
name= input("please enter your name")
print("Your name is", name)

age = input("please enter your age")
print("Thank you, you entered", age)

import math

dir(math)

math.pi

math.pow(12,8)


value= input("Please enter a number")
"value of variable"
print("Please enter a value for your variable")

import math
a= int(input)("enter a value"))

def cadbury(a):
    cadbury=math.pow(a.1/3)
    print("the cubic root of", a, "is", cadbury)

darkchocolate= 5
whitechocolate= 8
milk= 6
print(whitechocolate)
whitechocolate

1=("milk chocolate")
2=("dark chocolate")
3=("white chocolate")
print(1,2,3)
 
steve= 32
lia=28
vin=45
katie=38

studentgender{"steve",32:"M","lia,28":"F","vin,45":"M","katie",38:"F"}
student

import pandas
dir(pandas)

studentdf = pandas.DataFrame(studentgender)
studentdf

milk= 5
dark= 8
white=3

choco= [["milk", 5], ["dark", 6], ["white", 8]]
choco = pandas.DataFrame(choco,columns=("choco")


studentdf["name"]
studentdf["age"]

#create a data frame
studentlist = [["steve",32,"m"]],["lia",28,"f"],["vin",45,"m"],["katie",38]
studentlist

import pandas

studentdf = pandas.DataFrame(studentlist,columns=("name","age","gender"))
studentdf

studentdf2 = pandas.DataFrame(studentlist,columns=("name","age","gender"),index["1","2","3","4"])
studentdf2

import plotly
dir(plotly)
from plotly.offline import plot

import plotly.graph_objs as go
studentbar = go.Bar(x=studentdf["name"],y=studentdf["age"])
plot([studentbar])

titles = go.Layout(title) = "number of chocolate" by type")
plot([chocolatesBar])

fig = go.Figure(data=[chocolatesBar], layout=titles)
plot(fig)
