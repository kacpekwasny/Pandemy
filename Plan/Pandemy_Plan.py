# Ewentualne Pomysly:
# 1. Symulator bedzie wielo komputerowy wiec jakas komunikacja
#   synchronizacja, powalenie trudne!
#  


# Do ZROBIENIA:
# 1. Zapisywanie i przerywanie symulacji,   
# 2. Dzielenie terenu, kwarantanny lokalne,
#   odizolowane spolecznosci, a nie rodziny
# 3.  




# Rozwiazania?
# 1. petla oczywiscie, ktora sprawdza czy sa wcisniete odpowiednie klawisze
    # Jezeli sa to wlacza input() i wpisujemy komende,
    # ale pewnie trzeba by bylo czekac na ukonczenie symulacji dnia,
    # mozna by zapisywac do pliku komende jezeli nie mamy lepszego pomyslu
    #     
#  

# co musi zawierac symulacja?
# Powierzchnia!:
#   Powierzchnia miasta
#   Powierzchni calego terenu
#   Ile miast
#       Powierzchnia miast
#  
#   Ile domow
#       Powierrzchnia dzialki 
# 
# Osoby:
#   Ile w miesciee,
#   Ile poza piastem,
#       promien do ktorego beda sie rownomiernie rozkladali
#       albo brak promienia wtedy 
#  
#
#


class Simulation:
    def __init__(self, config, default_config):
        # W taki sposob bedzie zaciagany config
        # Bedzie config, ktory podajesz oraz wartosc defaultowa
        #  
        self.config1 = config["config1"] if "config1" in config else default_config["config1"]
        self.config2 = config["config2"] if "config2" in config else default_config["config2"]
        self.config3 = config["config3"] if "config3" in config else default_config["config3"]
        # ...


    # Przy rozpoczynaniu symulacji
    # beda generowane osoby domy itd
    # wszystko bedzie zalezalo od config i deafult 
    # oraz rowniez miasta, bo mozna zrobic np kraj
    # z 20 miastami, itd. ale mnie osob, wszystko w
    # osobnych thread itd.
    # im wiecej opcji tym lepiej 
    self.person_ls  = []
    self.home_ls    = []
    self.blok_ls    = []
    self.city_ls    = []



    def stop(self, ...):
        # mozna zatrzymac i zapisac uzywając pickle
        #  
        # 
        pass     

    # Droga
class Road:
    self.cords = ((start_x, start_y), (koniec_x, koniec_y)) # w srodku szerokosci
    self.width = 10 m # mamy prostokat
    self.pavement_width = 2 m

    def Cords_in_self():
        # takes
        pass


# Miasto
class City:
    self.home_ls = [Home(), Home()...]
    self.day_place_ls [Day_Place(), Day_Place()...]
    self.people_ls = [...]
    self.roads = ls[Road, Road]


    def gen_roads(length_min_max=(50 m, 300 m), ile_drog=500):
        # droga to asfalt taki od skrzyzowania do skrzyzowania
        # musi wziac dane configuracyjne i zwrocic liste obiektow drog 
        pass

    def gen_homes(area, numberof, etc..):
        for i in range(numberof):
            home_ls.append(Home.)
        
        pass




# Dzien i wszystkie czynnosci i zachowania luudzi i atrybuty z tym zwiazane
class Day:
    self.inne rozne atrybty
    self.social_awarness
    self.


class Day_Place:
    self.people_ls      # Ile osob nalezy do day place, ile osob tam pracuje, ile dzieci chodzi do szkoly
    self.infected       # float() jaka czesc jest zarazona budynku? float = osoby_zarazone/people_ls
    self.time_in_self   # Czas jaki spedza sie w tym miejscu

class School:
    def __init__(self, config):
        self
    pass



class Home:
    self.cords = (x, y)
    self.

class Blok:
    self.num_of_flats
    self.how_infected  = len(residents_infected)/len(residents)
    self.residents = people_ls[400:540] #np.
    self.residents_infected = [i for i in self.residents if i.infected]

    class Flat:
        self.area = ()  # Zakladamy ze to prostokat kiedy ktos wchodzi do domu to nie jest symolowane porusuzanie sie
                        # Nie moze byc zarazony z zew, a status wszystkich w domu jest taki sam czyli
                        # albo wszyscy zdrowi albo wszyscy chorzy
        self.infected




class Person:
    self.home = obiekt_home
    self.work = obiiekt_Day_Place
    self.social_distancing # kazdy ma swoj parametr
    self.day_schedule_ls = [[self.home.sleep()], [], []]
    self.cords = (x, y)         # (metry.cm, metry.cm) (float, float)
    self.infectable = False     # Bo np. jedzie samochodem
    self.radius_of_spread = const_spread*cos_bo_szybko_oddycha albo kaszle
    self.has_age_group = False


    # Configuruje osobe, co powinno byc robione zaraz po init
    # czy 

    def be_in_group(self, group_age_config):
        if not self.has_type:
            self.age = group_age_config["age"]
            self.death_risk = group_age_config["death_risk"]
            self.death_risk = self.death_risk*group_age_config["high_risk_multiply"] if random()>group_age_config["high_risk_probability"] else self.death_risk

            self.death
            pass



    def move_home(self, self.home):
        self.move(...)

    def move_in_day_place(self, day_place):
        self.move(parameter1=xxx, paramter2=y, ...)
    
    def move_drive(self, where = (x, y)):
        # Po co symlacja 1M osob ktore jezdza, skoro i tak sie nie zarazaja
        # gorzej jak sa w samochodzie razem, ale tutaj mozna dac zarazanie instant,
        #  
        # FUNCKJA WEZMIE WSZYSTKIE DROGI JAKIE SA
        # I ZROBI TRASE, Policzy ile zajmie przejechanie,
        # doda do osoby, ile jest wykluuczona z symulacji
        # i ustawi jej polozenie na cel, t 
        pass


    def move():
        # BARDZO WAZNA FUNCJA!!!
        # MUSI BYC PRZEMYSLANA, Z WIELOMA OPCJAMI,
        # Taki self.drive() bedzie bral move i zwracal
        # i puszczal move z specjalnymi opcjami 
        # move tot bedzie raw funcja ktora bedzie duzo umozliwiala
        #  
        pass


    def drive(self):
        pass


class Night:
    self.time #(steps)


    def people_sleep(self ,time):
        for human in people_ls:
            human.sleep(time) # time jest w steps
    






        # Oczywiscie do symulacji beedzie mniejszy obszar i mniej ludzi chyba ze by sie dalo odpalic to u kogos na komp
        #random people for work ile osob przyjezdza do miasta i wraca poza nie
        # 
krakow = Simulation(people=700k, obszar=(13 000 m, X 7 000 m), chorzy_start= np.: 10, illness_data=jakis_dict_config, random_people_for_work=50 000)

jakis_dict_config = {promien_zarazania:"2[metry]", }


