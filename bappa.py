import turtle as t

t.pencolor("white")
t.bgcolor("black")

def go(x,y):
          t.penup()
          t.goto(x,y)
          t.pendown()


#u1          
go(-60,180)
t.lt(70)
for i in range(5):
          t.pensize(i+0.5)
          t.fd(2)

t.circle(-5,190)
t.fd(12)
for i in range(12):
          t.pensize(i+0.5)
          t.fd(3)
          t.lt(20)
#u2
go(-70,145)
t.rt(140)
def to():
          
          for i in range(8):
                    t.pensize(i+0.7)
                    t.fd(8)
                    t.lt(10)
                    


to()
go(-65,130)
t.rt(80)
to()
go(-60,118)
t.rt(80)
to()

#u3
go(-8,115)
t.rt(145)
for i in range(5):
          t.pensize(i+0.2)
          t.fd(7)
          t.rt(2)
t.pensize(3)

for i in range(10):
          t.fd(5)
          t.rt(2)
for i in range(8):
          t.fd(5)
          t.lt(1.5)
for i in range(5):
          t.fd(5)
          t.lt(2.5)
t.pensize(2)
for i in range(14):
          t.fd(2)
          t.lt(3)
          
t.pencolor("red")
go(-10,95)
t.rt(135)
t.fd(15)
t.circle(4,190)
t.fd(16)
go(-10,85)
t.lt(180)
t.fd(15)
t.circle(4,185)
t.fd(16)
t.pencolor("white")
#u4
go(8,108)
t.lt(40)
for i in range(10):
          t.pensize(i)
          t.fd(5)
          t.rt(6)
t.pensize(9)
t.circle(-20,120)
for i in range(8,0,-1):
          t.pensize(i)
          t.fd(10)
          t.rt(4)

#lr
go(-5,35)
t.rt(180)
for i in range(10):
          t.pensize(i)
          t.fd(5)
          t.rt(12)
for i in range(10,0,-1):
          t.pensize(i)
          t.fd(5)
          t.rt(10)

t.lt(190)

for i in range(10):
          t.pensize(i)
          t.fd(15)
          t.rt(15)

for i in range(10,0,-1):
          t.pensize(i)
          t.fd(25)
          t.rt(16)         
          
go(30,-15)
#lrr
for i in range(10):
          t.pensize(i+4)
          t.fd(4)
          t.rt(8)
for i in range(10,0,-1):
          t.pensize(i+4)
          t.fd(20)
          t.rt(15) 
for i in range(4,0,-1):
          t.pensize(i)
          t.fd(15)
          t.lt(25)
          
#lru
go(40,30)

#lrus
for i in range(5):
          t.pensize(i+5)
          t.fd(10)
          t.lt(25)
for i in range(5):
          t.pensize(i+5)
          t.fd(6)
          t.lt(21)

go(55,27)
t.fillcolor("white")
t.begin_fill()
t.circle(-3)
t.end_fill()

#dl
go(-140,-25)
t.rt(130)
for i in range(12):
          t.pensize(i)
          t.fd(8)
          t.lt(18)
          
for i in range(12,0,-1):
          t.pensize(i)
          t.fd(31)
          t.lt(16)
          
go(-145,60)
for i in range(8):
          t.pensize(i+4)
          t.fd(7)
          t.rt(25)
for i in range(12,0,-1):
          t.pensize(i)
          t.fd(15)
          t.rt(22)

go(-74,110)
t.rt(150)
t.pensize(6)
t.circle(4,270)
#t.rt(90)
t.pensize(6)
for i in range(10):
          t.fd(5)
          t.lt(12)
          
for i in range(4,10):
          t.pensize(i)
          t.fd(6)
          t.lt(13)
          
for i in range(3):
          t.fd(4)
          t.lt(14)

for i in range(9,1,-1):
          t.pensize(i)
          t.fd(10)
          t.rt(7)
          
go(-80,30)
t.lt(120)
t.pensize(1)
t.fillcolor("white")
t.begin_fill()
t.fd(12)
t.rt(100)
t.fd(6)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(6)
t.end_fill()

go(-72,18)
t.fillcolor("white")
t.begin_fill()
t.rt(167)
t.fd(19)
t.lt(150)
t.fd(22)
t.lt(115)
t.fd(15)
t.end_fill()

#eye eyebrow
go(-66,85)
t.lt(150)
for i in range(3):
          t.pensize(i)
          t.fd(5)
          t.rt(3)

for i in range(3,1,-1):
          t.pensize(i)
          t.fd(7)
          t.rt(3)


for i in range(12):
          t.fd(2)
          t.rt(7)

#eye uperlid
go(-71,73)
t.lt(110)
t.pensize(1)
for i in range(4):
          t.fd(2)
          t.lt(3)
for i in range(9):
          t.fd(4)
          t.rt(11)
          
t.rt(135)
for i in range(6):
          t.fd(3)
          t.lt(4)

for i in range(6):
          t.fd(3)
          t.lt(5)

for i in range(4):
          t.fd(3)
          t.rt(4)
#eye lower lid
t.lt(5)
for i in range(5):
          t.fd(6.5)
          t.rt(9)

go(-45,58)
t.lt(85)
t.fillcolor("cyan")
t.begin_fill()
for i in range(6):
          t.fd(4)
          t.rt(25)

t.end_fill()

go(-38,55)

t.lt(150)
for i in range(9):
          t.fd(4)
          t.rt(12)
go(-1000,1000)
t.exitonclick()