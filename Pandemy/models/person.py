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

from functions.functions import away_from
from ..config_and_instructions.person_config import disease_config

class Person:
    # kacper = Person({"pid":1, "age":17, "infected":True, "symptoms":False}, {"pid":0, "age":30, "infected":False, "symptoms":False, "config":"yes"})
    # config odpowiada za wprowadzenie danych, przygotowane configi dla mlodych starych itd..
    # Tym sposobem mozna wprowadzic ile sie chce atrybotow
    # CZYLI BARDZO BARDZO skalowalne!!!
    def __init__(self, config):
        # type(config) = dict !!!
        self.pid = None

        # Atrybuty personalne majace znaczenie dla zarazania
        #    
        self.age = None             # wiek 
        self.infected = False       # zarazony, umycie rak nic nie da
        self.time_infected = 0      # czas od zarazenia, po X czasu pojawiaja sie symptomy albo i nie 
        self.symptoms = False       # czy ma symptomy 
        self.cords = (0.00, 0.00)   # koordynaty
                                    #  
        self.infecting = False      # czy zaraza? 
        self.dirty = 0              # czy jest zabrudzdona wirusami to moz 
        self.dirty_hands = False    # czy ma brudne rece? bedzie zakazala, klamki itp.: wykorzystaj to do swojej symulacji
        self.death_chance = None    # szansa na smierc w zaleznosci od wieku i ewentualnych powiklan zdrowotnych 

        # te atrybuty sa od  
        self.home = None            # dom jako obiekt
        self.day_place = None       # miejsce gdzie sie na ogol w dzien siedzi    
        self.day_plan_array = []
        self.time_in_place = 0
        self.max_time_in_place = None
        for i, z in config.items():
            setattr(self, i, z)

    def __repr__(self):
        return "pid: {}, age: {}, infected: {}, death chance: {}".format(self.pid, self.age, self.infected, self.death_chance)

    

    def infect_in_radius(self, other):
        if self.infected and away_from(self, otther)<:
            if random()

    # kiedy bedziemy robili symulacje miejsc pracy itd 
    def move(self, **options):
        # {"random":"full/places"
        #   }  
        if "random" in options:
            # moves in random
            if "full" == options["random"]:
                randomness = 1
                pass
            
            if "palces"
                pass

            pass

        if "area" in options:
            # moves in that area ((x1, x2), (y1, y2))
            pass

        if "destination" in options:
            # finds roads that lead to destination 
            # and  makes a list, calculates time needed (x = steps)
            # self is excluded from simulation for next x steps,
            # self.coords = (x, y) 
            pass
        
        speed = options["speed"] if "speed" in options else move_default["speed"]