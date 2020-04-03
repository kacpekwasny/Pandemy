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
from functions.functions import full_config
# full config bierze dict config, i dict default_config,
# zwraca dict jako uzupelnienie config przez default config :) 


class Person:
    # kacper = Person({"pid":1, "age":17, "infected":True, "symptoms":False}, {"pid":0, "age":30, "infected":False, "symptoms":False, "config":"yes"})
    # config odpowiada za wprowadzenie danych, przygotowane configi dla mlodych starych itd..
    # Tym sposobem mozna wprowadzic ile sie chce atrybotow
    # CZYLI BARDZO BARDZO skalowalne!!!
    def __init__(self, config, def_config):
        self_config = full_config(config, def_config)
        for i, z in self_config.items():
            setattr(self, i, z)


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