# Notatki:
# Get_infected: 
# chance of getting infected every time
# for eample touches infected handle
# from now on until self washes hands self will be infecting,
# ergo can infect himself antil washes hands   
#    
#   
#   
# Become_infecting:
# self has infected hands
# after every move self will get viruses on clothes  
#    
# probably every move 
#  
#  
# 
# Desinfect self: 
# if self was infecting self is not infecting 
#  
#  
#  
#  
# from functions.functions import full_config
# nie uzywany import aktualnie
# full config bierze dict config, i dict default_config,
# zwraca dict jako uzupelnienie config przez default config :) 

from numpy import arctan
from random import random, randrange, choice
from math import copysign
import turtle


from .functions.functions import away_from
from ..config_and_instructions.person_config import *

SCREEN_SIZE = 20
vector = -100
debug = True

class Person:
    # kacper = Person({"pid":1, "age":17, "infected":True, "symptoms":False}, {"pid":0, "age":30, "infected":False, "symptoms":False, "config":"yes"})
    # config odpowiada za wprowadzenie danych, przygotowane configi dla mlodych starych itd..
    # Tym sposobem mozna wprowadzic ile sie chce atrybotow
    # CZYLI BARDZO BARDZO skalowalne!!!
    def __init__(self, config):
        # type(config) = dict !!!
        self.pid = None

        # Atrybuty personalne majace znaczenie dla zarazania
        # osobiste atrybuty    
        self.age = None             # wiek 
        self.infected = False       # zarazony, umycie rak nic nie da
        self.time_infected = 0      # czas od zarazenia, po X czasu pojawiaja sie symptomy albo i nie 
        self.symptoms = False       # czy ma symptomy 
        self.cords = (0.00, 0.00)   # koordynaty
        self.v_dir = (0.00, 0.00)
        
        self.dir_zzz = random()
        self.cords_zzz = 0

        # te atrybuty sa od infekcji  
        self.infecting = False      # czy zaraza? 
        self.dirty = 0              # czy jest zabrudzdona wirusami to moz 
        self.dirty_hands = False    # czy ma brudne rece? bedzie zakazala, klamki itp.: wykorzystaj to do swojej symulacji
        self.death_chance = None    # szansa na smierc w zaleznosci od wieku i ewentualnych powiklan zdrowotnych 

        # te atrybuty sa od symulacji dnia i czynnosci 
        self.home = None            # dom jako obiekt
        self.day_place = None       # miejsce gdzie sie na ogol w dzien siedzi    
        self.day_plan_array = []
        self.time_in_place = 0
        self.max_time_in_place = None

        # dodatkowe atrybuty
        self.trt = False            # do wizualizacji chodzenia wlasciwie to DEBUGowa funkcja albo do prezentacji 

        # nadpisywanie defaultowych atrybutow
        # MUSI BYC NA KONCU !!!!!!
        # w przeciwnym wypadku pozostanie defaultowy!!!! 
        for i, z in config.items():
            setattr(self, i, z)

        if self.trt:
            self.turtle = turtle.Turtle()
            self.turtle.penup()
            self.turtle.goto(self.cords[0]*SCREEN_SIZE+vector, self.cords[1]*SCREEN_SIZE+vector)
            self.turtle.pendown()
            self.turtle.color(random(), random(), random())

    def __repr__(self):
        return "pid: {}, age: {}, infected: {}, death chance: {}".format(self.pid, self.age, self.infected, self.death_chance)

    def infect_in_radius(self, other, *radius):
        # other zaraza sie od self,
        # self nie zaraza sie od other
        # zawsze trzeba puscic dwa self.infect_in_radius(other)
        # i other.infect_in_radius(self)
        if self.infected and away_from(self, otther) < radius[0] if radius else disease_config["infection_radius"]:
            if random()<disease_config["air_radius_spread_chance"]: # albo dodac ze
                other.infected = True

    # kiedy bedziemy robili symulacje miejsc pracy itd
    #  
    # move to cords, po prostu rusz się do wybranych koordynatów
    # 
    # move in line with max step, step to jest przemieszczenie podczas jednej tury, 
    #   jezeli godzina ma 1000 tur to jedna tura trwa 3.6 sekuundy
    #   wiec racjonalne przemieszczenie to bedzie z 4/5 metrow 
    #  
    # random in area, przypadkowy ruch w jakims prostokacie
    #   step = *czyli predkosc*, jak bez step to default
    #   proportional = *czyli czy po krotszym boku chodzi proporcjonalnie wolniej*
    #   dzieki temu nie wpada w sciany i sie nie odbija jak pinball      
    #  
    # random in line chodzi po lini w lewo i prawo przypadkowo   
    # 
    # random: True/False (przypadkowo chodzi / idzie do celu ), lista alejek i chodzi przypadkowo po alejkach
    {"area":((5543, 5545), (120, 124)), "destination":(5543, 124), "line":(20, 21),
    "right_angle_only":"x/y", "line_random_radius":(5, ("starting cords")) }
    def move(self, **options):
        x, y = self.cords
        vx, vy = self.v_dir
        # do configu zmienne:
        chnc_chng       = options["chnc_chng"]      if "chnc_chng"      in options else person_move_config["chnc_chng"]
        corct_turn      = options["corct_turn"]     if "corct_turn"     in options else person_move_config["corct_turn"]
        move_radius     = options["move_radius"]    if "move_radius"    in options else person_move_config["move_radius"]
        mv              = options["mv"]             if "mv"             in options else person_move_config["mv"]
        const           = options["const"]          if "const"          in options else person_move_config["const"]
        chnc_fast_chng  = options["chnc_fast_chng"] if "chnc_fast_chng" in options else person_move_config["chnc_fast_chng"]

        if "random" in options:
            # moves in random
            if "full" == options["random"]:
                randomness = 1
                pass
            
            if "palces":
                pass

            pass

        # chodzenie po linii do celu
        elif "line" in options:
            dest_x, dest_y = options["line"]
            gx, gy = dest_x-x, dest_y-y

            if gx==0 and gy==0:
                return True

            # FOR LINE and border
            if "line_random_radius" in options:
                sx, sy = options["line_random_radius"][1]
                if debug:
                    print("sx, sy: ", sx, sy)
                LRx = sy if options["right_angle_only"]=="x" else dest_y
                LRy = sx if options["right_angle_only"]=="y" else dest_x

                border = options["line_random_radius"][0]
                border_R, border_L =    LRy + border,     LRy - border
                border_U, border_D =    LRx + border,     LRx - border
                # side_steps = options["side_steps"] if "side_steps" in options else person_move_config["side_steps"]
                
            else:
                border = 0
            
            if debug:
                print("x, y:", x, y)
                print("vx, vy: ", vx, vy)
                print("gx, gy: ", gx, gy)
                if "line_random_radius" in options:
                    print("LR: ", LRx, LRy)
                    print("borders U_D: ", border_U, border_D)
                    print("borders_R_L: ", border_R, border_L)

            # Chodzenie po pionie i poziomie
            if "right_angle_only" in options:
                if options["right_angle_only"].lower() =="y":
                    if abs(gy)<=border:
                        mvx = copysign(mv, gx) if abs(gx)>mv else gx
                        mvy=0
                        side = "x"
                    else:
                        mvy = copysign(mv, gy) if abs(gy)>mv else gy
                        mvx=0
                        side = "y"

                elif options["right_angle_only"].lower( )=="x":
                    if abs(gx)<=border:
                        mvy = copysign(mv, gy) if abs(gy)>mv else gy
                        mvx = 0
                        side = "y"

                    else:
                        mvx = copysign(mv, gx) if abs(gx)>mv else gx
                        mvy=0
                        side = "x"

                else:
                    print("Wrong config Error!")
                    print(""" Wrong config in Person().move(right_angle_only='x'or'y') """)
                    print("Error you have used wrong atribute in right_angle_only direction indication!")
                    exit()

                #if debug:
                #    print("abs(gx) debug gx %f, gy %f, mv*2 %f" %(gx, gy, mv*2))
                #    print("abs(gx)<mv*2: ", (abs(gx)<mv*2 or abs(gy)<mv*2))


                if "line_random_radius" in options and not (abs(gx)<border*1.01 and abs(gy)<border*1.01):
                    if side=="x":
                        if random()>.3:
                            if random()>.5:
                                vy = vy*const + (1-(abs(vy)))*random()*const
                            else:
                                vy = vy*const - (1-abs(vy))*random()*const
                        else:
                            vy = vy*const + copysign((1-abs(vy))*random()*const, vy)
                        mvy = mvy + vy*mv

                    if side=="y":
                        if random()>.7:
                            if random()>.5:
                                vx = vx*const + ((abs(1-vx)))*random()*const
                            else:
                                vx = vx*const - (abs(-1-vx))*random()*const
                        else:
                            vx = vx*const + copysign((1-abs(vx))*random()*const, vx)
                        mvx = mvx + vx*mv

                    if debug:
                        print("side steps: ", mvx if side=="y" else mvy)

                if abs(gx)<border*1.01 and abs(gy)<border*1.01:
                    mvy = copysign(mv, gy) if abs(gy)>mv else gy
                    mvx = copysign(mv, gx) if abs(gx)>mv else gx

                
            else:
                if abs(gx)>abs(gy):
                    steps = gx/mv
                    mvgy=gy/steps
                    mvx = copysign(mv, gx) if abs(gx)>mv else gx
                    mvy = copysign(mvgy, gy) if abs(gy)>mvgy else gy
                else:
                    steps = gy/mv
                    mvgx = gx/steps
                    mvy = copysign(mv, gy) if abs(gy)>mv else gy
                    mvx = copysign(mvgx, gx) if abs(gx)>mvgx else gx

            
                if "line_random_radius" in options:
                    if gx==0:
                        pass
                    else:
                        pass

        
                else:
                    pass

            if debug:
                print("mv: ", mvx, mvy)
                print("side: ", side)

            # Stay in radius and move
            if "line_random_radius" in options:
                if side=="y":    
                    if x+mvx>border_R:
                        x= border_R- border*0.01 
                        vx = -1*vx
                    elif x+mvx<border_L:
                        x= border_L+ border*0.01 
                        vx = -1*vx
                    else:
                        x+=mvx
                    y += mvy

                if side=="x":
                    if y+mvy>border_U:
                        y= border_U- border*0.01
                        vy = -1*vy
                    elif y+mvy<border_D:
                        y= border_D+ border*0.01
                        vy = -1*vy
                    else:
                        y+=mvy
                    x+=mvx
            
            else:
                x += mvx
                y += mvy


        elif "area" in options:
            # moves in that area ((x1, x2), (y1, y2))
            # PROBABILITY THAT vx nad vy will change directions
            dirx = -1 if random()>chnc_fast_chng else 1
            diry = -1 if random()>chnc_fast_chng else 1

            #if sethome tries to get home and back
            if "destination" in options:
                dest_x, dest_y = options["destination"][0], options["destination"][1]
                #vector to house: gx-go x, gy go-y
                gx, gy = dest_x-x, dest_y-y
                gx, gy = copysign(abs(arctan(gx*move_radius))/1.5707963267948966, gx), copysign(abs(arctan(gy*move_radius))/1.5707963267948966, gy)
                if debug:
                    print(gx, gy)

                if gx>0:
                    CHANGE_L_R = 1-(chnc_chng+(1-chnc_chng)*abs(gx))
                    L_R = 1-(corct_turn+(1-corct_turn)*gx)
                elif gx==0:
                    CHANGE_L_R = 0.8
                    L_R = 0.5
                else:
                    CHANGE_L_R = 1-(chnc_chng+(1-chnc_chng)*abs(gx))
                    L_R = corct_turn+(1-corct_turn)*(-gx)

                if gy>0:
                    CHANGE_U_D = 1-(chnc_chng+(1-chnc_chng)*abs(gy))
                    U_D = 1-(corct_turn+(1-corct_turn)*gy)
                elif gy==0:
                    CHANGE_U_D = 0.8
                    U_D = 0.5
                else:
                    CHANGE_U_D = 1-(chnc_chng+(1-chnc_chng)*abs(gy))
                    U_D = corct_turn+(1-corct_turn)*(-gy)

                #L_R = 0.2 20% LEFT 1-0.2 RIGHT
                #U_D = 0.2 20% UP   1-0.2 DOWN

            else:
                # CHANGE_L_R and _U_D is the  1-x  probability of occuring a change
                CHANGE_L_R  = options["chng_lr"] if "chng_lr" in options else 0.7
                CHANGE_U_D  = options["chng_ud"] if "chng_ud" in options else 0.7

                # turn D is x, turn U is 1-x
                U_D         = options["turn_ud"] if "turn_ud" in options else 0.5

                # turn L is x, turn R is 1-x
                L_R         = options["turn_lr"] if "turn_lr" in options else 0.5

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


            # Move for x in <area> SAEFTY stop
            if mvx+x>   options["area"][0][1]:
                x=2*options["area"][0][1] -mvx-x
                vx = vx*(-1)
            elif mvx+x< options["area"][0][0]:
                x=2*options["area"][0][0]-(mvx+x)
                vx = vx*(-1)
            else:
                x = mvx+x

            # Move for y in <area>
            if mvy+y>   options["area"][1][1]:
                y=2*options["area"][1][1]-mvy-y
                vy = vy*(-1)
            elif mvy+y< options["area"][1][0]:
                y=2*options["area"][1][0]-mvy-y
                vy = vy*(-1)
            else:
                y = mvy+y


        elif "destination" in options:
            # finds roads that lead to destination 
            # and  makes a list, calculates time needed (x = steps)
            # self is excluded from simulation for next x steps,
            # self.coords = (x, y) 
            # moves in that area ((x1, x2), (y1, y2))
        
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
                    CHANGE_L_R = 1-(chnc_chng_lr+(1-chnc_chng_lr)*abs(gx))
                    L_R = 1-(crct_turn+(1-crct_turn)*gx)
                elif gx==0:
                    CHANGE_L_R = 0.8
                    L_R = 0.5
                else:
                    CHANGE_L_R = 1-(chnc_chng_lr+(1-chnc_chng_lr)*abs(gx))
                    L_R = crct_turn+(1-crct_turn)*(-gx)

                if gy>0:
                    CHANGE_U_D = 1-(chnc_chng_lr+(1-chnc_chng_lr)*abs(gy))
                    U_D = 1-(crct_turn+(1-crct_turn)*gy)
                elif gy==0:
                    CHANGE_U_D = 0.8
                    U_D = 0.5
                else:
                    CHANGE_U_D = 1-(chnc_chng_lr+(1-chnc_chng_lr)*abs(gy))
                    U_D = crct_turn+(1-crct_turn)*(-gy)

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

        self.v_dir = vx, vy
        self.cords = x, y
        #For turtle
        if self.trt:
            self.turtle.goto(self.cords[0]*SCREEN_SIZE+vector, self.cords[1]*SCREEN_SIZE+vector)
            #self.turtle.stamp()
        # speed = options["step"] if "step" in options else move_default["step"]