person_default_config = {"pid":None, "age":None, "infected":False, "symptoms":False, "home":None, "day_place":None, "day_plan_array":None, "time_in_place":0, "max_time_in_place":None,
                    "time_infected":0, "infecting":False, "dirty":0, "death_chance":None}

# config __init__
# config = {"pid":13, "age":23, "infected":False, "symptoms":False, "home":home_ls[34], "cords":home_ls[34].cords, "day_place":day_place[42],
#           "day_plan_array":None, "time_in_place":0, "max_time_in_place":None, "time_infected":0, "infecting":False, "dirty":0, "death_chance":None}

person_disease_config = {"infection_radius":2.0, "air_radius_spread_chance":1.0, "infection_from_dirty_hands":5.0, "infection_from_dirty":2.0}


person_move_config = {"chnc_chng": 0.4, "corct_turn": 0.6, "chnc_fast_chng":0.999, "move_radius":0.01,
                    "mv":0.2, "const":0.01, "defa_chng_lr_ud":0.7, "defa_chnc_lr_ud":0.5}