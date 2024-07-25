import pgzrun, random

TITLE="Illusion"
WIDTH=300
HEIGHT=300

def draw():
    r=255
    g=0
    b=random.randint(0,255)
    radius=20
    for i in range(20):
        screen.draw.circle((150, 150), radius, (r, g, b))
        r-=10
        g+=10
        radius+=10



pgzrun.go()