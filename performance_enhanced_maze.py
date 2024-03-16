import random
import turtle

wn = turtle.Screen()
wn.title("Maze Try")
wn.setup(750,750)
wn.screensize(500,500,bg="white")

pen = turtle.Turtle()
pen.color("black")

directions1 = ["right", "left"]
directions2 = directions1 + ["up"]
directions3 = directions2 + ["down"]

maze_code = "S2121011011111111111F"


def possibilites(maze_code):
    possibilites = 1
    for i in maze_code:
        if i == "S":
            possibilites *= 4
        elif i == "1":
            possibilites *= 2
        elif i == "2":
            possibilites *= 3
        else:
            possibilites *= 1
    return possibilites


print(possibilites(maze_code))


def paths(maze_code):
    tries = 0
    paths = []
    while tries < possibilites(maze_code):
        path = []
        for i in maze_code:
            if i == "S":
                path += [random.choice(directions3)]
            elif i == "1":
                path += [random.choice(directions1)]
            elif i == "2":
                while True:
                    a = random.randint(0, 2)
                    b = random.randint(0, 2)
                    if b == a:
                        b = random.randint(0, 2)
                    else:
                        path += [[directions2[a], directions2[b]]]
                        break
            elif i == "3":
                path += [directions2]
            elif i == "F":
                path += ["F"]
            else:
                path += ["0"]
        if not path in paths:
            paths += [path]
            tries += 1
        del path
    return paths


def decision_points(maze_code):
    decision_points = []
    for i in range(len(maze_code)):
        if maze_code[i] == "2":
            decision_points += [["junction", i]]
        elif maze_code[i] == "3":
            decision_points += [["fork", i]]
    return decision_points


def occurence_counter_bool(anylist):
    for count in range(len(anylist)):
        if anylist.count(anylist[count]) > 1:
            return False
    return True


def check_collision(path):
    cords = []
    heads = []
    decisions = decision_points(maze_code)
    idx = 0
    wall1 = turtle.Turtle()
    wn.tracer(0)
    wall1.pu()
    wall1.goto(-360,360)
    wall1.pd()
    cords += [wall1.pos()]
    while idx < len(path):
        if idx == 0:
            wall1.write("Start", move= False, align= "center")
            wall1.seth(0)
            if path[idx] == "up":
                wall1.seth(90)
                wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                if wall1.pos() in cords:
                    return False
                cords += [wall1.pos()]
                heads += [wall1.heading()]
            elif path[idx] == "right":
                wall1.seth(0)
                wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                if wall1.pos() in cords:
                    return False
                cords += [wall1.pos()]
                heads += [wall1.heading()]
            elif path[idx] == "down":
                wall1.seth(270)
                wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                if wall1.pos() in cords:
                    return False
                cords += [wall1.pos()]
                heads += [wall1.heading()]
            elif path[idx] == "left":
                wall1.seth(180)
                wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                if wall1.pos() in cords:
                    return False
                cords += [wall1.pos()]
                heads += [wall1.heading()]
            idx += 1
        else:
            if type(path[idx]) != type([]):
                if path[idx] != "0" and path[idx] != "F":
                    if -1 < heads[idx - 1] < 1: #if head 0
                        if path[idx] == "right":
                            wall1.right(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[idx] == "left":
                            wall1.left(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[idx] == "up":
                            wall1.seth(0)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                    elif 89 < heads[idx - 1] < 91: #if head 90
                        if path[idx] == "right":
                            wall1.right(90)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[idx] == "left":
                            wall1.left(90)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[idx] == "up":
                            wall1.seth(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                    elif 179 < heads[idx - 1] < 181: #if head 180
                        if path[idx] == "right":
                            wall1.right(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[idx] == "left":
                            wall1.left(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[idx] == "up":
                            wall1.seth(180)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                    elif 269 < heads[idx - 1] < 271: #if head 270
                        if path[idx] == "right":
                            wall1.right(90)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[idx] == "left":
                            wall1.left(90)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[idx] == "up":
                            wall1.seth(270)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]   
                    idx += 1
                elif path[idx] == "0":
                    wall1.write("0",move=False,align="center")
                    wall1.pu()
                    wall1.seth(heads[decisions[0][1] - 1])
                    wall1.setpos(cords[decisions[0][1]])
                    wall1.pd()
                    if -1 < heads[decisions[0][1] - 1] < 1: #if head 0
                        if path[decisions[0][1]][1] == "right":
                            wall1.right(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[decisions[0][1]][1] == "left":
                            wall1.left(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[decisions[0][1]][1] == "up":
                            wall1.seth(0)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                    elif 89 < heads[decisions[0][1] - 1] < 91: #if head 90
                        if path[decisions[0][1]][1] == "right":
                            wall1.right(90)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[decisions[0][1]][1] == "left":
                            wall1.left(90)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[decisions[0][1]][1] == "up":
                            wall1.seth(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                    elif 179 < heads[decisions[0][1] - 1] < 181: #if head 180
                        if path[decisions[0][1]][1] == "right":
                            wall1.right(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[decisions[0][1]][1] == "left":
                            wall1.left(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[decisions[0][1]][1] == "up":
                            wall1.seth(180)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                    elif 269 < heads[decisions[0][1] - 1] < 271: #if head 270
                        if path[decisions[0][1]][1] == "right":
                            wall1.right(90)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[decisions[0][1]][1] == "left":
                            wall1.left(90)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[decisions[0][1]][1] == "up":
                            wall1.seth(270)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                    decisions = decisions[1:]
                    idx += 1
                elif path[idx] == "F":
                    return True
            else:
                if len(path[idx]) == 2:
                    if -1 < heads[idx - 1] < 1: #if head 0
                        if path[idx][0] == "right":
                            wall1.right(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[idx][0] == "left":
                            wall1.left(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[idx][0] == "up":
                            wall1.seth(0)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                    elif 89 < heads[idx - 1] < 91: #if head 90
                        if path[idx][0] == "right":
                            wall1.right(90)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[idx][0] == "left":
                            wall1.left(90)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[idx][0] == "up":
                            wall1.seth(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                    elif 179 < heads[idx - 1] < 181: #if head 180
                        if path[idx][0] == "right":
                            wall1.right(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[idx][0] == "left":
                            wall1.left(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[idx][0] == "up":
                            wall1.seth(180)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                    elif 269 < heads[idx - 1] < 271: #if head 270
                        if path[idx][0] == "right":
                            wall1.right(90)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[idx][0] == "left":
                            wall1.left(90)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                        elif path[idx][0] == "up":
                            wall1.seth(270)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            if wall1.pos() in cords:
                                return False
                            cords += [wall1.pos()]
                            heads += [wall1.heading()]
                    idx += 1
                else:
                    print("üçlü") #sonra bakıcam yeto
        if abs(cords[-1][0]) > 360 or abs(cords[-1][1]) > 360:
            cords.pop(-1)
            heads.pop(-1)
            return False

def draw_maze_walls(path):
    cords1 = []
    cords2 = []
    cordsC = []
    heads1 = []
    heads2 = []
    headsC = []
    decisions = decision_points(maze_code)
    idx = 0
    wall1 = turtle.Turtle()
    wall2 = turtle.Turtle()
    cr = turtle.Turtle()
    wall1.hideturtle()
    wall2.hideturtle()
    cr.hideturtle()
    cr.pensize(8)
    cr.pencolor("white")
    wn.tracer(0)
    wall1.pu()     #check collision functaki testi silip wall 1 yaptım, wall 2 için de aynıları yazılacak ve kordinatlar +- 10 yapılacak
    wall2.pu()
    cr.pu()
    wall1.goto(-360,365)
    cr.goto(-360,360)
    wall2.goto(-360,355)
    wall1.pd()
    wall2.pd()
    cr.pd()
    cords1 += [wall1.pos()]
    cords2 += [wall2.pos()]
    cordsC += [cr.pos()]
    while idx < len(path):
        if idx == 0:
            wall1.write("Start", move= False, align= "center")
            wall1.seth(0)
            wall2.seth(0)
            cr.seth(0)
            if path[idx] == "up":
                wall1.seth(90)
                wall2.seth(90)
                wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                wall2.setpos(wall2.xcor(), wall2.ycor() + 50)
                cords1 += [wall1.pos()]
                cords2 += [wall2.pos()]
                heads1 += [wall1.heading()]
                heads2 += [wall2.heading()]
            elif path[idx] == "right":
                wall1.seth(0)
                wall2.seth(0)
                cr.seth(0)
                wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                wall2.setpos(wall2.xcor() + 50, wall2.ycor())
                cr.setposition(cr.xcor() + 50, cr.ycor())
                cords1 += [wall1.pos()]
                cords2 += [wall2.pos()]
                cordsC += [cr.pos()]
                heads1 += [wall1.heading()]
                heads2 += [wall2.heading()]
                headsC += [cr.heading()]
            elif path[idx] == "down":
                wall1.setpos(wall1.xcor() + 10, wall1.ycor())
                cr.setpos(cr.xcor() + 5, cr.ycor())
                cr.seth(270)
                cr.setpos(cr.xcor(), cr.ycor() - 5)
                wall1.setpos(wall1.xcor() , wall1.ycor() - 10)
                wall1.seth(270)
                wall2.seth(270)
                wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                wall2.setpos(wall2.xcor(), wall2.ycor() - 50)
                cr.setpos(cr.xcor(), cr.ycor() - 50)
                cords1 += [wall1.pos()]
                cords2 += [wall2.pos()]
                cordsC += [cr.pos()]
                heads1 += [wall1.heading()]
                heads2 += [wall2.heading()]
                headsC += [cr.heading()]
            elif path[idx] == "left":
                wall1.seth(180)
                wall2.seth(180)
                wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                wall2.setpos(wall2.xcor() - 50, wall2.ycor())
                cords1 += [wall1.pos()]
                cords2 += [wall2.pos()]
                heads1 += [wall1.heading()]
                heads2 += [wall2.heading()]
            idx += 1
        else:
            if type(path[idx]) != type([]):
                if path[idx] != "0" and path[idx] != "F":
                    if -1 < heads1[idx - 1] < 1: #if head 0
                        if path[idx] == "right":
                            wall1.setpos(wall1.xcor() + 10, wall1.ycor())
                            cr.setpos(cr.xcor() + 5, cr.ycor())
                            cr.right(90)
                            cr.setpos(cr.xcor(), cr.ycor() - 5)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 10)
                            wall1.right(90)
                            wall2.right(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() - 50)
                            cr.setpos(cr.xcor(), cr.ycor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[idx] == "left":
                            wall2.setpos(wall2.xcor() + 10, wall2.ycor())
                            cr.setpos(cr.xcor() + 5, cr.ycor())
                            cr.left(90)
                            cr.setpos(cr.xcor(), cr.ycor() + 5)
                            wall2.setpos(wall2.xcor(), wall2.ycor() + 10)
                            wall1.left(90)
                            wall2.left(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() + 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[idx] == "up":
                            wall1.seth(0)
                            wall2.seth(0)
                            cr.seth(0)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() + 50, wall2.ycor())
                            cr.setpos(cr.xcor() + 50, cr.ycor())
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                    elif 89 < heads1[idx - 1] < 91: #if head 90
                        if path[idx] == "right":
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 10)
                            cr.sety(cr.ycor() + 5)
                            cr.right(90)
                            cr.setx(cr.xcor() + 5)
                            wall1.setpos(wall1.xcor() + 10, wall1.ycor())
                            wall1.right(90)
                            wall2.right(90)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() + 50, wall2.ycor())
                            cr.setx(cr.xcor() + 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[idx] == "left":
                            wall2.setpos(wall2.xcor(), wall2.ycor() + 10)
                            cr.sety(cr.ycor() + 5)
                            cr.lt(90)
                            cr.setx(cr.xcor() - 5)
                            wall2.setpos(wall2.xcor() - 10, wall2.ycor())
                            wall1.left(90)
                            wall2.left(90)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() - 50, wall2.ycor())
                            cr.setx(cr.xcor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[idx] == "up":
                            wall1.seth(90)
                            wall2.seth(90)
                            cr.seth(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() + 50)
                            cr.sety(cr.ycor() + 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                    elif 179 < heads1[idx - 1] < 181: #if head 180
                        if path[idx] == "right":
                            wall1.setpos(wall1.xcor() - 10, wall1.ycor())
                            cr.setx(cr.xcor() - 5)
                            cr.rt(90)
                            cr.sety(cr.ycor() + 5)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 10)
                            wall1.right(90)
                            wall2.right(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() + 50)
                            cr.sety(cr.ycor() + 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[idx] == "left":
                            wall2.setpos(wall2.xcor() - 10, wall2.ycor())
                            cr.setx(cr.xcor() - 5)
                            cr.lt(90)
                            cr.sety(cr.ycor() - 5)
                            wall2.setpos(wall2.xcor(), wall2.ycor() - 10)
                            wall1.left(90)
                            wall2.left(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() - 50)
                            cr.sety(cr.ycor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[idx] == "up":
                            wall1.seth(180)
                            wall2.seth(180)
                            cr.seth(180)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() - 50, wall2.ycor())
                            cr.setx(cr.xcor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                    elif 269 < heads1[idx - 1] < 271: #if head 270
                        if path[idx] == "right":
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 10)
                            cr.sety(cr.ycor() - 5)
                            cr.rt(90)
                            cr.setx(cr.xcor() - 5)
                            wall1.setpos(wall1.xcor() - 10, wall1.ycor())
                            wall1.right(90)
                            wall2.right(90)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() - 50, wall2.ycor())
                            cr.setx(cr.xcor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[idx] == "left":
                            wall2.setpos(wall2.xcor(), wall2.ycor() - 10)
                            cr.sety(cr.ycor() - 5)
                            cr.lt(90)
                            cr.setx(cr.xcor() + 5)
                            wall2.setpos(wall2.xcor() + 10, wall2.ycor())
                            wall1.left(90)
                            wall2.left(90)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() + 50, wall2.ycor())
                            cr.setx(cr.xcor() + 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[idx] == "up":
                            wall1.seth(270)
                            wall2.seth(270)
                            cr.seth(270)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() - 50)
                            cr.sety(cr.ycor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                    idx += 1
                elif path[idx] == "0":
                    wall1.write("0",move=False,align="center")
                    wall1.pu()
                    wall2.pu()
                    cr.pu()
                    wall1.seth(heads1[decisions[0][1] - 1])
                    wall2.seth(heads2[decisions[0][1] - 1])
                    cr.seth(headsC[decisions[0][1] - 1])
                    wall1.setpos(cords1[decisions[0][1]])
                    wall2.setpos(cords2[decisions[0][1]])
                    cr.setpos(cordsC[decisions[0][1]])
                    cr.pd()
                    wall2.pd()
                    wall1.pd()
                    if -1 < heads1[decisions[0][1] - 1] < 1: #if head 0
                        if path[decisions[0][1]][1] == "right":
                            wall1.setpos(wall1.xcor() + 10, wall1.ycor())
                            cr.setpos(cr.xcor() + 5, cr.ycor())
                            cr.right(90)
                            cr.setpos(cr.xcor(), cr.ycor() - 5)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 10)
                            wall1.right(90)
                            wall2.right(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() - 50)
                            cr.setpos(cr.xcor(), cr.ycor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[decisions[0][1]][1] == "left":
                            wall2.setpos(wall2.xcor() + 10, wall2.ycor())
                            cr.setpos(cr.xcor() + 5, cr.ycor())
                            cr.left(90)
                            cr.setpos(cr.xcor(), cr.ycor() + 5)
                            wall2.setpos(wall2.xcor(), wall2.ycor() + 10)
                            wall1.left(90)
                            wall2.left(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() + 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[decisions[0][1]][1] == "up":
                            wall1.seth(0)
                            wall2.seth(0)
                            cr.seth(0)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() + 50, wall2.ycor())
                            cr.setpos(cr.xcor() + 50, cr.ycor())
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                    elif 89 < heads1[decisions[0][1] - 1] < 91: #if head 90
                        if path[decisions[0][1]][1] == "right":
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 10)
                            cr.sety(cr.ycor() + 5)
                            cr.right(90)
                            cr.setx(cr.xcor() + 5)
                            wall1.setpos(wall1.xcor() + 10, wall1.ycor())
                            wall1.right(90)
                            wall2.right(90)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() + 50, wall2.ycor())
                            cr.setx(cr.xcor() + 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[decisions[0][1]][1] == "left":
                            wall2.setpos(wall2.xcor(), wall2.ycor() + 10)
                            cr.sety(cr.ycor() + 5)
                            cr.lt(90)
                            cr.setx(cr.xcor() - 5)
                            wall2.setpos(wall2.xcor() - 10, wall2.ycor())
                            wall1.left(90)
                            wall2.left(90)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() - 50, wall2.ycor())
                            cr.setx(cr.xcor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[decisions[0][1]][1] == "up":
                            wall1.seth(90)
                            wall2.seth(90)
                            cr.seth(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() + 50)
                            cr.sety(cr.ycor() + 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                    elif 179 < heads1[decisions[0][1] - 1] < 181: #if head 180
                        if path[decisions[0][1]][1] == "right":
                            wall1.setpos(wall1.xcor() - 10, wall1.ycor())
                            cr.setx(cr.xcor() - 5)
                            cr.rt(90)
                            cr.sety(cr.ycor() + 5)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 10)
                            wall1.right(90)
                            wall2.right(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() + 50)
                            cr.sety(cr.ycor() + 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[decisions[0][1]][1] == "left":
                            wall2.setpos(wall2.xcor() - 10, wall2.ycor())
                            cr.setx(cr.xcor() - 5)
                            cr.lt(90)
                            cr.sety(cr.ycor() - 5)
                            wall2.setpos(wall2.xcor(), wall2.ycor() - 10)
                            wall1.left(90)
                            wall2.left(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() - 50)
                            cr.sety(cr.ycor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[decisions[0][1]][1] == "up":
                            wall1.seth(180)
                            wall2.seth(180)
                            cr.seth(180)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() - 50, wall2.ycor())
                            cr.setx(cr.xcor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                    elif 269 < heads1[decisions[0][1] - 1] < 271: #if head 270
                        if path[decisions[0][1]][1] == "right":
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 10)
                            cr.sety(cr.ycor() - 5)
                            cr.rt(90)
                            cr.setx(cr.xcor() - 5)
                            wall1.setpos(wall1.xcor() - 10, wall1.ycor())
                            wall1.right(90)
                            wall2.right(90)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() - 50, wall2.ycor())
                            cr.setx(cr.xcor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[decisions[0][1]][1] == "left":
                            wall2.setpos(wall2.xcor(), wall2.ycor() - 10)
                            cr.sety(cr.ycor() - 5)
                            cr.lt(90)
                            cr.setx(cr.xcor() + 5)
                            wall2.setpos(wall2.xcor() + 10, wall2.ycor())
                            wall1.left(90)
                            wall2.left(90)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() + 50, wall2.ycor())
                            cr.setx(cr.xcor() + 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[decisions[0][1]][1] == "up":
                            wall1.seth(270)
                            wall2.seth(270)
                            cr.seth(270)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() - 50)
                            cr.sety(cr.ycor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                    
                    cr.pu()
                    cr.setpos(cordsC[decisions[0][1] + 1])
                    if -1 < headsC[decisions[0][1]] < 1: #if head 0
                        cr.pd()
                        cr.seth(0)
                        cr.setx(cr.xcor() - 50)
                        cr.pu()
                    elif 89 < headsC[decisions[0][1]] < 91:
                        cr.pd()
                        cr.seth(90)
                        cr.sety(cr.ycor() - 50)
                        cr.pu()
                    elif 179 < headsC[decisions[0][1]] < 181:
                        cr.pd()
                        cr.seth(180)
                        cr.setx(cr.xcor() + 50)
                        cr.pu()
                    elif 269 < headsC[decisions[0][1]] < 271:
                        cr.pd()
                        cr.seth(270)
                        cr.sety(cr.ycor() + 50)
                        cr.pu()
                    cr.seth(headsC[-1])
                    cr.setpos(cordsC[-1])
                    cr.pd()
                    decisions = decisions[1:]
                    idx += 1
                elif path[idx] == "F":
                    return True
            else:
                if len(path[idx]) == 2:
                    if -1 < heads1[idx - 1] < 1: #if head 0
                        if path[idx][0] == "right":
                            wall1.setpos(wall1.xcor() + 10, wall1.ycor())
                            cr.setpos(cr.xcor() + 5, cr.ycor())
                            cr.right(90)
                            cr.setpos(cr.xcor(), cr.ycor() - 5)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 10)
                            wall1.right(90)
                            wall2.right(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() - 50)
                            cr.setpos(cr.xcor(), cr.ycor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[idx][0] == "left":
                            wall2.setpos(wall2.xcor() + 10, wall2.ycor())
                            cr.setpos(cr.xcor() + 5, cr.ycor())
                            cr.left(90)
                            cr.setpos(cr.xcor(), cr.ycor() + 5)
                            wall2.setpos(wall2.xcor(), wall2.ycor() + 10)
                            wall1.left(90)
                            wall2.left(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() + 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[idx][0] == "up":
                            wall1.seth(0)
                            wall2.seth(0)
                            cr.seth(0)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() + 50, wall2.ycor())
                            cr.setpos(cr.xcor() + 50, cr.ycor())
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                    elif 89 < heads1[idx - 1] < 91: #if head 90
                        if path[idx][0] == "right":
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 10)
                            cr.sety(cr.ycor() + 5)
                            cr.right(90)
                            cr.setx(cr.xcor() + 5)
                            wall1.setpos(wall1.xcor() + 10, wall1.ycor())
                            wall1.right(90)
                            wall2.right(90)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() + 50, wall2.ycor())
                            cr.setx(cr.xcor() + 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[idx][0] == "left":
                            wall2.setpos(wall2.xcor(), wall2.ycor() + 10)
                            cr.sety(cr.ycor() + 5)
                            cr.lt(90)
                            cr.setx(cr.xcor() - 5)
                            wall2.setpos(wall2.xcor() - 10, wall2.ycor())
                            wall1.left(90)
                            wall2.left(90)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() - 50, wall2.ycor())
                            cr.setx(cr.xcor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[idx][0] == "up":
                            wall1.seth(90)
                            wall2.seth(90)
                            cr.seth(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() + 50)
                            cr.sety(cr.ycor() + 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                    elif 179 < heads1[idx - 1] < 181: #if head 180
                        if path[idx][0] == "right":
                            wall1.setpos(wall1.xcor() - 10, wall1.ycor())
                            cr.setx(cr.xcor() - 5)
                            cr.rt(90)
                            cr.sety(cr.ycor() + 5)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 10)
                            wall1.right(90)
                            wall2.right(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() + 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() + 50)
                            cr.sety(cr.ycor() + 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[idx][0] == "left":
                            wall2.setpos(wall2.xcor() - 10, wall2.ycor())
                            cr.setx(cr.xcor() - 5)
                            cr.lt(90)
                            cr.sety(cr.ycor() - 5)
                            wall2.setpos(wall2.xcor(), wall2.ycor() - 10)
                            wall1.left(90)
                            wall2.left(90)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() - 50)
                            cr.sety(cr.ycor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[idx][0] == "up":
                            wall1.seth(180)
                            wall2.seth(180)
                            cr.seth(180)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() - 50, wall2.ycor())
                            cr.setx(cr.xcor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                    elif 269 < heads1[idx - 1] < 271: #if head 270
                        if path[idx][0] == "right":
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 10)
                            cr.sety(cr.ycor() - 5)
                            cr.rt(90)
                            cr.setx(cr.xcor() - 5)
                            wall1.setpos(wall1.xcor() - 10, wall1.ycor())
                            wall1.right(90)
                            wall2.right(90)
                            wall1.setpos(wall1.xcor() - 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() - 50, wall2.ycor())
                            cr.setx(cr.xcor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[idx][0] == "left":
                            wall2.setpos(wall2.xcor(), wall2.ycor() - 10)
                            cr.sety(cr.ycor() - 5)
                            cr.lt(90)
                            cr.setx(cr.xcor() + 5)
                            wall2.setpos(wall2.xcor() + 10, wall2.ycor())
                            wall1.left(90)
                            wall2.left(90)
                            wall1.setpos(wall1.xcor() + 50, wall1.ycor())
                            wall2.setpos(wall2.xcor() + 50, wall2.ycor())
                            cr.setx(cr.xcor() + 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                        elif path[idx][0] == "up":
                            wall1.seth(270)
                            wall2.seth(270)
                            cr.seth(270)
                            wall1.setpos(wall1.xcor(), wall1.ycor() - 50)
                            wall2.setpos(wall2.xcor(), wall2.ycor() - 50)
                            cr.sety(cr.ycor() - 50)
                            cords1 += [wall1.pos()]
                            cords2 += [wall2.pos()]
                            cordsC += [cr.pos()]
                            heads1 += [wall1.heading()]
                            heads2 += [wall2.heading()]
                            headsC += [cr.heading()]
                    idx += 1
                else:
                    print("üçlü") #sonra bakıcam yeto



def draw_maze():
    for i in paths(maze_code):
        wn.clear()
        if check_collision(i):
            break
    wn.update()

def true_counter(maze_code):
    trues = 0
    tries = 0
    paths = []
    while tries < possibilites(maze_code):
        path = []
        for i in maze_code:
            if i == "S":
                path += [random.choice(directions3)]
            elif i == "1":
                path += [random.choice(directions1)]
            elif i == "2":
                while True:
                    a = random.randint(0, 2)
                    b = random.randint(0, 2)
                    if b == a:
                        b = random.randint(0, 2)
                    else:
                        path += [[directions2[a], directions2[b]]]
                        break
            elif i == "3":
                path += [directions2]
            elif i == "F":
                path += ["F"]
            else:
                path += ["0"]
        if not path in paths:
            paths += [path]
            tries += 1
            if check_collision(path):
                trues += 1
        del path
    alls = possibilites(maze_code)
    wn.update()
    return 100 * (trues / alls)

def draww_maze(maze_code):
    trues = 0
    while True:
        path = []
        for i in maze_code:
            if i == "S":
                path += [random.choice(directions3)]
            elif i == "1":
                path += [random.choice(directions2)]
            elif i == "2":
                while True:
                    a = random.randint(0, 2)
                    b = random.randint(0, 2)
                    if b == a:
                        b = random.randint(0, 2)
                    else:
                        path += [[directions2[a], directions2[b]]]
                        break
            elif i == "3":
                path += [directions2]
            elif i == "F":
                path += ["F"]
            else:
                path += ["0"]
            wn.clear()
        if check_collision(path):
            wn.clear()
            draw_maze_walls(path)
            trues += 1
            break
        del path

draww_maze(maze_code)
wn.update()

turtle.done()
