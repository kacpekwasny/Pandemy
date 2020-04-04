from random import random
from math import sqrt, copysign
import turtle


SCREEN_SIZE = 800
vector = -400
SPEED = 10
FROM_DEST = 0.02
CHANCE_CHNG_DEST = 0.05

#(0;1)
SPREAD_CHANCE = 0.5
SPREAD_RADIUS = 0.01

class Person:
    def __init__(self, pid, **kwargs):
        self.pid = pid
        self.x = random()
        self.y = random()
        self.v_dir = (random(), random())
        self.infected = False
        self.is_alive = True
        self.inf_time = 0
        self.trt = False
        self.home = (self.x, self.y)
        self.work = (random(), random())
        self.goto_h_w = False #FALSE go to work, TRUE go to home
        if kwargs and "turtle" in kwargs:
            if kwargs["turtle"]:
                self.trt = True
                self.turtle = turtle.Turtle()
                trt = self.turtle
                trt.speed(SPEED)
                trt.color(0, (random()+0.3)/1.3, 1)
                trt.shapesize(0.7,0.7,0.7)
                trt.penup()
                trt.goto(self.home[0]*SCREEN_SIZE+vector, self.home[1]*SCREEN_SIZE+vector)
                if pendown:
                    trt.pendown()
    def __add__(self, other):
        if self.infected:
            x = self.x-other.x
            y = self.y-other.y
            r = sqrt(x*x+y*y)
            if r<SPREAD_RADIUS and not other.infected:
                if random()<SPREAD_CHANCE:
                    #print("Infecting other.pid: %d" %other.pid)
                    other.get_infected()
        return other.infected

    def __repr__(self):
        return str(self.pid) +"_"+ str(self.infected) 
    
    def move(self):
        x, y = self.x, self.y
        vx, vy = self.v_dir
    
        #SETS ACTUAL DESTINATION DEPENDING ON goto_h_w
        if not self.goto_h_w:   #False-work True-home
            dest_x, dest_y = self.work
            if debug:
                print("goto work", dest_x, dest_y)
        else:
            dest_x ,dest_y = self.home
            if debug:
                print("goto home", dest_x, dest_y)

        #PROBABILITY THAT PERSON WILL CHANGE DESTINATION IF 
        #HAS CAME CLOSE ENOUGH
        from_dest = sqrt(abs(x-dest_x)**2+abs(y-dest_y)**2)
        if from_dest<FROM_DEST:
            if 1-CHANCE_CHNG_DEST<random():
                self.goto_h_w = not self.goto_h_w
                if debug1:
                    print(self.goto_h_w)
        # PROBABILITY THAT vx nad vy will change directions
        dirx = -1 if random()>0.99 else 1
        diry = -1 if random()>0.99 else 1

        #const urozmaica roznorodnosc katow
        const = 0.2
        #mv to odleglosc skoku
        mv = 0.01

        #if sethome tries to get home and back
        if sethome:
            #vector to house: gx-go x, gy go-y
            gx, gy = dest_x-x, dest_y-y
            if debug:
                print(gx, gy)

            if gx>0:
                CHANGE_L_R = 1-(0.4+0.6*abs(gx))
                L_R = 1-(0.6+0.4*gx)
            elif gx==0:
                CHANGE_L_R = 0.8
                L_R = 0.5
            else:
                CHANGE_L_R = 1-(0.4+0.6*abs(gx))
                L_R = 0.6+0.4*(-gx)

            if gy>0:
                CHANGE_U_D = 1-(0.4+0.6*abs(gy))
                U_D = 1-(0.6+0.4*gy)
            elif gy==0:
                CHANGE_U_D = 0.8
                U_D = 0.5
            else:
                CHANGE_U_D = 1-(0.4+0.6*abs(gy))
                U_D = 0.6+0.4*(-gy)

            #L_R = 0.2 20% LEFT 1-0.2 RIGHT
            #U_D = 0.2 20% UP   1-0.2 DOWN

        else:
            CHANGE_L_R = 0.7
            CHANGE_U_D = 0.7
            U_D = 0.5
            L_R = 0.5

        if random()>CHANGE_L_R:
            #
            if random()<L_R:    #LEFT
                #Changes speed randomly between -1;1
                v = (vx - random()*const*abs(-1-vx))
                mvx = dirx * mv * v
                vx = copysign(v, mvx)
            else:               #RIGHT
                #Changes speed randomly between -1;1
                v = (vx + random()*const*abs(1-vx))
                mvx = dirx * mv * v
                vx = copysign(v, mvx)
        else:
            mvx = dirx * mv *(vx + copysign(random()*const*(copysign(1, vx)-abs(vx)), vx))

        if random()>CHANGE_U_D:
            if random()>U_D:    #UP
                #Changes speed randomly between -1;1
                v = (vy + random()*const*abs(1-vy))
                mvy = diry * mv * v
                vy = copysign(v, mvy)
            else:               #DOWN
                #Changes speed randomly between -1;1
                v = (vy - random()*const*abs(-1-vy))
                mvy = diry * mv * v
                vy = copysign(v, mvy)
        else:
            mvy = diry * mv *(vy + copysign(random()*const*(copysign(1, vx)-abs(vy)), vy))


        # Move for x in <0;1> SAEFTY stop
        if mvx+x>1:
            x=2-mvx-x
            vx = vx*(-1)
        elif mvx+x<0:
            x=-mvx-x
            vx = vx*(-1)
        else:
            x = mvx+x

        # Move for y in <0;1>
        if mvy+y>1:
            y=2-mvy-y
            vy = vy*(-1)
        elif mvy+y<0:
            y=-mvy-y
            vy = vy*(-1)
        else:
            y = mvy+y

        self.x, self.y = x, y
        #For turtle
        if self.trt:
            self.turtle.goto(x*SCREEN_SIZE+vector, y*SCREEN_SIZE+vector)
            #self.turtle.stamp()
        #Randomness of velocity random velocity
        self.v_dir = (vx, vy)

    def get_infected(self):
        if not self.infected:
            if self.trt:
                self.turtle.color(1, 0, 0)
            self.infected = True


# Return relaoded ls
def infect(k, ls):
    ret = []
    infected = [i for i in ls if i.infected]
    #print("infected", infected)
    uninfected = [i for i in ls if not i.infected]
    if printing:
        print(k, len(infected), len(uninfected))
    #print("uninfected", uninfected)
    for i in infected:
        c = len(uninfected)-1
        while c >= 0:
            d = uninfected[c]
            i+d
            if d.infected:
                infected.append(uninfected.pop(c))
            c = c-1
    ret.extend(infected)
    ret.extend(uninfected)
    #print("return", ret)
    return ret

    #print("infected should be all",[i for i in infected])
    #print("uninfected should be some",[i for i in uninfected])

def list_no_self(ls, ob):
    ret = [x for x in ls if x.pid!=ob.pid]
    return ret

def action(k, ls):
    for i in range(k):
        ln = len([i for i in ls if not i.infected])
        if ln>0:
            ls = infect(i, ls)
            for m in ls:
                m.move()    
            #if turtle_bl:
                #turtle.update()
    ls_inf = sorted([i for i in ls if i.infected], key=lambda x: x.pid)
    #print(ls_inf)
    return len(ls_inf)

def main(n, ls):
    return action(n, ls)


if __name__ == "__main__":

    people = 100
    #one step is up to 10m, it will be
    steps = 500
    measurments = 5
    a = 0

    turtle_bl   = False      #graficzne przedstawienie
    infection   = True      #zarazona pierwsza osoba
    pendown     = True      #linie
    sethome     = True      #Sethome, has work and home and usualy tires to go there
    printing    = False      #ZARAZENIE, krok
    debug       = False      #gx, gy, go to
    debug1      = False      #Change of go_to
    showoff_h_w = False      #Show 0.01,0.01 home and oposite work

    if turtle_bl:

        s = turtle.getscreen()
        #turtle.mainloop()
        #turtle.tracer(0, 0)
    
        for k in range(measurments):
            ls = [Person(i, turtle=True) for i in range(people)]
            if infection:
                ls[0].get_infected()
            if showoff_h_w:
                ls[0].work = (0.99,0.99)
                ls[0].home = (0.01,0.01)
            v = main(steps, ls)
            print(v)
            a += v
    
    else:
        for k in range(measurments):
            ls = [Person(i) for i in range(people)]
            if infection:
                ls[0].get_infected()
            v = main(steps, ls)
            print(v)
            a += v
    a = a/measurments
    print(a)
    if turtle_bl:
        input()