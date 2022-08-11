import tkinter as tk
import turtle
from PIL import ImageGrab
from time import strftime
from random import randint
from ttkbootstrap import Style
import time
import random
# style = Style()
style = Style(theme='superhero')
#theme[ 'cyborg', 'journal', 'darkly', 'flatly', 'solar', 'minty', 'litera', '
# united',  'pulse', 'cosmo', 'lumen', 'yeti', 'superhero', 'winnative', 'sandstone', 'default']
top = style.master
# top=tk.Tk()
top.geometry("410x500+1320+50")
cv=tk.Canvas(top,bg='#acc')
cv.place(x=0,y=0,width=410,height=500)
def creatString(a4,a7,a8,a9=''):
    a4=a4
    a7=a7
    a8=a8
    a9=a9
    for i in range(a7):
        try:
            a4=a4.replace('F',a8)
            a4=a4.replace('f',a9)
        except:
            a4=a4.replace('f',a9)
            a4=a4.replace('F',a8)
            
    return a4
def drewString(angle1,angle2,d,string,speed,color,xbegin,ybegin,pensize,fillcolor):
    tic = time.perf_counter()
    turtle.screensize(2000,2000,'#EEE685')
    turtle.setup(700,700,600,50)
    turtle.hideturtle()#隐藏画笔
    turtle.penup()
    turtle.goto(xbegin,ybegin)
    turtle.pendown()
    string=string
    d=d
    angle1=angle1
    angle2=angle2
    turtle.pensize(pensize)
    turtle.pencolor(color)
    speeds=v.get()
    if speeds!=0:
        turtle.speed(speed)
    else:
        turtle.tracer(False)
        
    zhandian=[]
    p=(0,0)
    a=90
    turtle.seth(90)
    for i in string:
        if i=='F' or i=='f':
            turtle.fd(d)
            a=a%360
            p=turtle.pos()
            #print(turtle.pos())
        elif i=='+':
            a-=angle2
            turtle.setheading(a)
        elif i=='-':
            a+=angle1
            turtle.setheading(a)
        elif i=='[':
            zhandian.append([p,a])
        elif i==']':
            m=zhandian.pop()
            p=m[0]
            a=m[1]
            turtle.penup()
            turtle.goto(p[0],p[1])
            turtle.pendown()
            turtle.setheading(a)
        elif i=='<':
            turtle.begin_fill()
            turtle.fillcolor(fillcolor)
        elif i=='>':
            turtle.end_fill()
        elif i=='.':
            turtle.fd(pensize)
            turtle.dot(3*pensize,fillcolor)
    turtle.penup()
    turtle.goto(xbegin+40,ybegin+20)
    turtle.pendown()
    turtle.setheading(0)
    turtle.pencolor(fillcolor)
    # turtle.write('Zhan  '+strftime('%Y-%m-%d'))
    zhandian=[]
    turtle.pencolor(color)
    if speeds==0:
        turtle.tracer(True)
    toc = time.perf_counter()
    turtle.write('the total time is '+str(toc-tic)+'seconds')
# def petal(m, t):  # 树下花瓣
#     t = t.Turtle()
#     t.hideturtle()
#     for i in range(m):
#         a = 200 - 400 * random.random()
#         b = 30 - 40 * random.random()
#         t.up()
#         t.forward(b)
#         t.left(90)
#         t.forward(a)
#         t.down()
#         # 淡珊瑚色
#         t.color("green")
#         t.circle(1)
#         t.up()
#         t.backward(a)
#         t.right(90)
#         t.backward(b)

def saveimg():
    numb=randint(0,10000)
    turtle.setup(700,700,600,50)
    bbox=(600,50,1300,750)
    im=ImageGrab.grab(bbox)
    im.save(str(numb)+'.jpg',"JPEG")
def rules():
    global numb
    l=lists[numb%4]
    var1.set('25')
    var2.set('25')
    var3.set('5')
    var4.set('10')
    var15.set('4')
    var7.set(l[0])
    var8.set(l[1])
    var9.set(l[2])
    numb+=1

def main():
    turtle.reset()
    turtle.pendown()
    a1=var1.get()
    a2=var2.get()
    a3=var3.get()
    a4=var4.get()
    a5=var5.get()
    a11=var11.get()
    a12=var12.get()
    a13=var13.get()
    a14=var14.get()
    a15=var15.get()
    
    a7=var7.get()
    a8=var8.get()
    a9=var9.get()
    
    nstring=creatString(a7,int(a15),a8,a9)
    #print(nstring)
    drewString(int(a1),int(a2),int(a3),nstring,int(a4),a5,int(a11),int(a12),int(a13),a14)
    # petal(255,turtle)
    turtle.penup()
    v.set('0')
top.title("L-System plant simulation - Zerui Zhan")
lists=[['F','F[-F.]F[+F.]F','F'],['f','FF','F-[[f.]+f.]+F[+Ff.]-f'],['f','FF','F[-f.]+f'],['F','FF+[+F-F-F.]-[-F+F+F.]','F']]
numb=0

lbl1=tk.Label(top,text='Left Angle :',bg='#acc')
lbl1.place(x=0,y=0,width=100,height=40)
lbl2=tk.Label(top,text='Right Angle:',bg='#acc')
lbl2.place(x=0,y=50,width=100,height=40)
lbl3=tk.Label(top,text='Line Lengh:',bg='#acc')
lbl3.place(x=0,y=100,width=100,height=40)
lbl4=tk.Label(top,text='Pen Speed:',bg='#acc')
lbl4.place(x=0,y=150,width=100,height=40)
lbl5=tk.Label(top,text='Pen Color:',bg='#acc')
lbl5.place(x=0,y=200,width=100,height=40)
#lbl6=tk.Label(top,text='Pen Color:',bg='#acc')
#lbl6.place(x=0,y=250,width=100,height=40)

lbl7=tk.Label(top,text='Axiom  :',bg='#acc')
lbl7.place(x=0,y=300,width=150,height=40)
lbl8=tk.Label(top,text='First Rule(F) :',bg='#acc')
lbl8.place(x=0,y=350,width=150,height=40)
lbl9=tk.Label(top,text='Second Rule(f):',bg='#acc')
lbl9.place(x=0,y=400,width=150,height=40)

lbl11=tk.Label(top,text='x_begin:',bg='#acc')
lbl11.place(x=200,y=0,width=100,height=40)
lbl12=tk.Label(top,text='y_begin:',bg='#acc')
lbl12.place(x=200,y=50,width=100,height=40)
lbl13=tk.Label(top,text='pensize:',bg='#acc')
lbl13.place(x=200,y=100,width=100,height=40)
lbl14=tk.Label(top,text='fillcolor:',bg='#acc')
lbl14.place(x=200,y=150,width=100,height=40)
lbl15=tk.Label(top,text='iteration:',bg='#acc')
lbl15.place(x=200,y=200,width=100,height=40)
#lbl16=tk.Label(top,text='2:',bg='#acc')
#lbl16.place(x=200,y=250,width=100,height=40)
#lbl17=tk.Label(top,text='3:',bg='#acc')
#lbl17.place(x=200,y=300,width=100,height=40)
#lbl18=tk.Label(top,text='Left Angle:',bg='#acc')
#lbl18.place(x=0,y=0,width=100,height=40)
lbl=tk.Label(top,text='        F:forward  f:same F  -:turn left  +:turn left  [:save state,start new branch \n          ]:end branch,restore state  <:start Filling  >:end filling    . :plot',bg='#acc')
lbl.place(x=0,y=250,width=400,height=40)
var1=tk.StringVar()
var2=tk.StringVar()
var3=tk.StringVar()
var4=tk.StringVar()
var5=tk.StringVar()
#var6=tk.StringVar()

var11=tk.StringVar()
var12=tk.StringVar()
var13=tk.StringVar()
var14=tk.StringVar()
var15=tk.StringVar()
#var16=tk.StringVar()
#var17=tk.StringVar()

var7=tk.StringVar()
var8=tk.StringVar()
var9=tk.StringVar()

var3.set('10')
var4.set('6')
speeds=[1]
var5.set('green')
#var6.set('green')
var11.set('0')
var12.set('-300')
var13.set('2')
var14.set('white')
var15.set('3')
var7.set("F")
var9.set('F')
entry1=tk.Entry(top,textvariable=var1,bg='#acc')
entry2=tk.Entry(top,textvariable=var2,bg='#acc')
entry3=tk.Entry(top,textvariable=var3,bg='#acc')
entry4=tk.Entry(top,textvariable=var4,bg='#acc')
entry5=tk.Entry(top,textvariable=var5,bg='#acc')
#entry6=tk.Entry(top,textvariable=var6,bg='#acc')
entry7=tk.Entry(top,textvariable=var7,bg='#acc')
entry8=tk.Entry(top,textvariable=var8,bg='#acc')
entry9=tk.Entry(top,textvariable=var9,bg='#acc')

entry11=tk.Entry(top,textvariable=var11,bg='#acc')
entry12=tk.Entry(top,textvariable=var12,bg='#acc')
entry13=tk.Entry(top,textvariable=var13,bg='#acc')
entry14=tk.Entry(top,textvariable=var14,bg='#acc')
entry15=tk.Entry(top,textvariable=var15,bg='#acc')
#entry16=tk.Entry(top,textvariable=var16,bg='#acc')
#entry17=tk.Entry(top,textvariable=var17,bg='#acc')

entry1.place(x=100,y=0,width=100,height=40)
entry2.place(x=100,y=50,width=100,height=40)
entry3.place(x=100,y=100,width=100,height=40)
entry4.place(x=100,y=150,width=100,height=40)
entry5.place(x=100,y=200,width=100,height=40)
#entry6.place(x=100,y=250,width=100,height=40)

entry11.place(x=300,y=0,width=100,height=40)
entry12.place(x=300,y=50,width=100,height=40)
entry13.place(x=300,y=100,width=100,height=40)
entry14.place(x=300,y=150,width=100,height=40)
entry15.place(x=300,y=200,width=100,height=40)
#entry16.place(x=300,y=250,width=100,height=40)
#entry17.place(x=300,y=300,width=100,height=40)

entry7.place(x=150,y=300,width=250,height=40)
entry8.place(x=150,y=350,width=250,height=40)
entry9.place(x=150,y=400,width=250,height=40)

#text=tk.Text(top)
#text.place(x=0,y=250,width=400,height=200)
btn=tk.Button(top,text='Generate2D',bg='#acc',command=main)
btn.place(x=0,y=450,width=110,height=50)
btn=tk.Button(top,text='Generate3D',bg='#acc',command=main)
btn.place(x=125,y=450,width=110,height=50)
btn1=tk.Button(top,text='Save\nImg',bg='#acc',font=('黑体',8),command=saveimg)
btn1.place(x=355,y=450,width=50,height=50)
btn2=tk.Button(top,text='Help',bg='#acc',font=('黑体',8),command=rules)
btn2.place(x=300,y=450,width=50,height=50)
v=tk.IntVar()
v.set('0')
btn3=tk.Radiobutton(top,text='set\nspeed',value='1',variable=v,bg='#acc',font=('黑体',8))
btn3.place(x=245,y=450,width=50,height=50)


top.mainloop()
