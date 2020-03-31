'''
参考资料
https://blog.csdn.net/qq_41597912/article/details/80030626?depth_1-utm_source=distribute.wap_relevant.none-task&utm_source=distribute.wap_relevant.none-task&tdsourcetag=s_pctim_aiomsg
https://eyehere.net/2011/python-pygame-novice-professional-2/?tdsourcetag=s_pctim_aiomsg
'''
#  https://blog.csdn.net/rwangnqian/article/details/80021808 关于类的说明
import pygame, sys
from pygame.locals import *
from random import randrange


pygame.init()
screen_size = 480, 600
pygame.display.set_mode(screen_size)
#  全屏为.set_mode(screen_size,FULLSCREEN)
pygame.mouse.set_visible(0)
plane_image = pygame.image.load('plane2.jpg')
background = pygame.image.load('background.jpg')
myplane_image = pygame.image.load('myplane.png')
bullets_image = pygame.image.load('bullets.jpg')


class plane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = plane_image
        self.rect = self.image.get_rect()
        self.rect.top = -self.rect.height
        self.rect.centerx = int(randrange(screen_size[0]-self.rect.width)+self.rect.width/2)

    def update(self):
        self.rect.top += 1
        if self.rect.top>screen_size[1]:
            self.kill()


class bullets(pygame.sprite.Sprite):
    def __init__(self, axis):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullets_image
        self.rect = self.image.get_rect()
        self.rect.centerx = axis[0]
        self.rect.centery = axis[1]

    def update(self):
        self.rect.top -= 3
        if self.rect.bottom <= 0:
            self.kill()


class myplane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = myplane_image
        self.rect = self.image.get_rect()
        self.rect.bottom = screen_size[1]
        self.rect.centerx = int(screen_size[0]/2)

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -3)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 3)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)
    #  限制飞机在屏幕中
        if self.rect.bottom > screen_size[1]:
            self.rect.bottom = screen_size[1]
        elif self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right > screen_size[1]:
            self.rect.right = screen_size[1]

    def fire(self):
        axis = [self.rect.centerx, self.rect.top]
        new_bullet = bullets(axis)
        mybullets.add(new_bullet)
        all_sprites.add(new_bullet)


sprites = pygame.sprite.RenderUpdates()
#  创建Sprite的容器（什么意思没弄清楚）
sprites.add(plane())  # # 向容器中添加一个plane对象
mysprites = pygame.sprite.RenderUpdates()
myplane = myplane()
mysprites.add(myplane)
mybullets = pygame.sprite.RenderUpdates()
all_sprites = pygame.sprite.RenderUpdates()
all_sprites.add(mysprites)
all_sprites.add(sprites)
all_sprites.add(mybullets)

screen = pygame.display.get_surface()
bg = background
#  RGB格式
screen.blit(background, (0, 0))
#  填充背景颜色
pygame.display.flip()
#  显示更新后的屏幕
clock = pygame.time.Clock()
speed = 100  # #最大帧率
ADDENEMY = pygame.USEREVENT+1
pygame.time.set_timer(ADDENEMY, 1600)
score = 0


def clear_callback(surf, rect):  # # 清除旧的Sprite图形
    surf.blit(background, rect)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            myplane.fire()
        if event.type == ADDENEMY:
            newplane = plane()
            sprites.add(newplane)
            all_sprites.add(sprites)

    pressed_keys = pygame.key.get_pressed()
    sprites.clear(screen, clear_callback)
    clock.tick(speed)
    all_sprites.clear(screen, clear_callback)
    mybullets.update()
    mysprites.update(pressed_keys)
    sprites.update()
    updates = all_sprites.draw(screen)
    #  父类RenderUpdates的draw方法
    #  返回需要更新的部分
    pygame.display.update(updates)
    #  更新显示
    for j in mybullets.sprites():
        for i in sprites.sprites():
            if j.rect.colliderect(i.rect):
                i.kill()
                j.kill()

                score += 1
                font = pygame.font.Font(None, 25)
                black = 0, 0, 0
                textScore = f'Score: {score}'
                textS = font.render(textScore, True, black)
                dirs = textS.get_rect()
                screen.blit(background, (0, 0))
                screen.blit(textS, dirs)
                pygame.display.update()
                break
    if pygame.sprite.spritecollideany(myplane, sprites):
        myplane.kill()
        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 48)
        text = 'YOU   LOST!'
        height = font.get_linesize()
        antialias = 1
        black = 0, 0, 0
        text2 = font.render(text, antialias, black)
        r = text2.get_rect()
        center, top = screen.get_rect().center
        r.midtop = center, top
        screen.blit(text2, r)
        pygame.display.flip()
        break

