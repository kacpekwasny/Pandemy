from math import sqrt
# Takes dict, dict
# Returns overlap of them 
def full_config(conf, def_conf):
    # Bierze dict conf i dict def_conf
    # zwraca uzupelnienie conf przez def_conf 
    # bez powtorzen :) 
    ret = conf
    for i, z in def_conf.items():
        print(i, z)
        if not (i in conf):
            print("update", i)
            ret.update([(i, z)])
    return ret

def away_from(_self, _other):
    # takes object or (x, y)
    # object has to have .cords
    # returns how far is other
    try:
        sx, sy = _self.cords
    except:
        sx, sy = _self

    try:
        ox, oy = _other.cords
    except:
        ox, oy = _other

    l = sqrt((ox-sx)**2 + (oy-sy)**2)
    return l