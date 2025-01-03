import pygame
from global_variable import *
import sound
from save_load_game import*  
from class_file import * 
import json
from dashboard import *
def load_filegame():
    file_names =  []
    with open('database.json','r') as f :
        data = json.load(f)
        for account in data : 
            if login_forms.User_name in account : 
                if len(account) > 1 :
                    for key in account :
                        if (key!=login_forms.User_name):
                            tmp = key.split("_")
                            file_names.append(tmp[0])
                            print(tmp[0])
    return file_names 

# Hàm vẽ mỗi maze mini
def draw_mini_maze(screen, grid_cells, cols, rows, playerx, playery, start, end, x, y, size,color, flag = True):
    cell_size = size / max(cols, rows)
    if flag:
        Silver = (192, 192, 192)
        hover_rect = pygame.Rect(0, 0, size , size)
        pygame.draw.rect(screen, Silver,hover_rect)
    for cell in grid_cells:
        cell.draw_mini_map(screen, cell_size, x, y,color)

    
    player = Player(playerx, playery, "Tom_animation.png", 4, 4, cell_size)

    # Vẽ người chơi với hình chữ nhật
    player_rect = pygame.Rect(x + player.x * cell_size, y + player.y * cell_size, cell_size*1.3, cell_size*1.3)
    pygame.draw.rect(screen, pygame.Color('yellow'), player_rect)

    # Vẽ điểm bắt đầu với hình chữ nhật
    start_rect = pygame.Rect(x + start.x * cell_size, y + start.y * cell_size, cell_size*1.3, cell_size*1.3)
    pygame.draw.rect(screen, pygame.Color('red'), start_rect)

    # Vẽ điểm kết thúc với hình chữ nhật
    end_rect = pygame.Rect(x + end.x * cell_size, y + end.y * cell_size, cell_size*1.3, cell_size*1.3)
    pygame.draw.rect(screen, pygame.Color('blue'), end_rect)
# Hàm vẽ giao diện load game
def draw_load_screen(screen, file_names, selected_maze_index):
    global WIDTH, HEIGHT
    global sound_enabled
    load_game_img = pygame.image.load("backgroundload.png")
    load_game_img = pygame.transform.scale(load_game_img, (WIDTH, HEIGHT))
    sound_on_button = pygame.image.load('sound_on.png')
    sound_on_button = pygame.transform.scale(sound_on_button,(WIDTH // 40, HEIGHT // 20))
    sound_on_button_coord = (WIDTH // 500, HEIGHT // 15)
    sound_on_button_rect = sound_on_button.get_rect(topleft = sound_on_button_coord)
    sound_off_button = pygame.image.load('sound_off.png')
    sound_off_button = pygame.transform.scale(sound_off_button,(WIDTH // 40, HEIGHT // 20))
    sound_off_button_coord = (WIDTH // 500, HEIGHT // 15)
    sound_off_button_rect = sound_off_button.get_rect(topleft = sound_off_button_coord)
    screen.fill((255, 255, 255))  # Xóa màn hình
    screen.blit(load_game_img,(0, 0))
    screen.blit(Back_outgame,(0,0))
    pos = pygame.mouse.get_pos()
    if sound.sound_enabled: 
        screen.blit(sound_on_button, sound_on_button_coord)
    else:
        screen.blit(sound_off_button, sound_off_button_coord)
    font = pygame.font.Font(None, 36)
    text_y = MARGIN

    # Tính toán số lượng maze có thể hiển thị trên một dòng
    num_mazes_per_row = min(len(file_names), NUM_MAZES)
    if len(file_names)==0:
        num_mazes_per_row = 1

    # Tính toán kích thước của mỗi maze và khoảng cách giữa chúng
    maze_WIDTH_mini_maze = (WIDTH_mini_maze - (num_mazes_per_row + 1) * MARGIN) / num_mazes_per_row
    
    maze_HEIGHT_mini_maze = min(maze_WIDTH_mini_maze, HEIGHT_mini_maze - 2 * MARGIN)
    maze_WIDTH_mini_maze = 250
    maze_HEIGHT_mini_maze = 250
    x_spacing = (WIDTH - num_mazes_per_row * maze_WIDTH_mini_maze - (num_mazes_per_row - 1) * MARGIN) / 2
    y_spacing = (HEIGHT - len(file_names) / num_mazes_per_row * (maze_HEIGHT_mini_maze + MARGIN)) / 2
    # Vẽ các maze và tên file lên màn hình
    for i, file_name in enumerate(file_names):
        row = i // num_mazes_per_row
        col = i % num_mazes_per_row

        x = x_spacing + col * (maze_WIDTH_mini_maze + MARGIN)
        y = y_spacing + row * (maze_HEIGHT_mini_maze + MARGIN) 

        maze_rect = pygame.Rect(x, y, maze_WIDTH_mini_maze, maze_HEIGHT_mini_maze)  # Cập nhật maze_rect ở đây
        grid_cells, cols, rows, player, start, end, steps, elapsed_time = load_game(file_name)
        start, end = grid_cells[start[0] + start[1]*cols], grid_cells[end[0] + end[1]*cols]
        draw_mini_maze(screen, grid_cells, cols, rows, player[0],player[1], start, end, x, y, maze_WIDTH_mini_maze,Green, False)

        # Vẽ tên file ở dưới maze
        file_text = font.render(file_name, True, White)
        file_rect = file_text.get_rect()
        file_rect.midtop = (x + maze_WIDTH_mini_maze // 2, y + maze_HEIGHT_mini_maze + 5)

        screen.blit(file_text, file_rect)
        mouse_pos = pygame.mouse.get_pos()
        if maze_rect.collidepoint(mouse_pos):
            selected_maze_index = i  # Lưu chỉ số của maze được chọn

    # Vẽ viền đen xung quanh maze được chọn
    if selected_maze_index is not None:
        selected_x = x_spacing + (selected_maze_index % num_mazes_per_row) * (maze_WIDTH_mini_maze + MARGIN)
        selected_y = y_spacing + (selected_maze_index // num_mazes_per_row) * (maze_HEIGHT_mini_maze + MARGIN)
        selected_rect = pygame.Rect(selected_x, selected_y, maze_WIDTH_mini_maze, maze_HEIGHT_mini_maze)
        pygame.draw.rect(screen, pygame.Color('white'), selected_rect,3)

    pygame.display.flip()
    return

# Hàm chính