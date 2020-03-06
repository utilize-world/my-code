import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen_size = (400, 400)   # #屏幕为400 X 400大小
screen = pygame.display.set_mode(screen_size, 0, 32)
screen_rect = screen.get_rect()
rbg = (255, 255, 255)   # #设定RGB数值为白色
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
# 隐藏鼠标


class Ball(pygame.sprite.Sprite):
    # 定义一个滚球的类
    def __init__(self, pos, speed):
        pygame.sprite.Sprite.__init__(self)
        self.x_speed = speed[0]
        self.y_speed = speed[1]
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.image = pygame.image.load('ball.jpg').convert_alpha()      # #加载图片
        self.rect = self.image.get_rect()

    def move(self):
        passed_time = clock.tick(60)  # #控制帧率最大为60FPS
        self.x_pos += self.x_speed*passed_time / 1000   # #除以1000是将毫秒转化为秒，这里速度的单位是秒每像素
        self.y_pos += self.y_speed*passed_time / 1000

    def update(self):
        #  以下是用来控制小球碰到边界时的情况，速度反向
        if self.x_pos > screen_size[0] - self.rect.width:
            self.x_pos = screen_size[0] - self.rect.width
            self.x_speed = -self.x_speed
        if self.y_pos > screen_size[1] - self.rect.height:
            self.y_pos = screen_size[1] - self.rect.height
            self.y_speed = -self.y_speed
        if self.x_pos < 0:
            self.x_pos = 0
            self.x_speed = -self.x_speed
        if self.y_pos < 0:
            self.y_pos = 0
            self.y_speed = -self.y_speed


ball = Ball(pos=[0, 0], speed=[50, 50])
# 创建一个Ball类的实例，并初始化其位置和速度

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
            elif event.key == K_DOWN and ball.y_speed < 200:
                ball.y_speed += 30
            elif event.key == K_UP:
                ball.y_speed -= 30
            elif event.key == K_RIGHT and ball.x_speed < 200:
                ball.x_speed += 30
            elif event.key == K_LEFT:
                ball.x_speed -= 30
    ball.move()
    ball.update()
    screen.fill(rbg)    # #填涂屏幕
    screen.blit(ball.image, (int(ball.x_pos), int(ball.y_pos)))     # #画出小球
    #  这里一定要注意，屏幕要在小球前面填涂，否则会直接覆盖后面物理的图像，在这里卡了半个小时
    pygame.display.update()     # #更新屏幕显示
