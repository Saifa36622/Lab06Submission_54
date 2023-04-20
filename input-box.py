import sys
import pygame as pg
pg.init()

win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)
font = pg.font.Font('freesansbold.ttf', 32)

#####################################

first = font.render('Firstname', True, (0,0,0))
firstRect = first.get_rect()
firstRect.center = (120,80)

last = font.render('lastname', True, (0,0,0))
lastRect = last.get_rect()
lastRect.center = (120,180)


age = font.render('age', True, (0,0,0))
ageRect = last.get_rect()
ageRect.center = (120,280)

submit = font.render('submit', True, (0,0,0))
subRect = submit.get_rect()
subRect.center = (425,400)


font2 = pg.font.Font('freesansbold.ttf', 32)
error = font2.render('Please enter number', True, (255,0,0))
errorRect = error.get_rect()
errorRect.center = (475,320)

####################################

class InputBox:
    def __init__(self, x, y, w, h, text='',wow = ''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.wow = wow
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    # collect = ""
                    # collect += self.text
                    print(self.text)
                    self.wow = self.text
                    # print(collect)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
    def re_collect(self):
        return self.wow
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

class InputBoxage:
    def __init__(self, x, y, w, h, text='', wow=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.wow = wow
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.error_displayed = False
        self.error_display_time = 0

    def handle_event(self, event):
        switchfor_age = 0
        if event.type == pg.MOUSEBUTTONDOWN:  # ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos):  # ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE  # เปลี่ยนสีของ InputBox

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    # collect = ""
                    # collect += self.text
                    print(self.text)
                    self.wow = self.text
                    # print(collect)
                    self.text = ''
                    if not self.wow.isnumeric():
                        print("hi")
                        self.error_displayed = True
                        self.error_display_time = pg.time.get_ticks()
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def re_collect(self):
        if not self.wow.isnumeric():
            self.wow = " ERROR "
        return self.wow

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
        # Check if error message should be displayed
        if self.error_displayed:
            current_time = pg.time.get_ticks()
            if current_time - self.error_display_time < 5000:  # Display error for 5 seconds
                screen.blit(error, errorRect)
            else:
                self.error_displayed = False


input_box1 = InputBox(100, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(100, 200, 140, 32) # สร้าง InputBox2
input_boxage = InputBoxage(100, 300, 140, 32)
input_boxes = [input_box1, input_box2, input_boxage] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย

##############################################################################

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
        mouse_x, mouse_y = pg.mouse.get_pos()
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
btn = Button(350,350,150,100)
switch = 0
x = 0
while (1):
    
    screen.fill((255, 255, 255))
    screen.blit(first, firstRect)
    screen.blit(last, lastRect)
    screen.blit(age, ageRect)
    if switch == 1:
        ans = font.render('Hello ' +input_box1.re_collect() +" "+input_box2.re_collect()+" !", True, (0,0,0))
        ansRect = ans.get_rect()
        ansRect.center = (550,150)
        screen.blit(ans, ansRect)


        ans2 = font.render("You are "+ input_boxage.re_collect()+" years old", True, (0,0,0))
        ans2Rect = ans2.get_rect()
        ans2Rect.center = (550,200)
        screen.blit(ans2, ans2Rect)
        # print("hi",x)
        # x+= 1
        # screen.blit(age, lastRect)
        # switch = 0
        

    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
    if btn.isMouseOn():
        if btn.isclick():
            # btn.w = 100
            # btn.h = 100
            btn.R = 255
            btn.G = 0
            btn.B = 0
            switch = 1
        else :
            # btn.w = 100
            # btn.h = 100
            btn.R = 128
            btn.G = 128
            btn.B = 128
    else:
        # btn.w = 100
        # btn.h = 100
        btn.R = 255
        btn.G = 255
        btn.B = 255
    pg.draw.rect(screen,(0,0,0),(340,340,170,120))
    btn.draw(screen)
    screen.blit(submit, subRect)
    firstname = input_box1.text

    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()

    pg.time.delay(1)
    pg.display.update()

    # class InputBoxage:
#     def __init__(self, x, y, w, h, text='',wow = ''):
#         self.rect = pg.Rect(x, y, w, h)
#         self.color = COLOR_INACTIVE
#         self.text = text
#         self.wow = wow
#         self.txt_surface = FONT.render(text, True, self.color)
#         self.active = False

#     def handle_event(self, event):
#         switchfor_age = 0
#         if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
#             if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
#                 # Toggle the active variable.
#                 self.active = not self.active
#             else:
#                 self.active = False
#             self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
#         if event.type == pg.KEYDOWN:
#             if self.active:
#                 if event.key == pg.K_RETURN:
#                     # collect = ""
#                     # collect += self.text
#                     print(self.text)
#                     self.wow = self.text
#                     # print(collect)
#                     self.text = ''
#                     if not self.wow.isnumeric():
#                         print("hi")
#                         screen.blit(error, errorRect)
#                         pg.time.delay(5000)
#                 elif event.key == pg.K_BACKSPACE:
#                     self.text = self.text[:-1]
#                 else:
#                     self.text += event.unicode
#                 # Re-render the text.
#                 self.txt_surface = FONT.render(self.text, True, self.color)
#     def re_collect(self):
#         return self.wow
#     def update(self):
#         # Resize the box if the text is too long.
#         width = max(200, self.txt_surface.get_width()+10)
#         self.rect.w = width

#     def draw(self, Screen):
#         # Blit the text.
#         Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
#         # Blit the rect.
#         pg.draw.rect(Screen, self.color, self.rect, 2)