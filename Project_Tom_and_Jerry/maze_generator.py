from class_file import*
from global_variable import*
from algorithms import *
# Hàm tạo mê cung
def generate_maze(cols, rows, TILE):
    global Bottom_right_x
    grid_cells = [Cell(x, y) for y in range(rows) for x in range(cols)]
    current_cell = grid_cells[0]
    array = []
    break_count = 1
    maze = grid_cells
    # Tạo một đối tượng Drawer mê cung ngoài vòng lặp
    drawer = MazeDrawer(cols ,rows, maze, interactive=True)
    if cols == 100 :
        TILE = Bottom_right_x//cols 
        drawer.Update_TILE(TILE)
    speed =  100
    if cols== 20 : 
        speed = 2
    elif cols== 40 : 
        speed = 5 
    elif cols== 100 : 
        speed = 100
    while break_count !=cols * rows:
        current_cell.visited = True
        next_cell = current_cell.check_neighbors(grid_cells, cols, rows)
        if next_cell:
            next_cell.visited = True
            break_count += 1
            array.append(current_cell)
            remove_walls(current_cell, next_cell, grid_cells, cols, rows, True)
            if break_count % speed == 0 : 
                drawer.draw()
                pygame.display.update()
            current_cell = next_cell
        elif array:
            current_cell = array.pop()

    for j in range(len(grid_cells)):
        grid_cells[j].visited = False 
    if cols != 100:
        divide_maze(grid_cells, cols, rows)
    return grid_cells



# Hàm loại bỏ tường giữa hai ô
def remove_walls(current, next, grid_cells, cols, rows, flag):
    dx = current.x - next.x
    x = random.random()
    if dx == 1:
        if current.x < cols - 1 and random.random() > 0.4 and flag:
            current.walls['right'] = False
            grid_cells[current.x + current.y*cols + 1].walls['left'] = False
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        if current.x > 0 and random.random() > 0.4 and flag:
            current.walls['left'] = False
            grid_cells[current.x + current.y*cols - 1].walls['right'] = False
        current.walls['right'] = False
        next.walls['left'] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False

def build_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = True
        next.walls['right'] = True
    if dx == -1:
        current.walls['right'] = True
        next.walls['left'] = True
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = True
        next.walls['bottom'] = True
    if dy == -1:
        current.walls['bottom'] = True
        next.walls['top'] = True



def divide_maze(grid_cells, cols, rows):
    start = grid_cells[0]
    rad = (cols**2 + rows**2)//4
    list_cell = []
    for vertex in grid_cells:
        if euclid_distance(start, vertex) >= rad and euclid_distance(start, vertex) <= 3*rad:
            list_cell.append(vertex)
    while (len(DFS_spread(grid_cells, start, cols, rows)) ==  len(grid_cells)):
        boundary = choice(list_cell)
        neighbors = boundary.check_neighbors_pass(grid_cells, cols, rows)
        neighbor = choice(neighbors)
        build_walls(boundary, neighbor)
        if (boundary.walls['top'] and boundary.walls['bottom'] and boundary.walls['left'] and boundary.walls['right']) or (neighbor.walls['top'] and neighbor.walls['bottom'] and neighbor.walls['left'] and neighbor.walls['right']):
            remove_walls(boundary, neighbor, grid_cells, cols, rows, False)
           
