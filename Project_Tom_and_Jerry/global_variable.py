import pygame
from timer import *
from class_file  import*
sound_on = True
FPS = 60 
clock = pygame.time.Clock()

pygame.font.init()
#Hàm lấy thông số màn hình
def get_screen_size():
    # Khởi tạo pygame
    pygame.init()
    # Lấy kích thước màn hình
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h

    # Kết thúc pygame
    pygame.quit()

    return screen_width, screen_height
time = 60
score = 0
RES = WIDTH, HEIGHT = get_screen_size()
DELTA_X = WIDTH//8   # dời ngang mê cung 
DELTA_Y = HEIGHT//5  # dời dọc mê cung xuống 

Bottom_right_x, Bottom_right_y = 19*HEIGHT//24, 19*HEIGHT//24 # kích cỡ mê cung
Mode_Findpath = 0
Mode_game_bot = 1
paused = False
COLS = 20
ROWS = 20
ChosingStartendMode = 1
Game_mode = "Player"
DarkGray = (128, 128, 128)
White = (255, 255, 255)
Black = (0, 0, 0)
FPS = 60
#LOADGAME 
WIDTH_mini_maze = WIDTH //2 
HEIGHT_mini_maze= HEIGHT //2 
NUM_MAZES = 3
MARGIN = 30 # Khoảng cách giữa các maze
MAZE_SIZE = min((WIDTH_mini_maze - (NUM_MAZES + 1) * MARGIN) // NUM_MAZES, HEIGHT_mini_maze - 2 * MARGIN)
# create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
CELLSIZE = 96  # cell width/height in pixels in tilesheet
SCALE_FACTOR = 0.45
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT ))
pygame.init()
pygame.display.init()
# background
background = pygame.image.load('ingame.png')
# Score :
score_value = 0
#font = pygame.font.Font('freesansbold.ttf', 32)
font = pygame.font.Font('8-BIT WONDER.ttf', 23)
font2 = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
# Game Winner Text :
win_font = pygame.font.Font('freesansbold.ttf', 60)
# Game Over text
over_font = pygame.font.Font('freesansbold.ttf', 60)
diesound_times = 0
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h
surface = pygame.Surface([WIDTH, HEIGHT], pygame.SRCALPHA)
ImMenu = pygame.image.load('Menu\menu.png')
ImMenu = pygame.transform.scale(ImMenu, (screen_width, screen_height))
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)
Cyan = (0, 255, 255)
Magenta = (255, 0, 255)
Orange = (255, 165, 0)
Purple = (128, 0, 128)
Pink = (255, 192, 203)
Brown = (165, 42, 42)
Teal = (0, 128, 128)
Navy = (0, 0, 128)
Olive = (128, 128, 0)
Lime = (0, 255, 0)
Maroon = (128, 0, 0)
Silver = (192, 192, 192)
Gold = (255, 215, 0)
menu_options = ["Random", "Manual"]
selected_option_choose_again = 0
option_font = pygame.font.Font('8-BIT WONDER.ttf', 29)
Mode_Findpath = 0
Mode_game_bot = 1
paused = False
ChosingStartendMode = 1
Game_mode = "Player"
DarkGray = (128, 128, 128)
White = (255, 255, 255)
Black = (0, 0, 0)
FPS = 60
current_direction = "None"

screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h
optionsettings = ["20x20","Player","DFS","Manual","OnSound","Back"]
rendered_text_settings = option_font.render("20x20", True, White)

game_clock = Clock()
Back_outgame =pygame.image.load('back2.png')
Back_outgame = pygame.transform.scale(Back_outgame, (rendered_text_settings.get_width(), rendered_text_settings.get_height()))
