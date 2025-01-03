import pygame
from global_variable import *
from save_load_game import* 
import json

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.links = {}
        self.visited = False
        self.passed = False
        self.path = False
        self.thickness = 1

    def draw_mini_map(self, screen, TILE, maze_x, maze_y):
        x, y = maze_x + self.x * TILE, maze_y + self.y * TILE

        # Vẽ các bức tường bằng cách vẽ các hình chữ nhật
        if self.walls['top']:
            pygame.draw.rect(screen, pygame.Color('green'), pygame.Rect(x, y, TILE, self.thickness))
        if self.walls['right']:
            pygame.draw.rect(screen, pygame.Color('green'), pygame.Rect(x + TILE - self.thickness, y, self.thickness, TILE))
        if self.walls['bottom']:
            pygame.draw.rect(screen, pygame.Color('green'), pygame.Rect(x, y + TILE - self.thickness, TILE, self.thickness))
        if self.walls['left']:
            pygame.draw.rect(screen, pygame.Color('green'), pygame.Rect(x, y, self.thickness, TILE))
        if self.path:
            pygame.draw.rect(screen, pygame.Color('red'), (x + 10, y + 10, TILE - 20, TILE - 20))

# Hàm vẽ mỗi maze mini
def draw_mini_maze(screen, grid_cells, cols, rows, player, start, end, x, y, size):
    cell_size = size / max(cols, rows)
    for cell in grid_cells:
        cell.draw_mini_map(screen, cell_size, x, y)
    start, end = grid_cells[start[0] + start[1]*cols], grid_cells[end[0] + end[1]*cols]
    player = Player(player[0], player[1],"Tom_animation.png",4,4,cell_size)
    pygame.draw.circle(screen, pygame.Color('yellow'), (x + player.x * cell_size + cell_size // 2, y + player.y * cell_size + cell_size // 2), cell_size // 4)
    pygame.draw.circle(screen, pygame.Color('red'), (x + start.x * cell_size + cell_size // 2, y + start.y * cell_size + cell_size // 2), cell_size // 4)
    pygame.draw.circle(screen, pygame.Color('blue'), (x + end.x * cell_size + cell_size // 2, y + end.y * cell_size + cell_size // 2), cell_size // 4)

# Hàm vẽ giao diện load game
def draw_load_screen(screen, file_names, selected_maze_index):
    screen.fill((255, 255, 255))  # Xóa màn hình

    font = pygame.font.Font(None, 36)
    text_y = MARGIN

    # Tính toán số lượng maze có thể hiển thị trên một dòng
    num_mazes_per_row = min(len(file_names), NUM_MAZES)

    # Tính toán kích thước của mỗi maze và khoảng cách giữa chúng
    maze_WIDTH_mini_maze = (WIDTH_mini_maze - (num_mazes_per_row + 1) * MARGIN) // num_mazes_per_row
    #print(maze_WIDTH_mini_maze)
    
    maze_HEIGHT_mini_maze = min(maze_WIDTH_mini_maze, HEIGHT_mini_maze - 2 * MARGIN)
    #print(maze_HEIGHT_mini_maze)
    maze_WIDTH_mini_maze = 250
    maze_HEIGHT_mini_maze = 250
    #x_spacing = WIDTH//10
    #y_spacing = HEIGHT//3
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
        draw_mini_maze(screen, grid_cells, cols, rows, player, start, end, x, y, maze_WIDTH_mini_maze)

        # Vẽ tên file ở dưới maze
        file_text = font.render(file_name, True, (0, 0, 0))
        file_rect = file_text.get_rect()
        file_rect.midtop = (x + maze_WIDTH_mini_maze // 2, y + maze_HEIGHT_mini_maze + 10)

        screen.blit(file_text, file_rect)
        mouse_pos = pygame.mouse.get_pos()
        if maze_rect.collidepoint(mouse_pos):
            selected_maze_index = i  # Lưu chỉ số của maze được chọn

    # Vẽ viền đen xung quanh maze được chọn
    if selected_maze_index is not None:
        selected_x = x_spacing + (selected_maze_index % num_mazes_per_row) * (maze_WIDTH_mini_maze + MARGIN)
        selected_y = y_spacing + (selected_maze_index // num_mazes_per_row) * (maze_HEIGHT_mini_maze + MARGIN)
        selected_rect = pygame.Rect(selected_x, selected_y, maze_WIDTH_mini_maze, maze_HEIGHT_mini_maze)
        pygame.draw.rect(screen, pygame.Color('black'), selected_rect, 3)

    pygame.display.flip()

def load_filegame():
    file_names =  []
    with open('database.json','r') as f :
        data = json.load(f)
        for account in data : 
            if login_forms.User_name in account : 
                print(account)
                if len(account) > 1 :
                    for key in account :
                        if (key!=login_forms.User_name):
                            tmp = key.split("_")
                            file_names.append(tmp[0])
                            print(tmp[0])
    return file_names 

# Hàm chính
def main(file_names):
    # Tính toán số lượng maze có thể hiển thị trên một dòng
    num_mazes_per_row = min(len(file_names), NUM_MAZES)

    # Tính toán kích thước của mỗi maze và khoảng cách giữa chúng
    maze_WIDTH_mini_maze = (WIDTH_mini_maze - (num_mazes_per_row + 1) * MARGIN) // num_mazes_per_row
    maze_HEIGHT_mini_maze = min(maze_WIDTH_mini_maze, HEIGHT_mini_maze - 2 * MARGIN)
    x_spacing = (WIDTH - num_mazes_per_row * maze_WIDTH_mini_maze - (num_mazes_per_row - 1) * MARGIN) // 2
    y_spacing = (HEIGHT - len(file_names) // num_mazes_per_row * (maze_HEIGHT_mini_maze + MARGIN)) // 2 
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Load Game')

    # Lấy danh sách các file maze đã lưu
    file_names = load_filegame()

    selected_maze_index = None  # Biến lưu chỉ số của maze hiện tại được chọn

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Xử lý sự kiện khi người chơi nhấn chuột
                mouse_pos = pygame.mouse.get_pos()
                for i, file_name in enumerate(file_names):
                    row = i // num_mazes_per_row
                    col = i % num_mazes_per_row
                    x = x_spacing + col * (maze_WIDTH_mini_maze + MARGIN)
                    y = y_spacing + row * (maze_HEIGHT_mini_maze + MARGIN)
                    maze_rect = pygame.Rect(x, y, maze_WIDTH_mini_maze, maze_HEIGHT_mini_maze)  # Cập nhật maze_rect ở đây
                    if maze_rect.collidepoint(mouse_pos):
                        print(file_name)
                        #selected_maze_index = i  # Lưu chỉ số của maze được chọn
                        

        # Vẽ giao diện load game
        draw_load_screen(screen, file_names, selected_maze_index)

    pygame.quit()

if __name__ == "__main__":
    main(load_filegame())
