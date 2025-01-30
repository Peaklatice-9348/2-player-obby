import pygame
import os
pygame.init()
WIDTH = 900
HEIGHT = 500
SWIDTH = 55
SHEIGHT = 40

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('2 player obby!!!')

#loading images
cooldown1 = 0
cooldown2 = 0
player1 = pygame.image.load('2 player obby!!!/images/Player1.png')
player2 = pygame.image.load('2 player obby!!!/images/Player2.png')
bgbg = pygame.image.load('2 player obby!!!/images/Spacey backround.png')
player1_size = pygame.transform.rotate(pygame.transform.scale(player1,(SWIDTH,SHEIGHT)),90)
player2_size = pygame.transform.rotate(pygame.transform.scale(player2,(SWIDTH,SHEIGHT)),-90)
bgbg_size = pygame.transform.scale(bgbg,(WIDTH,HEIGHT))
font = pygame.font.SysFont('impact',50)
yellow_bullets = []
red_bullets = []

class Spaceship:
    def __init__(self,x,y,color,keys):
        self.rect = pygame.Rect(x,y,SWIDTH,SHEIGHT)
        self.color = color
        self.health = 10
        self.keys = keys
        self.y_bullets = []
        self.r_bullets = []
    def draw(self):
        if self.color == 'yellow':
            screen.blit(player1_size,(self.rect.x,self.rect.y))
        elif self.color == 'red':
            screen.blit(player2_size,(self.rect.x,self.rect.y))
    def move(self):
        keypressed = pygame.key.get_pressed()
        if self.color == 'yellow':
            if keypressed[self.keys['left']] and self.rect.x > 0:
                self.rect.x -= 5
            if keypressed[self.keys['right']] and self.rect.x < WIDTH/2 - SWIDTH:
                self.rect.x += 5
            if keypressed[self.keys['up']] and self.rect.y > 0:
                self.rect.y -= 5
            if keypressed[self.keys['down']] and self.rect.y < HEIGHT - SHEIGHT:
                self.rect.y += 5
        if self.color == 'red':
            if keypressed[self.keys['left']] and self.rect.x > WIDTH/2:
                self.rect.x -= 5
            if keypressed[self.keys['right']] and self.rect.x < WIDTH - SWIDTH:
                self.rect.x += 5
            if keypressed[self.keys['up']] and self.rect.y > 0:
                self.rect.y -= 5
            if keypressed[self.keys['down']] and self.rect.y < HEIGHT - SHEIGHT:
                self.rect.y += 5



                

class Bullet:
    def __init__(self,x,y,direction,size):
        self.size = size
        self.rect = pygame.Rect(x,y,size*3,size)
        self.direction = direction
    def draw(self):
        pygame.draw.rect(screen,'white',self.rect)
    def move(self):
        if self.direction == 'right':
            self.rect.x += 5
        if self.direction == 'left':
            self.rect.x -= 5 

        

class Game:
    def __init__(self):
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.yellow_bullets = yellow_bullets
        self.red_bullets = red_bullets
        self.yellowspaceshiporplayer2 = Spaceship(WIDTH/4,HEIGHT/2,'yellow',{'right':pygame.K_d,
                                                                            'left':pygame.K_a,
                                                                            'down':pygame.K_s,
                                                                            'up':pygame.K_w,
                                                                            'lctrl':pygame.K_LCTRL
                                                                            })
        self.redspaceshiporplayer1 = Spaceship(WIDTH - WIDTH/4,HEIGHT/2,'red',{'right':pygame.K_RIGHT,
                                                                            'left':pygame.K_LEFT,
                                                                            'down':pygame.K_DOWN,
                                                                            'up':pygame.K_UP,
                                                                            'rctrl':pygame.K_RCTRL
                                                                            })
    def draw_window(self):
        screen.blit(bgbg_size,(0,0))
        font = pygame.font.SysFont('impact',40)
        yellow_health_txt = font.render(f'HP:{self.yellowspaceshiporplayer2.health}',True,'gold')
        screen.blit(yellow_health_txt,(10,10))
        red_health_txt = font.render(f'HP:{self.redspaceshiporplayer1.health}',True,'gold')
        screen.blit(red_health_txt,(WIDTH-red_health_txt.get_width()-10,10))
        self.cooldown1 += 1
        self.cooldown2 += 1
        keypressed = pygame.key.get_pressed()
        self.yellowspaceshiporplayer2.draw()
        self.redspaceshiporplayer1.draw()
        pygame.draw.rect(screen,('black'),(WIDTH/2 - 5,0,10,HEIGHT))

        for bullet in self.yellow_bullets:
            if bullet.rect.x > WIDTH:
                self.yellow_bullets.remove(bullet)
            elif bullet.rect.x > self.redspaceshiporplayer1.rect.x and bullet.rect.x < self.redspaceshiporplayer1.rect.x + SWIDTH:
                if bullet.rect.y > self.redspaceshiporplayer1.rect.y and bullet.rect.y < self.redspaceshiporplayer1.rect.y + SWIDTH:
                    self.redspaceshiporplayer1.health -= 1
                    self.yellow_bullets.remove(bullet)
            bullet.draw()
            bullet.move()
        
        for bullet in self.red_bullets:
            if bullet.rect.x > WIDTH:
                self.red_bullets.remove(bullet)
            elif bullet.rect.x > self.yellowspaceshiporplayer2.rect.x and bullet.rect.x < self.yellowspaceshiporplayer2.rect.x + SWIDTH/2:
                if bullet.rect.y > self.yellowspaceshiporplayer2.rect.y and bullet.rect.y < self.yellowspaceshiporplayer2.rect.y + SHEIGHT:
                    self.yellowspaceshiporplayer2.health -= 1
                    self.red_bullets.remove(bullet)
            bullet.draw()
            bullet.move()

        if self.yellowspaceshiporplayer2.color == 'yellow' and keypressed[self.yellowspaceshiporplayer2.keys['lctrl']] and self.cooldown1 >= 30:
            y_bullet = Bullet(self.yellowspaceshiporplayer2.rect.x,self.yellowspaceshiporplayer2.rect.y + SHEIGHT/2 +3,'right',6)
            self.yellow_bullets.append(y_bullet)
            self.cooldown1 = 0

        if self.redspaceshiporplayer1.color == 'red' and keypressed[self.redspaceshiporplayer1.keys['rctrl']] and self.cooldown2 >= 30:
            r_bullet = Bullet(self.redspaceshiporplayer1.rect.x,self.redspaceshiporplayer1.rect.y + SHEIGHT/2 +3,'left',6)
            self.red_bullets.append(r_bullet)
            self.cooldown2 = 0

        if self.yellowspaceshiporplayer2.health < 1:
            screen.fill('red')
            font = pygame.font.SysFont('impact',100)
            red_win_txt = font.render('Red Wins!',True,'black')
            screen.blit(red_win_txt,(WIDTH/2 - red_win_txt.get_width()/2,HEIGHT/2 - red_win_txt.get_height()/2))
            self.redspaceshiporplayer1.health = 1000
        if self.redspaceshiporplayer1.health < 1:
            screen.fill('gold')
            font = pygame.font.SysFont('impact',100)
            red_win_txt = font.render('Yellow Wins!',True,'black')
            screen.blit(red_win_txt,(WIDTH/2 - red_win_txt.get_width()/2,HEIGHT/2 - red_win_txt.get_height()/2))
            self.yellowspaceshiporplayer2.health = 1000
            

    def main(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.yellowspaceshiporplayer2.move()
            self.redspaceshiporplayer1.move()
            self.draw_window()
            pygame.display.update()
        pygame.quit()
if __name__ == '__main__':
    game = Game()
    game.main()
