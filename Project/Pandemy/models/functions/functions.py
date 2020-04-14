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

def oneD_randomwalk(reps):
    for i in range(reps):
        z = self.cords_zzz
        dir_z = self.dir_zzz
        dir_z = dir_z if random()>.95 else dir_z*(-1)
        mv = 0.2

        if random()>.7:
            if random()>.5:
                dir_z = dir_z + (1-(abs(dir_z)))*random()*const
            else:
                dir_z = dir_z - (1-abs(dir_z))*random()*const
        else:
            dir_z = dir_z + copysign((1-abs(dir_z))*random()*const, dir_z)
        mvz = dir_z*mv

        if   mvz+z> border_z_R:
            z = 2*border_z_R - mvz - z
        elif mvz+z< border_z_L:
            z = 2*border_z_L + mvz + z
        else:
            z += mvz

        vx, vy  = self.v_dir
        x, y    = self.cords
        vzz = -vx/vy


        self.dir_zzz, self.cords_zzz = dir_z, z