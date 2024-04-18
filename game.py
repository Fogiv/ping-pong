from pygame import *
init()
window = display.set_mode((700,500))
window.fill((12,17,19))
bg = transform.scale(image.load("1660748860_3-flomaster-club-p-nastolnii-tennis-kartinki-dlya-detei-krasi-7.jpg"),(700,500))

class Rocket():
    def __init__(self, img, x , y, width_rocket, hight_rocket, speed):
        self.image = transform.scale(image.load(img),(width_rocket,hight_rocket))
        self.image_hit = self.image.get_rect()
        self.image_hit.x = x
        self.image_hit.y = y
        self.speed = speed 
    def show_s(self):
        window.blit(self.image, (self.image_hit.x,self.image_hit.y))
class Rocket_player1(Rocket):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] :
            self.image_hit.y -= self.speed
        if keys[K_s] :
            self.image_hit.y += self.speed

ball = Rocket("yyy.png" , 200 , 200 , 70 , 70 , 4)


class Rocket_player2(Rocket):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] :
            self.image_hit.y -= self.speed
        if keys[K_DOWN] :
            self.image_hit.y += self.speed

rocket1 = Rocket_player1("player.png", 30,22 ,25, 250,3)
rocket2 = Rocket_player2("player 2.png", 654, 223, 25, 250,3)

speed_x = 3
speed_y = 3
fps = time.Clock()
run = True
while run:
    for i in event.get():
        if i.type == QUIT: 
            run = False
    window.blit(bg,(0,0))    
    rocket1.show_s()
    rocket1.update_l()   
    rocket2.show_s()
    rocket2.update_r()  
    ball.show_s()

    ball.image_hit.x += speed_x
    ball.image_hit.y += speed_y
    
    if sprite.collide_rect(rocket1 , ball) or sprite.collide_rect(rocket2 , ball):
        speed_x *= -1
        speed_y *= -1
    if ball.image_hit.y < 10:
        speed_y *= -1
    if ball.image_hit.y > 470:
        speed_y *= -1





    display.update()
    fps.tick(120)