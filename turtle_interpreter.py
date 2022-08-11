#姓名：
#日期：2022年07月01日
import turtle
import sys
import lsystem
from math import cos,sin

def drewString(dstring,distance,angle1,angle2):
    turtle.pencolor('green')
    dtc=distance
    agl1=angle1
    agl2=angle2
    cmdlists=[]
    cmdlist=[]
    #turtle.tracer(False)#快速画完
    turtle.speed(10)
    ruledata=[None]#记录栈点
    xy=(0.0,0.0)#初始化数据
    a=90
    turtle.seth(90)
    for i in dstring:
        if i =='F'or i== 'f':
            a=a%360
            t=turtle.pos()
            xy=t
            #print(xy,a)
            #print(ruledata[-1])
            cmd=turtle.fd(dtc)
            cmdlist.append((xy,a))
            #print(turtle.pos())
        elif i=='-':
            a+=agl1
            cmd=turtle.setheading(a)
        elif i=='+':
            a-=agl2
            cmd=turtle.setheading(a)
        elif i=='[':
            ruledata.append((xy,a))
        elif i==']':
            p=ruledata.pop()
            xy=(p[0][0],p[0][1])
            a=p[1]
            turtle.penup()
            turtle.goto(p[0][0],p[0][1])
            turtle.pendown()
            turtle.setheading(a)
            
            #print(ruledata)
    
    #turtle.tracer(True)#快速画完


def hold():
    turtle.hideturtle()#隐藏画笔
    turtle.listen()#监听q按钮按下事件
    turtle.onkey(turtle.bye,'q')#当用户按下'q'键时关闭窗口
    turtle.exitonclick()#让乌龟听一下咔嗒声

def Drasting():
    scr=turtle.screensize(6000,6000,'#acc')
    string=lsystem.main()
    #string=lsystem.main(sys.argv)
    drewString(string,30,25,25)
    hold()#监听函数
if __name__=='__main__':
    Drasting()
    
