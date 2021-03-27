from vpython import *

isRunning = False
timeToBreak = False

myScene = canvas(background=vector(225 / 255, 237 / 255, 209 / 255), align="left")
myScene.title = """<h1 style="margin:5px;">One Spring Simulation</h1>"""

def Run():
    global isRunning

    if start_run_but.text == "Pause":
        isRunning = False
        start_run_but.text = "Play"
        start_run_but.background = color.blue
    #     Stop

    elif start_run_but.text == "Play":
        isRunning = True
        start_run_but.text = "Pause"
        start_run_but.background = color.red
    #     Play

    elif start_run_but.text == "Start":
        start_run_but.background = color.red
        start_run_but.text = "Pause"
        isRunning = True

# button_condition = "Start"
start_run_but = button(text="Start", pos=myScene.title_anchor, bind=Run,color=color.white, background=color.green)

# ________________________3D Objects__________________________
L = 10
R = L / 125
d = L - 2
xaxis = arrow(pos=vec(-16, 0.6, -1.5), axis=vec(d, 0, 0), shaftwidth =R,color=vector(224/255, 235/255, 213/255),opacity=0.6,round = True)
yaxis = arrow(pos=vec(-16, 0.6, -1.5), axis=vec(0,d , 0), shaftwidth =R, color=vector(224/255, 235/255, 213/255),opacity=0.6,round = True)
zaxis = arrow(pos=vec(-16, 0.6, -1.5), axis=vec(0, 0,d), shaftwidth =R, color=vector(224/255, 235/255, 213/255),opacity=0.6,round = True)
k = 1.02
h = 0.05 * L*1.5
text(pos=xaxis.pos + k * xaxis.axis, text='x', height=h, align='center', billboard=True, emissive=True,color=color.red,opacity=0.6)
text(pos=yaxis.pos + k * yaxis.axis, text='y', height=h, align='center', billboard=True, emissive=True,color=color.green,opacity=0.6)
text(pos=zaxis.pos + k * zaxis.axis, text='z', height=h, align='center', billboard=True, emissive=True,color=color.blue,opacity=0.6)


wall = box(texture=textures.wood, pos=vector(-15, 2.1, 0), size=vector(2, 4, 3))
wall_2 = box(pos=vector(-14.9, 1, 0), size=vector(2, 2, 1.5), color=color.red)
floor = box(texture=textures.wood, pos=vector(4, 0, 0), size=vector(40, 0.2, 3))

myObj = box(pos=vector(5, 0.61, 0), size=vector(1, 1, 1), color=vector(36 / 255, 98 / 255, 255 / 255))
spring = helix(texture=textures.metal, pos=vector(-14, 0.61, 0), axis=myObj.pos - vector(-14, 0.61, 0), radius=0.4,
               thickness=0.12, coils=30)
# ____________________________________________________________

# ________________________Properties__________________________
myObj.mass = 1
myObj.force = vector(0, 0, 0)
myObj.velocity = vector(20, 0, 0)

spring.stiffness = 50

friction = 10
# ____________________________________________________________

# myScene.camera.follow(myObj)

# ___________________________My UI____________________________
new_mass = myObj.mass
new_velocity = myObj.velocity.x
new_friction = friction
new_stiffness = spring.stiffness

def getMass(s):
    if s.number > 0:
        global new_mass
        new_mass = s.number

def getStartVelocity(s):
    global new_velocity
    new_velocity = s.number

def getFriction(s):
    if s.number > 0:
        global new_friction
        new_friction = s.number

def getStiffness(s):
    if s.number > 0:
        global new_stiffness
        new_stiffness = s.number

def ChangeProperties(b):
    myObj.mass = new_mass
    myObj.velocity = vector(new_velocity, 0, 0)
    spring.stiffness = new_stiffness

    global friction
    friction = new_friction

    global prop_text,mass_text,velocity_text,friction_text,stiffness_text

    myText = "Mass_________:" + str(myObj.mass)
    mass_text.text = myText
    myText = "\n\nStartVelocity___:" + str(myObj.velocity.x)
    velocity_text.text = myText
    myText = "\n\nFriction_______:" + str(friction)
    friction_text.text = myText
    myText = '\n\nStiffness______:' + str(spring.stiffness)
    stiffness_text.text = myText

    if start_run_but.text == "Pause":
        Run()

    global t,a,timeToBreak

    myObj.pos.x = start_pos
    t = 0
    a = 0
    spring.axis = myObj.pos - spring.pos

    global f1,f2
    f1.delete()
    f2.delete()


prop_text = wtext(text="<h3 style=\"margin-top:0px;\":>Properties</h3>")
myText = "Mass_________:"+str(myObj.mass)
mass_text = wtext(text=myText)
myText = "\n\nStartVelocity___:"+str(myObj.velocity.x)
velocity_text = wtext(text=myText)
myText = "\n\nFriction_______:"+str(friction)
friction_text = wtext(text=myText)
myText = '\n\nStiffness______:'+str(spring.stiffness)
stiffness_text = wtext(text=myText)


new_prop_text = wtext(text="<h3>Set new properties</h3>")

myScene.append_to_caption('Mass_________:')
getMass_Inp = winput(bind=getMass)
myScene.append_to_caption("\n\nStartVelocity___:")
getStartVelocity_Inp = winput(bind=getStartVelocity)
myScene.append_to_caption('\n\nFriction_______:')
getFriction_Inp = winput(bind=getFriction)
myScene.append_to_caption('\n\nStiffness______:')
getStiffness_Inp = winput(bind=getStiffness)
myScene.append_to_caption('\n\n')

change_but = button(bind=ChangeProperties,text="Set properties",color=color.white, background=color.blue)

# ____________________________________________________________

# ___________________________Graphs__________________________

wtext(text="\n\n")
wtext(text="<p style=\"color: green;margin-top: 0px;font-size: 20px;\">"+"_"*500+"\n"+"</p>")

graph_1 = graph(fast = False,xtitle='<i><b>Time</b></i>', ytitle='<i><b>Velocity</b></i>',align="left")
graph_2 = graph(fast = True,xtitle='<i><b>Time</b></i>', ytitle='<i><b>Acceleration</b></i>',align="right")
f1 = gcurve(color=color.blue,label="Velocity",graph=graph_1)
f2 = gcurve(color=color.red,label="Acceleration",graph=graph_2)
f1.plot(0,myObj.velocity.x)
f2.plot(0,0)



# ____________________________________________________________

# ___________________________Physics__________________________
t = 0
dt = 0.01
start_pos = myObj.pos.x
a = 0
def Animation():
    global a,t,timeToBreak

    while True:
        if isRunning:
            rate(60)

            dx =  myObj.pos.x - start_pos
            if myObj.velocity.x > 0.1:
                coef = 1
            elif myObj.velocity.x < -0.1:
                coef = -1
            else:
                coef = 0


            a = (-friction*coef-spring.stiffness*dx)/myObj.mass

            myObj.velocity.x = myObj.velocity.x + a * dt

            myObj.pos.x += myObj.velocity.x * dt
            spring.axis = myObj.pos - spring.pos
            f1.plot(t, myObj.velocity.x)
            f2.plot(t, a)
            t += dt
            if myObj.velocity.x < 0.1 and myObj.velocity.x > -0.1 and a < 0.1 and a > -0.1:
                Run()

# ____________________________________________________________


# _______________________Description__________________________
wtext(text="<p style=\"color: green;margin: 0px;  top: 910px;position: absolute;  font-size: 20px;\">"+("_"*500)+"</p>")

# ____________________________________________________________
Animation()


