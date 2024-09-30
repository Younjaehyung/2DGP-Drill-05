from pico2d import *
#from pygame.examples.sprite_texture import running

open_canvas(1280,1024)

character = load_image('Character_sheet5.png')
background = load_image('TUK_GROUND.png')


running = True
x = 800 // 2
y=600//2
framex=0
framey=0
dirx=0
diry=0

def handle_events():
    global running
    global x,dirx,diry
    # fill here

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            if event.key == SDLK_LEFT:
               dirx=dirx-1
            if event.key == SDLK_RIGHT:
                dirx=dirx+1
            if event.key == SDLK_UP:
                diry=diry+1
            if event.key == SDLK_DOWN:
                diry=diry-1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx=dirx-1
            if event.key == SDLK_LEFT:
                dirx=dirx+1
            if event.key == SDLK_DOWN:
                diry=diry+1
            if event.key == SDLK_UP:
                diry=diry-1


        # fill here

def draw_events():
    global framex,framey
    global dirx,diry

    if framey == 4:
        if framex == 4:
            framex = 0

    if dirx==0 and diry==0:
        framey=4
        character.clip_draw(framex * 125, 0, 125, 180, x, y, 200, 200)
        return
    elif dirx==0 and diry==1:   #위
        framey=0
    elif dirx==0 and diry==-1:  #아래
        framey=1
    elif dirx==1 and diry==0:   #오른쪽
        framey=3
    elif dirx==-1 and diry==0:  #왼쪽
        framey=2

    character.clip_draw(framex * 62, (framey*64)+180, 62, 64, x, y, 200, 200)

def move_character():
    global x,y
    x += dirx * 5
    y += diry * 5

    if x - 50 < 0:
        x += 5
    elif x + 50 > 1280:
        x -= 5

    if y - 50 < 0:
        y += 5
    elif y + 50 > 1024:
        y -= 5


# fill here
while running:
    clear_canvas()
    background.draw(640,512)
    draw_events()
    update_canvas()
    handle_events()
    move_character()

    framex = (framex+1)%8


    delay(0.05)

close_canvas()

