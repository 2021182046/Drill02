from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
x, y = 400, 90
circle_r = 200
center_x, center_y = 400, 300

def move_circle(a):
    clear_canvas_now()
    grass.draw_now(400, 30)
    circle_y = center_y + ( math.cos(math.radians(a)) * circle_r )
    circle_x = center_x + ( math.sin(math.radians(a)) * circle_r )
    character.draw_now(circle_x, circle_y)
    delay(0.05)

def move_4way(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x,y)


while (1):
    a = 0
    # 사각 운동
    while (y < 550):
        while (x < 790):
            move_4way(x, y)
            x += 20
            delay(0.05)
        move_4way(x, y)
        y += 20
        delay(0.05)
    while (y > 90):
        while (x > 0):
            move_4way(x, y)
            x -= 20
            delay(0.05)
        move_4way(x, y)
        y -= 20
        delay(0.05)
    while (x < 400): #중심 이동 추가
        move_4way(x,y)
        x += 20
        delay(0.05)
    # 원 운동
    while (a < 360):
        move_circle(a)
        a += 5
    

close_canvas()
