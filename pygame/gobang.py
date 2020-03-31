import pygame
from pygame.locals import *
from sys import exit
import numpy as np

pygame.init()
screen_size = 600, 600
pygame.display.set_caption('五子棋')
screen = pygame.display.set_mode(screen_size, 0, 32)
bg_color = 200, 200, 200    # 背景颜色
black_chess = (0, 0, 0)
white_chess = (255, 255, 255)
point_map = np.zeros([40, 40], int)     # 用二维数组来网格化
grid_width = 20             # 网格宽度和高度
grid_height = 20
black = 1               # 用于判断当前下的子是什么颜色，默认黑棋先
white = 0
screen.fill(bg_color)   # 画背景
running = True
clock = pygame.time.Clock()  # 这里面感觉没啥用


def draw_map():     # #用来画网格，很丑
    for i in range(30):
        pygame.draw.line(screen, black_chess, (i*20, 0), (i*20, 600))
        pygame.draw.line(screen, black_chess, (0, i*20), (600, i*20))
    pygame.display.update()


def judge(node_pos_x, node_pox_y, chess_color, x_dir, y_dir):   # 用于单向判断是否五子
    counter = 0     # 计数器，用来保存判断相同颜色子的个数
    text = ' '
    current_dir_x = x_dir       # 保留当前方向，在正向判断之后再传给本身进行反向判断
    current_dir_y = y_dir
    global running
    while point_map[node_pos_x+x_dir, node_pox_y+y_dir] == chess_color:     # #开始正向判断
        counter += 1
        if x_dir > 0:       # 按方向逐渐延伸
            x_dir += 1
        if y_dir > 0:
            y_dir += 1
        if y_dir < 0:
            y_dir -= 1
    x_dir = current_dir_x   # 为反向判断做准备
    y_dir = current_dir_y
    while point_map[node_pos_x-x_dir, node_pox_y-y_dir] == chess_color:     # #反向判断
        counter += 1
        if x_dir > 0:
            x_dir += 1
        if y_dir > 0:
            y_dir += 1
        if y_dir < 0:
            y_dir -= 1
    if counter >= 4:        # 假如计数器已经大于等于4，（因为进行判断时刻当前位置不计，所以为4）， 就结束主循环
        running = False
        if chess_color == 1:    # 判断当前子的颜色
            text = 'black'
        elif chess_color == -1:
            text = 'white'
        final_text = 'the winner is ' + text    # 打印出结果
        font = pygame.font.SysFont('arial', 32)
        text_surface = font.render(final_text, 1, (0, 0, 0))
        screen.blit(text_surface, (300, 500))
        pygame.display.flip()
        pygame.time.delay(2000)


def all_judge(node_pos_x, node_pox_y, chess_color):     # #对四个方向进行判断
    judge(node_pos_x, node_pox_y, chess_color, 1, 0)    # x
    judge(node_pos_x, node_pox_y, chess_color, 1, 1)    # y=x
    judge(node_pos_x, node_pox_y, chess_color, 0, 1)    # y
    judge(node_pos_x, node_pox_y, chess_color, 1, -1)   # y=-x


def chess_place(x, y):  # 放置棋子
    global black, white
    if point_map[round(x/20), round(y/20)] == 0:    # 当前位置没有棋子， 就放下
        if black == 1:                              # 判断是黑棋还是白棋
            pygame.draw.circle(screen, black_chess, [round(x/20)*20, round(y/20)*20], 8)
            point_map[round(x/20), round(y/20)] += 1   # 黑棋加一
            all_judge(round(x/20), round(y/20), 1)
            black = 0
            white = 1       # 每下一棋就更换顺序，颜色进行交替
            pygame.display.update()
            return
        elif white == 1:
            pygame.draw.circle(screen, white_chess, [round(x/20)*20, round(y/20)*20], 8)
            point_map[round(x/20), round(y/20)] += -1   # 白棋减一
            all_judge(round(x/20), round(y/20), -1)
            black = 1
            white = 0
            pygame.display.update()
            return


draw_map()


def run():
    while running:

        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                chess_place(*pygame.mouse.get_pos())
    clock.tick(20)
    exit()


if __name__ == '__main__':
    run()