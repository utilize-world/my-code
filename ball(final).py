import pygame
from pygame.locals import *
# from sys import exit

pygame.init()
screen_size = (400, 400)   # #屏幕为400 X 400大小
screen = pygame.display.set_mode(screen_size, 1, 32)
screen_rect = screen.get_rect()
rbg = (255, 255, 255)   # #设定RGB数值为白色
text_color = (0, 0, 0)
clock = pygame.time.Clock()
# pygame.mouse.set_visible(0)
mouse_posX = pygame.mouse.get_pos()[0]
mouse_posY = pygame.mouse.get_pos()[1]  # #获得鼠标的位置
# pygame.mouse.set_pos(mouse_posX, mouse_posY)
ball_sprites = pygame.sprite.Group()
block_sprites = pygame.sprite.RenderUpdates()
board = pygame.sprite.Sprite()      # #创建Sprite类的一个实例
board_image = pygame.image.load('board.jpg')
board.rect = board_image.get_rect()
board.rect.x = 200
board.rect.y = screen_size[1] - board.rect.height


class Block(pygame.sprite.Sprite):
    # 定义块的类
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('block.jpg').convert_alpha()
        self.rect = self.image.get_rect()


class Ball(pygame.sprite.Sprite):
    # 定义一个滚球的类
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.image = pygame.image.load('ball.jpg').convert_alpha()
        self.rect = Rect(200, 200, 20, 18)    # #初始化其位置

    def move(self):
        passed_time = clock.tick(60)  # #控制帧率最大为60FPS
        self.rect.x += int(self.speed[0] * passed_time / 1000)   # #除以1000是将毫秒转化为秒，这里速度的单位是秒每像素
        self.rect.y += int(self.speed[1] * passed_time / 1000)

    def update(self):
        #  以下是用来控制小球碰到边界时的情况，速度反向
        if self.rect.x > screen_size[0] - self.rect.width:
            self.rect.x = screen_size[0] - self.rect.width
            self.speed[0] *= -1
        if self.rect.y > screen_size[1] - self.rect.height:
            self.rect.y = screen_size[1] - self.rect.height
            # self.y_speed = -self.y_speed
            ball_sprites.remove(self)
        if self.rect.x < 0:
            self.rect.x = 0
            self.speed[0] *= -1
        if self.rect.y < 0:
            self.rect.y = 0
            self.speed[1] *= -1


score_count = 0     # #记录分数
ball = Ball(speed=[160, 180])
# 创建一个Ball类的实例，并初始化其位置和速度
ball_sprites.add(ball, board)
judge = False
block = Block()


def print_block_map():
    for i in range(0, screen_size[0], block.rect.width):
        for j in range(0, int(screen_size[1]*1/3), block.rect.height):
            new_block = Block()
            block_sprites.add(new_block)
            new_block.rect[0] = i
            new_block.rect[1] = j
            screen.blit(new_block.image, (i, j))
            pygame.display.update()


def print_text():
    global score_count  # #打印结束文字用
    text1 = 'YOU LOST'
    text2 = f'your final score is {score_count}'
    font1 = pygame.font.SysFont('arial', 40, True)
    font2 = pygame.font.SysFont('arial', 30, False, True)
    text1_surface = font1.render(text1, 1, text_color)
    text2_surface = font2.render(text2, 1, text_color)
    screen.blit(text1_surface, (50, 50))
    screen.blit(text2_surface, (100, 120))
    pygame.display.update()


def crash_detect():
    global score_count
    if pygame.sprite.collide_rect(ball, board):     # #判断两个矩形是否相撞
        '''if score_count % 5 == 0:
            ball.speed[0] *= 1.12
            ball.speed[1] *= 1.12
        '''      # #随着分数增加，速度会越来越快，一般三十分已经接不住了
        ball.speed[1] *= -1
    if pygame.sprite.spritecollide(ball, block_sprites, True):
        score_count += 1
        if score_count % 8 == 0:
            ball.speed[0] *= 1.2
            ball.speed[1] *= 1.2
        ball.speed[1] *= -1


def clear_screen():
    screen.fill((255, 255, 255))


print_block_map()   # #打印地图
while judge is False:
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            board.rect.centerx = event.pos[0]   # #控制板的中心一直在鼠标的位置
        if event.type == QUIT:
            judge = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                judge = True

    crash_detect()
    if score_count == 60:   # #胜利文字
        clear_screen()
        v_text = 'Great! YOU WIN!!'
        font3 = pygame.font.SysFont('arial', 40, True)
        v_text_surface = font3.render(v_text, 1, text_color)
        screen.blit(v_text_surface, (20, 20))
        pygame.display.update()
        pygame.time.delay(1000)
        judge = True
    if ball not in ball_sprites:
        clear_screen()
        print_text()
        pygame.time.delay(2000)     # #延迟2秒，至少看清最后的文字
        judge = True
    score_font = pygame.font.SysFont('arial', 24)
    score_text = f'score: {score_count}'
    score_surface = score_font.render(score_text, 1, text_color)
    ball.move()
    screen.fill(rbg)    # #填涂屏幕
    screen.blit(score_surface, (200, 200))
    block_sprites.update()  # #容器内所有sprite调用自身的update方法
    for blocks in block_sprites:
        screen.blit(blocks.image,(blocks.rect[0], blocks.rect[1]))
        ball_sprites.update()
        # 画block
    screen.blit(board_image, (board.rect.x, board.rect.y))  # #画板子
    screen.blit(ball.image, (ball.rect.x, ball.rect.y))     # #画出小球
    #  这里一定要注意，屏幕要在小球前面填涂，否则会直接覆盖后面物体的图像，在这里卡了半个小时
    pygame.display.update()     # #更新屏幕显示
