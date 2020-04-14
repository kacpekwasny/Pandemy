import Pandemy
import turtle
e = exit

s = turtle.getscreen()
print(turtle.speed(10))

kacper = Pandemy.models.person.Person({"pid":19, "age":13, "trt":True})


def mv(a, **_dict):
    for i in range(a):
        DONE = kacper.move(**_dict)
        if DONE:
            return True
        #print("cords: ", kacper.cords)

def test(ile, a, **_dict):
    const = 0
    xx = int(ile**(1/2))
    x = 0
    for il in range(xx):
        y = 0
        for ill in range(xx):
            const += 1/ile
            _dict.update({"area":((x, x+40/xx), (y, y+40/xx)), "const":const})
            DONE = mv(a, **_dict)
            if DONE:
                return "Done"
            y += 40/xx
        x += 40/xx