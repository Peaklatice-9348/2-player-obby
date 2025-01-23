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
player1 = pygame.image.load('2 player obby!!!/images/Player1.png')
player2 = pygame.image.load('2 player obby!!!/images/Player2.png')
bgbg = pygame.image.load('2 player obby!!!/images/Spacey backround.png')
player1_size = pygame.transform.rotate(pygame.transform.scale(player1,(SWIDTH,SHEIGHT)),90)
player2_size = pygame.transform.rotate(pygame.transform.scale(player2,(SWIDTH,SHEIGHT)),-90)
bgbg_size = pygame.transform.scale(bgbg,(WIDTH,HEIGHT))
font = pygame.font.SysFont('impact',50)



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
    def shoot(self):
        if self.color == 'yellow':
            y_bullet = Bullet(self.rect.x,self.rect.y,'right')
            self.y_bullets.append(y_bullet)
        else:
            r_bullet = Bullet(self.rect.x,self.rect.y,'left')
            self.r_bullets.append(r_bullet)



                

class Bullet:
    def __init__(self,x,y,direction):
        self.rect = pygame.Rect(x,y,20,10)
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
        self.yellow_bullets = self.yellow_bullets
        self.red_bullets = self.red_bullets
        self.yellowspaceshiporplayer2 = Spaceship(WIDTH/4,HEIGHT/2,'yellow',{'right':pygame.K_d,
                                                                            'left':pygame.K_a,
                                                                            'down':pygame.K_s,
                                                                            'up':pygame.K_w
                                                                            })
        self.redspaceshiporplayer1 = Spaceship(WIDTH - WIDTH/4,HEIGHT/2,'red',{'right':pygame.K_RIGHT,
                                                                            'left':pygame.K_LEFT,
                                                                            'down':pygame.K_DOWN,
                                                                            'up':pygame.K_UP
                                                                            })
    def draw_window(self):
        screen.blit(bgbg_size,(0,0))
        self.yellowspaceshiporplayer2.draw()
        self.redspaceshiporplayer1.draw()
        pygame.draw.rect(screen,('black'),(WIDTH/2 - 5,0,10,HEIGHT))
        
        for bullet in self.yellow_bullets:
            bullet.draw()
            bullet.move()
        for bullet in self.red_bullets:
            bullet.draw()
            bullet.move()
    def main(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    
            self.yellowspaceshiporplayer2.move()
            self.redspaceshiporplayer1.move()
            self.draw_window()
            pygame.display.update()
        pygame.quit()
if __name__ == '__main__':
    game = Game()
    game.main()
