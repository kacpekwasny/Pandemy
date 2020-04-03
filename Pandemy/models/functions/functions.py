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