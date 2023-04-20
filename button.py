import sys 
import pygame as pg
pg.init()

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,r = 0,g = 0,b = 0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.R = r
        self.G = g
        self.B = b
    def draw(self,screen):
        pg.draw.rect(screen,(self.R,self.G,self.B),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        mouse_x, mouse_y = pg.mouse.get_pos() #[100,200]
        if mouse_x >= self.x and mouse_x <= self.x + self.w and mouse_y >= self.y and mouse_y <= self.y + self.h:
            return True
        else:
            return False
        pass
    def isclick(self):
        if pg.mouse.get_pressed()[0] :
            return True
        else :
            return False

win_x = 800
win_y = 400
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(1):
    screen.fill((255, 255, 255))
    if btn.isMouseOn():
        if btn.isclick(): # can be replace by if pg.mouse.get_pressed()[0] :
            # btn.w = 100
            # btn.h = 100
            btn.R = 128
            btn.G = 0
            btn.B = 128
        else :
            # btn.w = 100
            # btn.h = 100
            btn.R = 128
            btn.G = 128
            btn.B = 128
    else:
        # btn.w = 100
        # btn.h = 100
        btn.R = 200
        btn.G = 0
        btn.B = 0
    btn.draw(screen)

    pg.display.update()
    pg.time.delay(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    
