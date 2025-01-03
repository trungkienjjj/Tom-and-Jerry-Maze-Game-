import pygame
from global_variable import *
from class_file import *
from screen_in_game import *
import sound

flag_sound_game = True
pygame.init()
step = 0
d_font = pygame.font.Font("SVN-Coder's Crux.otf", 50)
#d_font = pygame.font.Font("OCRAEXT.TTF", 25)

# LOAD BUTTON IMAGE
# nút suggest đường đi
suggest_img = pygame.image.load("suggest.png")
suggest_img = pygame.transform.scale(suggest_img, (150, 70))
# nút back
#back_img = pygame.image.load(r"In game/back.png")
#back_img = pygame.transform.scale(back_img, (300, 280))
# nút đổi thuật toán
change_algo_img = pygame.image.load("In game/change-algo.png")
change_algo_img = pygame.transform.scale(change_algo_img, (150, 70))
# nút pause
pause_img = pygame.image.load("In game/pause.png")
pause_img = pygame.transform.scale(pause_img, (50, 50))
# nút timer
timer_img = pygame.image.load(r"In game/timer.png")
timer_img = pygame.transform.scale(timer_img, (50, 50))
# nút moving
top_img = pygame.image.load("top.png")
top_img = pygame.transform.scale(top_img, (100, 100))
down_img = pygame.image.load("down.png")
down_img = pygame.transform.scale(down_img, (90, 90))
left_img = pygame.image.load("left.png")
left_img = pygame.transform.scale(left_img, (100, 100))
right_img = pygame.image.load("right.png")
right_img = pygame.transform.scale(right_img, (100, 100))
# nút play bot
playbot_img = pygame.image.load("play_bot.png")
playbot_img = pygame.transform.scale(playbot_img, (150, 70))
# nút trở về setting
back_setting_img = pygame.image.load(r"setting.jpg")
back_setting_img = pygame.transform.scale(back_setting_img, (100, 100))

# Loa âm thanh
sound_on_button_game = pygame.image.load('sound_on.png')
sound_on_button_game = pygame.transform.scale(sound_on_button_game, (WIDTH // 40, HEIGHT // 20))
sound_on_button_coord_game = (WIDTH // 500, 17 * HEIGHT // 18)
sound_on_button_rect_game = sound_on_button_game.get_rect(topleft=sound_on_button_coord_game)
sound_off_button_game = pygame.image.load('sound_off.png')
sound_off_button_game = pygame.transform.scale(sound_off_button_game, (WIDTH // 40, HEIGHT // 20))
sound_off_button_coord_game = (WIDTH // 500, 17 * HEIGHT // 18)
sound_off_button_rect_game = sound_off_button_game.get_rect(topleft=sound_off_button_coord_game)

# TỌA ĐỘ THÔNG SỐ
# tọa độ nút setting
setting_coord = (WIDTH // 15 - 10, 8 * HEIGHT // 9)
# tọa độ mode game
mode_coord1 = (WIDTH - 530, HEIGHT - 250)  # chữ
mode_coord2 = (mode_coord1[0] + 100, mode_coord1[1])  # thông số
# tọa độ thời gian
time_coord1 = (mode_coord1[0], mode_coord1[1] + 40)  # nút timer
time_coord2 = (time_coord1[0] + 80, time_coord1[1] + 20)  # thông số
# tọa độ số bước đi hiện tại
step_coord1 = (mode_coord1[0], mode_coord1[1] + 120)
step_coord2 = (step_coord1[0] + 120, step_coord1[1])
# tọa độ level
level_coord1 = (step_coord1[0], HEIGHT - 50)  # chữ
level_coord2 = (level_coord1[0] + 120, level_coord1[1])  # thông số
# tọa độ nút suggest
suggest_coord = (WIDTH // 2 + 400, mode_coord1[1] - 200)
# tọa độ thuật toán hiện tại
algo_coord1 = (suggest_coord[0], HEIGHT // 2 + 45)  # chữ
algo_coord2 = (algo_coord1[0] + 200, algo_coord1[1])  # thông số
# tọa độ nút đổi thuật toán
change_suggest_coord = (WIDTH - 300, algo_coord1[1] + 30)
# tọa độ nút pause
pause_coord = (WIDTH - 60, HEIGHT - 60)
# toạ độ nút moving
top_coord = (9 * WIDTH // 10, mode_coord1[1] - 10)
down_coord = (top_coord[0], top_coord[1] + 100)
left_coord = (down_coord[0] - 100, down_coord[1])
right_coord = (down_coord[0] + 100, down_coord[1])

# tọa độ nút play bot
playbot_coord = (mode_coord1[0], change_suggest_coord[1] + 30)
change_suggest_rect = change_algo_img.get_rect(topleft=change_suggest_coord)
pause_rect = pause_img.get_rect(topleft=pause_coord)
down_rect = down_img.get_rect(topleft=down_coord)
top_rect = top_img.get_rect(topleft=top_coord)
left_rect = left_img.get_rect(topleft=left_coord)
right_rect = right_img.get_rect(topleft=right_coord)
back_setting_rect = back_setting_img.get_rect(topleft=setting_coord)

def draw_border(image, coord, border_color=(0, 0, 0), border_thickness=5):
    rect = image.get_rect(topleft=coord)
    pygame.draw.rect(screen, border_color, rect, border_thickness)
    screen.blit(image, coord)
def draw_text_with_background(text, font, color, bg_color, coord):
    # Render the text
    text_surface = font.render(text, True, color)
    # Get the size of the text surface
    text_rect = text_surface.get_rect(topleft=coord)
    # Draw the background rectangle
    pygame.draw.rect(screen, bg_color, text_rect)
    # Blit the text onto the screen
    screen.blit(text_surface, coord)
def draw_dashboard(steps, level, mode_game, algo):
    global hours, minutes, seconds
    global elapsed_time
    global sound_enabled
    d_color = "yellow"
    rect_color = (46, 60, 86)
    time_color = "red"
    if level == '100x100':
        d_color = "black"
        rect_color = "orange"
        time_color = "black"
    elapsed_time = game_clock.get_elapsed_time()
    # Chuyển đổi thời gian sang định dạng hh:mm:ss
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    # VẼ CHỮ
    # vẽ thời gian
    screen.blit(timer_img, time_coord1)
    time_text = f"{hours:02}:{minutes:02}:{seconds:02}"
    draw_text_with_background(time_text, d_font, time_color, rect_color, time_coord2)
    # vẽ step
    draw_text_with_background('Steps:', d_font, pygame.Color(d_color), rect_color, step_coord1)
    draw_text_with_background(f'{steps}', d_font, pygame.Color(d_color), rect_color, step_coord2)
    # vẽ mode game
    draw_text_with_background('Mode:', d_font, pygame.Color(d_color), rect_color, mode_coord1)
    draw_text_with_background(f'{mode_game}', d_font, pygame.Color(d_color), rect_color, mode_coord2)
    # vẽ level
    draw_text_with_background('Level: ', d_font, pygame.Color(d_color), rect_color, level_coord1)
    draw_text_with_background(f'{level}', d_font, pygame.Color(d_color), rect_color, level_coord2)
    # vẽ thuật toán hiện tại
    draw_text_with_background('Algorithm:', d_font, pygame.Color(d_color), rect_color, algo_coord1)
    draw_text_with_background(f'{algo}', d_font, pygame.Color(d_color), rect_color, algo_coord2)

    pos = pygame.mouse.get_pos()

    # VẼ NÚT
    # nút pause
    if is_mouse_over_button(pos, pause_rect):
        draw_border(pause_img, pause_coord)
    else:
        screen.blit(pause_img, pause_coord)

    # nút moving
    if is_mouse_over_button(pos, top_rect):
        draw_border(top_img, top_coord)
    else:
        screen.blit(top_img, top_coord)

    if is_mouse_over_button(pos, down_rect):
        draw_border(down_img, down_coord)
    else:
        screen.blit(down_img, down_coord)

    if is_mouse_over_button(pos, left_rect):
        draw_border(left_img, left_coord)
    else:
        screen.blit(left_img, left_coord)

    if is_mouse_over_button(pos, right_rect):
        draw_border(right_img, right_coord)
    else:
        screen.blit(right_img, right_coord)

    # nút đổi thuật toán
    if is_mouse_over_button(pos, change_suggest_rect):
        draw_border(change_algo_img, change_suggest_coord)
    else:
        screen.blit(change_algo_img, change_suggest_coord)

    # nút quay về settings
    if is_mouse_over_button(pos, back_setting_rect):
        draw_border(back_setting_img, setting_coord)
    else:
        screen.blit(back_setting_img, setting_coord)

    # Nút loa
    if sound.sound_enabled:
        if is_mouse_over_button(pos, sound_on_button_rect_game):
            draw_border(sound_on_button_game, sound_on_button_coord_game)
        else:
            screen.blit(sound_on_button_game, sound_on_button_coord_game)
    else:
        if is_mouse_over_button(pos, sound_off_button_rect_game):
            draw_border(sound_off_button_game, sound_off_button_coord_game)
        else:
            screen.blit(sound_off_button_game, sound_off_button_coord_game)

    if mode_game == "Player":
        # vẽ nút gợi ý đường đi trong mode player, mode autoplay không có lựa chọn này
        if is_mouse_over_button(pos, suggest_img.get_rect(topleft=suggest_coord)):
            draw_border(suggest_img, suggest_coord)
        else:
            screen.blit(suggest_img, suggest_coord)

    if mode_game == "Bot" or mode_game == "Both":
        # vẽ nút play bot
        if is_mouse_over_button(pos, playbot_img.get_rect(topleft=playbot_coord)):
            draw_border(playbot_img, playbot_coord)
        else:
            screen.blit(playbot_img, playbot_coord)

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

def is_mouse_over_button(pos, button_rect):
    return button_rect.collidepoint(pos)

def handle_play_bot_button_click(pos):
    playbot_rect = playbot_img.get_rect(topleft=playbot_coord)
    if is_mouse_over_button(pos, playbot_rect):
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_w}))

def handle_suggest_button_click(pos):
    suggest_rect = suggest_img.get_rect(topleft=suggest_coord)
    if is_mouse_over_button(pos, suggest_rect):
        send_key_space()

#def handle_back_button_click(pos):
#    if is_mouse_over_button(pos, back_rect):
#        send_key_escape()

def handle_setting_back(pos):
    if is_mouse_over_button(pos, back_setting_rect):
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_e}))

def handle_change_algorithm_button_click(pos):
    if is_mouse_over_button(pos, change_suggest_rect):
        send_key_q()

def handle_sound_button(pos):
    if is_mouse_over_button(pos, sound_off_button_rect_game):
        sound.inMenu = False
        sound.toggle_sound()

def handle_move(pos):
    if is_mouse_over_button(pos, left_rect):
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_LEFT}))
    elif is_mouse_over_button(pos, right_rect):
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RIGHT}))
    elif is_mouse_over_button(pos, top_rect):
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_UP}))
    elif is_mouse_over_button(pos, down_rect):
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_DOWN}))

def handle_pause_button_click(pos):
    global paused
    if is_mouse_over_button(pos, pause_rect):
        send_key_escape()

def send_key_q():
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_q}))

def send_key_space():
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_SPACE}))

def send_key_escape():
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_ESCAPE}))

def send_key_right():
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RIGHT}))
