from pygame import *

FPS = 60
WIDTH = 800
HEIGHT = 600
image_x = 30
image_y = 140

window = display.set_mode((WIDTH,HEIGHT))
display.set_caption('Игра')
 
bg = transform.scale(image.load('58.png'), (WIDTH,HEIGHT))

image = Surface((30, 140))
image.fill((0, 0, 0))
rect = image.get_rect()
bg.blit(image, (20,50))

game = True
while game:
    window.blit(bg,(0,0))


    for e in event.get():
        if e.type == QUIT:
            game = False
            image.update


    clock = time.Clock()
    clock.tick(FPS)
    display.update()

