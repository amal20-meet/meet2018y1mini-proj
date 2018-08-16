import turtle
turtle.shape("turtle")
finn = turtle.clone()
finn.shape("square")
finn.goto(0,100)
finn.goto(100,100)
finn.left(100)
finn.goto(100,0)
finn.left(-100)
finn.goto(0,0)
charlie = turtle.clone()
charlie.left(180)
charlie.goto(-100,0)
charlie.left(180)
charlie.goto(0,-100)
charlie.left(90)
charlie.goto(0,0)
finn.goto(300,300)
finn.stamp()
finn.goto(100,100)
charlie.goto(400,400)





















turtle.mainloop()
