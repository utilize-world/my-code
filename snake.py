import pygame
from pygame.locals import *
import random
from sys import exit

running = True
fruit_judge = True
score_count = 0
pygame.init()
screen_size = 600, 600
screen = pygame.display.set_mode(screen_size, 0, 32)
pygame.display.set_caption('happy snake')
bg_color = (0, 0, 0)
fruit_color = (255, 205, 25)
text_color = (255, 255, 255)
direction = 'right'
snake_body = [[210, 210], [240, 210]]


class Snake(pygame.sprite.Sprite):
    block_width = 30
    block_height = 30

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == 'left':
            self.x -= 30
        if direction == 'right':
            self.x += 30
        if direction == 'up':
            self.y -= 30
        if direction == 'down':
            self.y += 30

    def judge(self):
        global running
        if [self.x, self.y] in snake_body[1:]:
            running = False


class Fruit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        global fruit_judge
        if fruit_judge:
            self.x = random.randrange(0, 600, 30)
            self.y = random.randrange(0, 600, 30)
            fruit_judge = False
        pygame.draw.rect(screen, fruit_color, (self.x, self.y, Snake.block_width, Snake.block_height))
        pygame.display.update()

    def judge(self, snake):
        global score_count, fruit_judge
        if snake.x == self.x and snake.y == self.y:
            score_count += 1
            screen.fill(bg_color)
            pygame.display.update()
            fruit_judge = True
            return True
        else:
            snake_body.pop()


def crack_detect(snake_head):
    global running
    if snake_head.x-15 > screen_size[0] or snake_head.y-15 > screen_size[1]:
        running = False
    if snake_head.x+15 < 0 or snake_head.y+15 < 0:
        running = False


def clear_bg():
    screen.fill(bg_color)


def draw(colors, rect):
    pygame.draw.rect(screen, colors, rect)


def print_text():
    text_score = f'score:{score_count}'
    font = pygame.font.SysFont('arial', 40)
    text_score_surface = font.render(text_score, 1, text_color)
    screen.blit(text_score_surface, (0, 0))
    pygame.display.update()


def run():
    global running
    global direction
    tick_time = 8
    snake_head = Snake(210, 210)
    fruit = Fruit(0, 0)
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP and direction != 'down':
                    direction = 'up'
                elif event.key == K_DOWN and direction != 'up':
                    direction = 'down'
                elif event.key == K_LEFT and direction != 'right':
                    direction = 'left'
                elif event.key == K_RIGHT and direction != 'left':
                    direction = 'right'
        screen.fill(bg_color)
        print_text()
        for i in snake_body:
            draw(text_color, (i[0], i[1], 30, 30))
        fruit.draw()
        clock.tick(tick_time)
        snake_head.judge()
        snake_body.insert(0, [snake_head.x, snake_head.y])
        fruit.judge(snake_head)
        snake_head.move(direction)
        crack_detect(snake_head)

        if not running:
            clear_bg()
            text_f = f'your final score is {score_count}'
            font1 = pygame.font.SysFont('arial', 40, True)
            text_f_surface = font1.render(text_f, 1, text_color)
            screen.blit(text_f_surface, (150, 200))
            pygame.display.flip()
            pygame.time.delay(1000)
        pygame.display.update()


if __name__ == '__main__':
    run()
