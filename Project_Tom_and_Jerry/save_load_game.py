TAIL = '_name_of_file_for_saving_and_loading'
from class_file import*
import login_forms
def save_maze_to_csv(grid_cells, cols, rows, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write maze dimensions
        writer.writerow([cols, rows])
        
        # Write maze cells
        for cell in grid_cells:
            writer.writerow([cell.x, cell.y,
                             int(cell.walls['top']), int(cell.walls['right']),
                             int(cell.walls['bottom']), int(cell.walls['left']),
                             int(cell.visited), int(cell.passed), int(cell.path)])


def save_player_position_to_csv(player, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([player.x, player.y])
def save_end_start_to_csv(start, end, filename):
    with open(filename, mode = 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow([start.x, start.y, end.x, end.y])

def save_time_and_steps_to_csv(steps, elapsed_time, filename):
    """Lưu thời gian và số bước của trò chơi vào tệp CSV."""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([elapsed_time, steps])

def save_game(file_name : str, username, grid_cells, cols, rows, player, start, end, steps):
    # dừng thời gian để lưu 
    elapsed_time = int(game_clock.get_elapsed_time())
    tail1, tail2, tail3, tail4 = '_maze.csv', '_player.csv', '_start_end.csv','_steps_time.csv'
    file_maze = file_name + tail1  #file for saving maze
    file_player = file_name + tail2 #file for saving player's position
    file_start_end = file_name + tail3# file for saving start and end points
    file_steps_time = file_name + tail4# file for saving steps and time
    file_name += TAIL #gắn đuôi để key file_name phân biệt với key user_name
    save_maze_to_csv(grid_cells, cols, rows, file_maze)
    save_player_position_to_csv(player, file_player)
    save_end_start_to_csv(start, end, file_start_end)
    save_time_and_steps_to_csv(steps, elapsed_time, file_steps_time)
    with open('database.json', 'r') as f:
        data = json.load(f)
        for i in range(len(data)):
            if username in data[i]:
                data[i][file_name] = []
                data[i][file_name].append(file_maze) #Phần tử thứ 0 trong list là mê cung
                data[i][file_name].append(file_player)#Phần tử thứ 1 trong list là vị trí người chơi
                data[i][file_name].append(file_start_end)#Phần tử thứ 2 trong list là vị trí bắt đầu và vị trí kết thúc
                data[i][file_name].append(file_steps_time)#Phần tử thứ 3  trong list là số bước và thời gian tại thời điểm dừng game
    with open('database.json', 'w') as out:
        json.dump(data, out, indent = 2)
    
def load_maze_from_csv(filename):
    grid_cells = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        cols, rows = map(int, next(reader))
        for row in reader:
            x, y, top, right, bottom, left, visited, passed, path = map(int, row)
            cell = Cell(x, y)
            cell.walls['top'] = bool(top)
            cell.walls['right'] = bool(right)
            cell.walls['bottom'] = bool(bottom)
            cell.walls['left'] = bool(left)
            cell.visited = bool(visited)
            cell.passed = bool(passed)
            cell.path = bool(path)
            grid_cells.append(cell)
    return grid_cells, cols, rows

def load_player_position_from_csv(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        x, y = map(int, next(reader))
        return (x, y)

def load_start_end_from_csv(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        start_x, start_y, end_x, end_y = map(int, next(reader))
        return (start_x, start_y), (end_x, end_y)

def load_time_and_steps_from_csv(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        elapsed_time, steps = map(float, next(reader))
        return int(elapsed_time), int(steps)

def load_game(file_name):
    file_name += TAIL
    with open('database.json', 'r') as f:
        data = json.load(f)
        for account in data:
            if login_forms.User_name in account:
                if len(account) > 1:
                    if file_name in account:
                        files = account[file_name]
                        grid_cells, cols, rows = load_maze_from_csv(files[0])
                        player = load_player_position_from_csv(files[1])
                        start, end = load_start_end_from_csv(files[2])
                        elapsed_time, steps = load_time_and_steps_from_csv(files[3])
                        print("elapsed_load = ", elapsed_time)
                        return grid_cells, cols, rows, player, start, end, steps, elapsed_time
    return False
        

def remove_file_in_database(file_name):                      #Xóa các tên file ra khỏi database
    file_name += TAIL
    with open('database.json', 'r') as f:
        data = json.load(f)
        for account in data:
            if login_forms.User_name in account:
                if file_name in account:
                    account.pop(file_name)
                
    
    with open('database.json', 'w') as out:
        json.dump(data, out)


def remove_file(file_name):                                 #Xóa các file đã lưu được chỉ định
    file_name +=  TAIL
    with open('database.json', 'r') as f:
        data = json.load(f)
        for account in data:
            if login_forms.User_name in account:
                if file_name in account:
                    os.remove(account[file_name][0])
                    os.remove(account[file_name][1])
                    os.remove(account[file_name][2])
                    os.remove(account[file_name][3])
