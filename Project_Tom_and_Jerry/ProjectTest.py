import pygame
import pyautogui
from class_file import *
from global_variable import *
import sound
from menu import *
from end_screen import *
from class_file import*
from algorithms import *
from menu import*
from end_screen import*
from maze_generator import*
from save_load_game import*
import save_load_game
import login_forms
from dashboard import *
from get_ranking import*
from load_game_draw import *
from screen_in_game import *
from timer import *
# Định nghĩa biến font
pygame.font.init()
font = pygame.font.Font(None, 36)

pygame.init()
pygame.mixer.init()
pygame.time.set_timer(pygame.USEREVENT, 1000)
# bắt đầu vào game 
game_clock.start()
def reset_game(grid_cells, TILE,drawer, start, end, cols, rows):
    # Thiết lập lại trạng thái trò chơi về trạng thái ban đầu
    global paused
    paused = False
    global COLS
    global ROWS
    global ChosingStartendMode
    screen.fill(Black)
    background = pygame.image.load("ingame.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    sound_on_button = pygame.image.load('sound_on.png')
    sound_on_button = pygame.transform.scale(sound_on_button,(WIDTH // 40, HEIGHT // 20))
    sound_on_button_coord = (WIDTH // 500, HEIGHT // 18)
    sound_on_button_rect = sound_on_button.get_rect(topleft = sound_on_button_coord)
    sound_off_button = pygame.image.load('sound_off.png')
    sound_off_button = pygame.transform.scale(sound_off_button,(WIDTH // 40, HEIGHT // 20))
    sound_off_button_coord = (WIDTH // 500, HEIGHT // 18)
    sound_off_button_rect = sound_off_button.get_rect(topleft = sound_off_button_coord)
    screen.blit(background, (0, 0))
    drawer = MazeDrawer(cols, rows,grid_cells,True)
    drawer.draw()
    
    pygame.display.update()
    pygame.display.flip()
    
    # Cho phép người chơi chọn lại vị trí ban đầu
    for cell in grid_cells:
        cell.path = False
    return grid_cells,drawer, start, end

def new_game(grid_cells, TILE, drawer):
    global paused
    paused = False
    global COLS
    global ROWS
    global DELTA_X
    global DELTA_Y
    global ChosingStartendMode
    screen.fill(Black)
    DELTA_X = WIDTH//8   # dời ngang mê cung 
    DELTA_Y = HEIGHT//5  # dời dọc mê cung xuống 
    pygame.display.update()
    background = pygame.image.load("ingame.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    grid_cells = generate_maze(COLS, ROWS, TILE)
    drawer = MazeDrawer(COLS, ROWS,grid_cells,True)
    drawer.draw()
    pygame.display.update()
    if ChosingStartendMode == 1:
        start, end = select_start_end_manually(grid_cells, COLS, ROWS, TILE, sc)
        path = DFS_spread(grid_cells, start, COLS, ROWS)
        while not end in path:
            start, end = Ask_Choose_Again(grid_cells, COLS, ROWS, TILE, sc, drawer, background)
            path = DFS_spread(grid_cells, start, COLS, ROWS)
    else:
        start, end = select_start_end(grid_cells, COLS, ROWS)
    # Cho phép người chơi chọn lại vị trí ban đầu
    for cell in grid_cells:
        cell.path = False
    return grid_cells,drawer, start, end

#time_started = False
def main(TILE = None, step = None,cols = None, rows = None, time_action = 0, grid_cells = None,player = None, start  = None, end = None):
     
    global Mode_Findpath
    global Mode_game_bot
    global Game_mode
    global paused
    global COLS
    global ROWS
    global ChosingStartendMode
    global current_direction
    global DELTA_X
    global DELTA_Y
    flag = sound.inMenu
    DELTA_X = WIDTH//8   # dời ngang mê cung 
    DELTA_Y = HEIGHT//5  # dời dọc mê cung xuống 
    pygame.display.update()
    sound.inMenu = False 
    if flag:
        for i in range(2):
            sound.toggle_sound()
    if TILE == None:
        TILE = Bottom_right_x//COLS  
    else:TILE = Bottom_right_x//cols      
    sc = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()
    sc.fill(pygame.Color('aquamarine'))
    screen.fill(Black)
    if cols == None and rows == None: 
        cols, rows = COLS, ROWS
    background = pygame.image.load("ingame.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    if grid_cells == None: 
        grid_cells= generate_maze(cols, rows, TILE)
    drawer = MazeDrawer(cols, rows, grid_cells, interactive=True)  # Tạo một thực thể MazeDrawer
    drawer.Update_TILE(TILE)
    screen.blit(background, (0, 0))
    if cols == 100 : 
        drawer.Update_TILE(TILE)
    drawer.draw()  # Vẽ mê cung lên màn hình
    #[cell.draw(sc, TILE) for cell in grid_cells]
    pygame.display.flip()
    clock.tick(120)
    game_clock.start(time_action)
    if start == None and end == None:
        start, end = grid_cells[0],grid_cells[-1]
        if ChosingStartendMode == 1 :
        # Chọn điểm bắt đầu và điểm kết thúc thủ công
            start, end = select_start_end_manually(grid_cells,cols, rows, TILE, sc)
            # bắt đầu tính giờ chơi game
            draw_dashboard(step, optionsettings[0], optionsettings[1], optionsettings[2])
            path = DFS_spread(grid_cells, start, cols, rows)
            while not(end in path):
               start,end = Ask_Choose_Again(grid_cells, cols,rows, TILE, sc,drawer,background)
               path = DFS_spread(grid_cells, start, cols, rows)
        elif ChosingStartendMode == 2: 
            start, end  = select_start_end(grid_cells,cols, rows) 
            # bắt đầu tính giờ
            start_real = Start(start.x,start.y,"Start_animation.png",TILE)
            mouse  = Mouse(end.x,end.y,"Jerry_animationBB.png",TILE)   
            pygame.time.delay(400)
            start_real.draw(sc,TILE)
            pygame.time.delay(400)
            mouse.draw(sc,TILE)
    else:
        start, end = grid_cells[start[0] + start[1]*cols], grid_cells[end[0] + end[1]*rows]
    if (cols== 100):     
        TILE = 100
    drawer = MazeDrawer(cols, rows, grid_cells, interactive=True)  # Tạo một thực thể MazeDrawer    
    if player == None: 
        player = Player(start.x,start.y,"Tom_animation.png",4,4,TILE)  
    else:
        player = Player(player[0], player[1],"Tom_animation.png",4,4,TILE)
    
    start_real = Start(start.x,start.y,"Start_animation.png",TILE)
    mouse  = Mouse(end.x,end.y,"Jerry_animationBB.png",TILE)
    start_real.draw(sc,TILE)
    intro_transition() 
    
    if (cols== 100):  
        player.updatecamera(player)
    maze_WIDTH_mini_maze = 250 
    if cols == 100 :
        drawer.Update_TILE(TILE)
    if cols == 100 : 
        maze_WIDTH_mini_maze = 500
    
    drawer.draw()  # Vẽ mê cung lên màn hình
    player.draw(sc,TILE)
    mouse.draw(sc,TILE)
    position = []
    path = None
    Allow = False
    time = 60
    player.draw(sc, TILE)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
    if step == None: step = 0
    start_time = pygame.time.get_ticks()
    option_after_game = None
    

    
    while True:
        player_index = player.x + player.y * cols
        target_cell = grid_cells[player_index]
        current_cell = target_cell
        if target_cell == end:
                playSound(3)
                elapsed_time = int(game_clock.get_elapsed_time())
                get_rank(elapsed_time, step, cols)
                screen.blit(background, (0, 0))
                for i in range(70):
                    drawer.draw()
                    current_direction = "smash"
                    player.move("smash",grid_cells,cols,rows)
                    player.draw(sc, TILE)
                    player.animationhidden.update()
                    pygame.display.update()
                    pygame.time.delay(10)
                    player.animationsmash.update()
                    clock.tick(120)
                    pygame.display.update()
                pygame.time.delay(400)
                player.move("laugh",grid_cells,cols,rows)
                current_direction = "laugh"
                player.draw(sc,TILE)
                player.animationlaugh.update()
                for i in range(100):
                    drawer.draw()
                    player.draw(sc,TILE)
                    player.animationlaugh.update()
                    mouse.move("Die",grid_cells,8,1)
                    mouse.animation_die.update()
                    mouse.draw(sc,TILE)
                    pygame.time.delay(20)
                    pygame.display.update()
                    clock.tick(120)
                pygame.time.delay(400)
                DELTA_X = WIDTH//8   # dời ngang mê cung 
                DELTA_Y = HEIGHT//5  # dời dọc mê cung xuống 
                option_after_game = winning_screen(elapsed_time, step)
                player.returncamera()
                TILE = Bottom_right_x//COLS 
                
                if option_after_game:
                    player.returncamera()
                    for i in range(2):
                        sound.toggle_sound()
                    main()
                  
                    
                    paused = False
                    Allow = False
                    step = 0 
                    pass
                else:
                    player.returncamera()
                    xulymenu()
                    break
        # KIỂM TRA TIME UP
        check_time_up = game_clock.get_elapsed_time()

        if int(check_time_up) > 5*60: #Chơi lâu hơn 15p là thua
            playSound(5)
            player.returncamera()
            TILE = Bottom_right_x//COLS 
            option_after_game = game_over_time_up(step) 
            if option_after_game:
                for i in range(2):
                    sound.toggle_sound()
                main()
            else:   
                player.returncamera()
                xulymenu()
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.USEREVENT:
                time -= 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x :
                    if event.key == pygame.K_x :
                        sound.toggle_sound()
                if event.key == pygame.K_e:
                    player.returncamera()
                    xulymenu_settings()
                    main()
                    
                playSound(4)
                if(Game_mode  == "Player" or Game_mode == "Both"):
                    if event.key == pygame.K_UP:
                        current_direction ='up'
                    elif event.key == pygame.K_DOWN:
                        current_direction ='down'
                    elif event.key == pygame.K_LEFT:
                        current_direction = 'left'
                    elif event.key == pygame.K_RIGHT:
                        current_direction = 'right'         
                    else:
                        current_direction = "None"
                        player.move("None",grid_cells,cols,rows)
                    
                if event.key == pygame.K_w:
                    if(Game_mode =="Bot" or Game_mode=="Both"):
                        if Mode_Findpath == 0:
                            route, path = DFS_findPath(grid_cells, target_cell, end, cols, rows, True)
                        elif Mode_Findpath == 1:
                            route, path = BFS_findPath(grid_cells, target_cell, end, cols, rows, True)
                        elif Mode_Findpath == 2 :
                            route, path = AStar_findPath(grid_cells,target_cell,end,cols,rows, True)
                        elif Mode_Findpath == 3:
                            route,path =  Dijkstra_FindPath(grid_cells,target_cell,end,cols,rows,True)
                        Mode_game_bot  = 2
                        tmp =[]
                        cnt =  0 
                        if path:
                            if route :
                                for rou in route : 
                                    rou.seen = True
                                    tmp.append(rou)
                                    rou.draw(sc,TILE)
                                    draw_mini_maze(screen, grid_cells, cols, rows, player.x,player.y, start, end, 0, 0, maze_WIDTH_mini_maze,Black)
                                    pygame.display.update()
                                    playSound(4)
                                    for events in pygame.event.get():
                                        if events.type == pygame.KEYDOWN:
                                            if events.key == pygame.K_w:
                                                Mode_game_bot = 1
                                                Allow = False                                
                                    if Mode_game_bot == 1 : 
                                        for cells in grid_cells:
                                            cells.path = False
                                            cells.seen = False
                                        break
                                if len(route) == len(tmp): 
                                    Allow = True
                                    for vertex in tmp:
                                        vertex.seen = False
                                    for vertex in path:
                                        vertex.path = True
                                if (Allow):
                                    cnt = 0
                                    path2 = path.copy()
                                    for cell in path:
                                        for events in pygame.event.get():
                                            if events.type == pygame.KEYDOWN:
                                                if events.key == pygame.K_w:
                                                    Mode_game_bot = 1
                                                    Allow = False 
                                                    break
                                        if Mode_game_bot == 1 : 
                                            for cells in grid_cells:
                                                cells.path = False
                                                cells.seen = False
                                            break
                                        if ((cell.x - player.x),(cell.y-player.y)) ==(0,1) :
                                            player.move('down',grid_cells,cols,rows)
                                        elif ((cell.x - player.x),(cell.y-player.y)) ==(0,-1) :
                                            player.move('up',grid_cells, cols, rows)
                                        elif ((cell.x - player.x),(cell.y-player.y)) ==(1,0) :
                                            player.move('right',grid_cells,cols, rows)
                                        elif ((cell.x - player.x),(cell.y-player.y)) ==(-1,0) :
                                            player.move('left',grid_cells, cols, rows)
                                        cell.path= False
                                        step += 1
                                        screen.blit(background, (0, 0))
                                        drawer.draw()
                                        draw_mini_maze(screen, grid_cells, cols, rows, player.x,player.y, start, end, 0, 0, maze_WIDTH_mini_maze,Black)
                                        if  Mode_Findpath  != 5 :
                                            for cell in path:
                                                if cell.path == True : 
                                                    cell.draw(sc,TILE)
                                        start_real.draw(sc,TILE)
                                        mouse.draw(sc,TILE)
                                        draw_dashboard(step, optionsettings[0], optionsettings[1], optionsettings[2])
                                        player.draw(sc, TILE)
                                        player.animation.update()
                                        FPS = 60 
                                        if cols == 100 : 
                                            FPS = 120 
                                            
                                        clock.tick(60)
                                        pygame.display.update()
                                            
                                        playSound(4)
                                    
                                    Allow = False
                                
                    #1 là DFS , 2 là BFS  , 3 là Astar,4 là Dijkstra
                    
                elif event.key == pygame.K_q:
                   
                    Mode_Findpath = (Mode_Findpath+1)%4
                    print(Mode_Findpath)
                    if Mode_Findpath == 0:
                        optionsettings[2] = "DFS"
                    elif Mode_Findpath == 1:
                        optionsettings[2] = "BFS"
                    elif Mode_Findpath == 2:
                        optionsettings[2] = "Astar"
                    elif Mode_Findpath == 3: 
                        optionsettings[2] = "Dijkstra"
                    print(Mode_Findpath)
                elif event.key == pygame.K_SPACE:
                    if len(position) == 0:
                        if Mode_Findpath == 0:
                            path = DFS_findPath(grid_cells, target_cell, end, cols, rows, False)
                        elif Mode_Findpath == 1:
                            path = BFS_findPath(grid_cells, target_cell, end, cols, rows, False)
                        elif Mode_Findpath == 2:
                            path = AStar_findPath(grid_cells,target_cell,end, cols, rows, False)
                        elif Mode_Findpath == 3:
                            path = Dijkstra_FindPath(grid_cells,target_cell,end, cols, rows, False)
                        if path:
                            flagpath = False
                            for cell in path:
                                if flagpath : 
                                    break
                                #drawer.draw()  
                                cell.path = True           
                                #cell.draw(sc,TILE)
                                #draw_mini_maze(screen, grid_cells, cols, rows, player.x,player.y, start, end, 0, 0, maze_WIDTH_mini_maze,Black)
                                for event1 in pygame.event.get():
                                    if event1.type == pygame.QUIT:
                                        pygame.quit()
                                        quit()
                                    elif event1.type == pygame.KEYDOWN:
                                        if event1.key == pygame.K_SPACE:
                                            for cell in path : 
                                                cell.path = False
                                            position.append(target_cell)
                                            screen.blit(background, (0, 0))
                                            drawer.draw()
                                            [cell.draw(sc, TILE) for cell in path]
                                            start_real.draw(sc,TILE)
                                            mouse.draw(sc,TILE)
                                            player.move("None", grid_cells, cols, rows)
                                            player.animation2.update()
                                            player.draw(sc, TILE)
                                            draw_dashboard(step, optionsettings[0], optionsettings[1], optionsettings[2])
                                            draw_mini_maze(screen, grid_cells, cols, rows, player.x,player.y, start, end, 0, 0, maze_WIDTH_mini_maze,Black)
                                            pygame.display.update()
                                            flagpath = True
                                    elif event1.type == MOUSEBUTTONDOWN : 
                                        send_key_space()
                                if cols!=100 :     
                                    #current_time = pygame.time.get_ticks()
                                    #elapsed_time = current_time - start_time  
                                    [cell.draw(sc, TILE) for cell in grid_cells]
                                    start_real.draw(sc,TILE)
                                    mouse.draw(sc,TILE)
                                    player.move("None", grid_cells, cols, rows)
                                    player.animation2.update()
                                    player.draw(sc, TILE)
                                    draw_dashboard(step, optionsettings[0], optionsettings[1], optionsettings[2])
                                    draw_mini_maze(screen, grid_cells, cols, rows, player.x,player.y, start, end, 0, 0, maze_WIDTH_mini_maze,Black)
                                    pygame.display.update()
                            position.append(target_cell)
                            screen.blit(background, (0, 0))
                            drawer.draw()
                            player.draw(sc, TILE)
                            draw_dashboard(step, optionsettings[0], optionsettings[1], optionsettings[2])
                            draw_mini_maze(screen, grid_cells, cols, rows, player.x,player.y, start, end, 0, 0, maze_WIDTH_mini_maze,Black)
                            pygame.display.update()
                            [cell.draw(sc, TILE) for cell in path]
                            start_real.draw(sc,TILE)
                            mouse.draw(sc,TILE)
                            pygame.display.update()
                            clock.tick(120)
                            #pygame.time.delay(50)
    
                    elif position[-1] == target_cell:
                        if path:
                            for cell in path:
                                cell.path = False
                            position = []
                    else:
                        if path:
                            for cell in path:
                                cell.path = False
                            position = []
                    
                # Phím bổ sung để tạm dừng, thiết lập lại, tiếp tục
                if event.key == pygame.K_ESCAPE:  # Tạm dừng trò chơi
                    pygame.mixer.pause()
                    paused = not paused
                elif event.key == pygame.K_r:  # Thiết lập lại trò chơi
                    player.returncamera() 
                  
                    print(cols, rows, COLS, ROWS, TILE)
                    grid_cells,drawer, start, end = reset_game(grid_cells,TILE,drawer, start, end, cols, rows)
                    # reset đồng hồ
                    game_clock.start()
                    DELTA_X = WIDTH//8   # dời ngang mê cung 
                    DELTA_Y = HEIGHT//5  # dời dọc mê cung xuống 
                    player.x, player.y = start.x, start.y
                    if cols == 100:
                        player.updatecamera(player)
                    player_index = player.x + player.y * cols
                    target_cell = grid_cells[player_index]
                    start_real = Start(start.x,start.y,"Start_animation.png",TILE)
                    mouse = Mouse(end.x,end.y,"Jerry_animationBB.png",TILE)
                    paused = False
                    step = 0 
                elif event.key == pygame.K_m:  # Tiếp tục trò chơi
                    if paused:
                        paused = False
                    player.returncamera()
                    xulymenu()
                    
                    
                    
                elif event.key == pygame.K_s: 
                    if paused:
                        screen.fill(Black)
                        screen.blit(background, (0, 0))
                        drawer.draw()  # Vẽ mê cung lên màn hình
                        [cell.draw(sc, TILE) for cell in grid_cells]
                        player.animation.update()
                        pygame.time.delay(50)
                        start_real.draw(sc,TILE)
                        mouse.animation.update()
                        start_real.animation.update()
                        player.draw(sc, TILE)
                        mouse.draw(sc,TILE)
                    s = save_screen(sc)
                    if s!=None:
                        save_game(s, login_forms.User_name,grid_cells, cols, rows, player, start, end, step)
                        
                    screen.fill(Black)
                    screen.blit(background, (0, 0))
                    drawer.draw()  # Vẽ mê cung lên màn hình
                    [cell.draw(sc, TILE) for cell in grid_cells]
                    player.animation.update()
                    pygame.time.delay(50)
                    start_real.draw(sc,TILE)
                    mouse.animation.update()
                    start_real.animation.update()
                    player.draw(sc, TILE)
                    mouse.draw(sc,TILE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if paused:
                    #start_time = pygame.time.get_ticks()
                    #reset đồng hồ
                    game_clock.start()
                # Xử lý sự kiện chuột
                    menu,reset,save = pause_screen(sc)
                    mouse_pos = pygame.mouse.get_pos()
                    if reset.collidepoint(mouse_pos):
                        grid_cells,drawer, start, end = reset_game(grid_cells,TILE,drawer, start, end, cols, rows)
                        # reset đồng hồ
                        game_clock.start()
                        player.x, player.y = start.x, start.y
                        if cols == 100 : 
                         player.updatecamera(player)
                
                        player_index = player.x + player.y * cols
                        target_cell = grid_cells[player_index]
                        start_real = Start(start.x,start.y,"Start_animation.png",TILE)
                        mouse = Mouse(end.x,end.y,"Jerry_animationBB.png",TILE)
                        paused = False
                        step = 0 
                        pass
                    elif save.collidepoint(mouse_pos):
                        if paused:
                            screen.fill(Black)
                            screen.blit(background, (0, 0))
                            drawer.draw()  # Vẽ mê cung lên màn hình

                            [cell.draw(sc, TILE) for cell in grid_cells]
                        
                            player.animation.update()
                            pygame.time.delay(50)
                            start_real.draw(sc,TILE)
                            mouse.animation.update()
                            start_real.animation.update()
                            player.draw(sc, TILE)
                            mouse.draw(sc,TILE)
                        s = save_screen(sc)
                        if s!=None:
                           save_game(s, login_forms.User_name,grid_cells, cols, rows, player, start, end, step)
                        screen.fill(Black)
                        screen.blit(background, (0, 0))
                        drawer.draw()  # Vẽ mê cung lên màn hình
                        [cell.draw(sc, TILE) for cell in grid_cells]
                        player.animation.update()
                        pygame.time.delay(50)
                        start_real.draw(sc,TILE)
                        mouse.animation.update()
                        start_real.animation.update()
                        player.draw(sc, TILE)
                        mouse.draw(sc,TILE)
                        
                    elif menu.collidepoint(mouse_pos):
                        if paused:
                            paused = False
                        DELTA_X = WIDTH//8   # dời ngang mê cung 
                        DELTA_Y = HEIGHT//5  # dời dọc mê cung xuống 
                        #drawer.Update_TILE(Bottom_right_x//COLS )
                        player.returncamera()
                        xulymenu()
                    else: 
                            paused = not paused
                            inMenu = True
                            for i in range(2):
                                sound.toggle_sound() 
                else:
                    pos = pygame.mouse.get_pos()
                    if event.button == 1 : 
                        #handle_back_button_click(pos)
                        handle_move(pos)
                        if Game_mode == "Player":
                            handle_suggest_button_click(pos)
                        else :
                            handle_play_bot_button_click(pos)  
                        handle_setting_back(pos)
                        handle_change_algorithm_button_click(pos)
                        handle_pause_button_click(pos)
                        handle_sound_button(pos)
            else:
                current_direction = "None"  
                player.move("None",grid_cells,cols, rows)
        if paused:             
            menu,reset,save = pause_screen(sc)
            continue  # Bỏ qua phần còn lại của vòng lặp nếu tạm dừng        
        if current_direction == 'up':
            player.move('up', grid_cells, cols, rows)
        elif current_direction == 'down':
            player.move('down', grid_cells, cols, rows)
        elif current_direction == 'left':
            player.move('left', grid_cells, cols, rows)
        elif current_direction == 'right':
            player.move('right', grid_cells, cols, rows)        
        if target_cell.x != player.x or target_cell.y != player.y:
            step += 1
        grid_cells[player_index].path = False
        draw_dashboard(step, optionsettings[0], optionsettings[1], optionsettings[2])        
        sc.fill(pygame.Color('aquamarine'))
        screen.fill(Black)
        screen.blit(background, (0, 0))
        drawer.draw()  # Vẽ mê cung lên màn hình


        [cell.draw(sc, TILE) for cell in grid_cells]

        player.animation.update()
        pygame.time.delay(25)
        start_real.draw(sc,TILE)
        mouse.animation.update()
        start_real.animation.update()
        player.draw(sc, TILE)
        mouse.draw(sc,TILE)
        draw_mini_maze(screen, grid_cells, cols, rows, player.x,player.y, start, end, 0, 0, maze_WIDTH_mini_maze,Black)
        
        
def continue_game(file_name):
    res = load_game(file_name)
    if res:
        grid_cells, cols, rows, player, start, end, step, elapsed_time = res
        if (COLS == 100):
            TILE = 100 
        else:
            TILE = Bottom_right_x//cols
        if sound.sound_enabled:
            transition_sound.play()
            sleep(1)
            mixer.music.load('Background.ogg')
            mixer.music.play(-1)       
        main(TILE, step, cols, rows, elapsed_time, grid_cells,player, start, end)
    else:
        return False
def guide():
    global WIDTH,HEIGHT
    global Back_outgame
    global screen
    global rendered_text
    optionguide = 0 
    if optionguide == 0 : 
        guide_background =pygame.image.load('guide1.png')
    elif optionguide == 1 : 
        guide_background = pygame.image.load('guide2.png')
    guide_background  = pygame.transform.scale(guide_background,(WIDTH,HEIGHT))
    guide_background = pygame.image.load('guide.png')
    guide_background = pygame.transform.scale(guide_background,(WIDTH,HEIGHT))
    sound_on_button = pygame.image.load('sound_on.png')
    sound_on_button = pygame.transform.scale(sound_on_button,(WIDTH // 40, HEIGHT // 20))
    sound_on_button_coord = (WIDTH // 500, HEIGHT // 15)
    sound_on_button_rect = sound_on_button.get_rect(topleft = sound_on_button_coord)
    sound_off_button = pygame.image.load('sound_off.png')
    sound_off_button = pygame.transform.scale(sound_off_button,(WIDTH // 40, HEIGHT // 20))
    sound_off_button_coord = (WIDTH // 500, HEIGHT // 15)
    sound_off_button_rect = sound_off_button.get_rect(topleft = sound_off_button_coord)
    screen.fill(Black)
    running = True
    while running :
        if optionguide == 0 : 
            guide_background =pygame.image.load('guide1.png')
            guide_background  = pygame.transform.scale(guide_background,(WIDTH,HEIGHT))
        elif optionguide == 1 : 
            guide_background = pygame.image.load('guide2.png')
            guide_background  = pygame.transform.scale(guide_background,(WIDTH,HEIGHT))
        screen.fill(Black)
        screen.blit( guide_background,(0,0))
        screen.blit(Back_outgame,(0,0))
       
        if sound.sound_enabled: 
            screen.blit(sound_on_button, sound_on_button_coord)
        else:
            screen.blit(sound_off_button, sound_off_button_coord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE: 
                    running = False
                elif event.key == pygame.K_RIGHT:
                    optionguide = (optionguide +  1 ) %2
                elif event.key == pygame.K_LEFT : 
                    optionguide = (optionguide - 1)% 2 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    mouse_pos = pygame.mouse.get_pos()
                    backbutton = pygame.Rect(0,0,rendered_text.get_width(),rendered_text.get_height())
                    if backbutton.collidepoint(mouse_pos):
                        return
                    elif sound_on_button_rect.collidepoint(mouse_pos):
                        sound.toggle_sound()
                    else:
                        optionguide = (optionguide + 1) % 2
                  
                    
                 
            
        pygame.display.update()

def xulymenu():
    global rendered_text
    global screen
    
    
    menu_option = 0
    in_menu = True
    flag = (sound.inMenu == False)
    sound.inMenu = True
    if flag:
        for i in range(2):
            sound.toggle_sound()
  
    guide_button = pygame.image.load('guide.png')
    guide_button = pygame.transform.scale(guide_button,(WIDTH // 8, HEIGHT // 8))
    guide_button_coord = (WIDTH // 500, 4*HEIGHT // 5)
    guide_button_rect = guide_button.get_rect(topleft=guide_button_coord)
    logout_button = pygame.image.load('switch_to_account.png')
    logout_button = pygame.transform.scale(logout_button,(WIDTH // 6, HEIGHT // 8))
    logout_button_coord = (WIDTH // 500, 3 * HEIGHT // 5 + HEIGHT // 15)
    logout_button_rect = logout_button.get_rect(topleft=logout_button_coord)
    sound_on_button = pygame.image.load('sound_on.png')
    sound_on_button = pygame.transform.scale(sound_on_button,(WIDTH // 40, HEIGHT // 20))
    sound_on_button_coord = (WIDTH // 500, HEIGHT // 18)
    sound_on_button_rect = sound_on_button.get_rect(topleft = sound_on_button_coord)
    sound_off_button = pygame.image.load('sound_off.png')
    sound_off_button = pygame.transform.scale(sound_off_button,(WIDTH // 40, HEIGHT // 20))
    sound_off_button_coord = (WIDTH // 500, HEIGHT // 18)
    sound_off_button_rect = sound_off_button.get_rect(topleft = sound_off_button_coord)
    while in_menu:
        menu_option, selected,clickmouse= handle_menu_input(menu_option)
        draw_menu(menu_option)
        screen.blit(guide_button,guide_button_coord)
        screen.blit(logout_button,logout_button_coord)
        if sound.sound_enabled:   
            screen.blit(sound_on_button, sound_on_button_coord)
        else:
            screen.blit(sound_off_button, sound_off_button_coord)
        pygame.display.update()
        if selected : 
            break
        if clickmouse:
            # Thực hiện các hành động liên quan đến lựa chọn
            mouse_pos = pygame.mouse.get_pos()

            for i in range(soluongoption):
                option_rect = pygame.Rect(WIDTH / (1.3) - rendered_text.get_width() / 2, 2*HEIGHT/12 + HEIGHT/(8.3) * i, rendered_text.get_width(), rendered_text.get_height())
                if option_rect.collidepoint(mouse_pos) :
                    in_menu = False
            if guide_button_rect.collidepoint(mouse_pos):
                in_menu = False
                menu_option = 6
            if logout_button_rect.collidepoint(mouse_pos):
                in_menu = False
                menu_option = 7
            if sound_on_button_rect.collidepoint(mouse_pos) and not sound.sound_enabled:
                in_menu = False
                menu_option = 8
            if sound_off_button_rect.collidepoint(mouse_pos) and sound.sound_enabled:
                in_menu = False
                menu_option = 9
            
            
                


    if menu_option == 0:
        mixer.music.stop()
        inMenu = False
       
        if sound.sound_enabled:
            transition_sound.play()
            sleep(1)
            mixer.music.load('Background.ogg')
            mixer.music.play(-1)       
        maze_game_loader = MazeGameLoader()
        #maze_game_loader.run()
        main()
    elif menu_option == 1:
        intro_transition()  
        xulymenu_settings()
        xulymenu()

    elif menu_option == 2:
        intro_transition()  
        Load_Game_Display(screen,load_filegame())
        xulymenu()
    elif menu_option == 3:
        intro_transition()  
        xuly_ranking()
        xulymenu()
    elif menu_option == 4 : 
        intro_transition()  
        about()
        xulymenu()
        pass
    elif menu_option== 5:
        pygame.quit()
        sys.exit()    
    elif menu_option == 6 : 
        intro_transition()  
        guide()   
        xulymenu()     
    elif menu_option == 7:
        login_forms.logged_in = False
        while True:
                if not login_forms.logged_in:
                    login_forms.login()
                if login_forms.logged_in:
                    xulymenu()
    elif menu_option == 8 or menu_option == 9:
        if menu_option == 8:
            if not sound.sound_enabled:
                sound.toggle_sound()
                xulymenu()
                
                
        
        elif menu_option == 9:
            if sound.sound_enabled:
                sound.toggle_sound()
          
                xulymenu()
               
                
       

        
        
            

def about():
    global WIDTH,HEIGHT
    global Back_outgame
    global screen
    global rendered_text
  
    about_background = pygame.image.load('about.png')
    about_background = pygame.transform.scale(about_background,(WIDTH,HEIGHT))
    sound_on_button = pygame.image.load('sound_on.png')
    sound_on_button = pygame.transform.scale(sound_on_button,(WIDTH // 40, HEIGHT // 20))
    sound_on_button_coord = (WIDTH // 500, HEIGHT // 18)
    sound_on_button_rect = sound_on_button.get_rect(topleft = sound_on_button_coord)
    sound_off_button = pygame.image.load('sound_off.png')
    sound_off_button = pygame.transform.scale(sound_off_button,(WIDTH // 40, HEIGHT // 20))
    sound_off_button_coord = (WIDTH // 500, HEIGHT // 18)
    sound_off_button_rect = sound_off_button.get_rect(topleft = sound_off_button_coord)
    screen.fill(Black)
    running = True
    while running :
        screen.fill(Black)
        screen.blit(about_background,(0,0))
        screen.blit(Back_outgame,(0,0))
        if sound.sound_enabled: 
            screen.blit(sound_on_button, sound_on_button_coord)
        else:
            screen.blit(sound_off_button, sound_off_button_coord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE: 
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    mouse_pos = pygame.mouse.get_pos()
                    backbutton = pygame.Rect(0,0,rendered_text.get_width(),rendered_text.get_height())
                    if backbutton.collidepoint(mouse_pos):
                        return
                if sound_on_button_rect.collidepoint(mouse_pos):
                    sound.toggle_sound()
                   
        pygame.display.update()
    return
def draw_menu_setting(current_option):
    global optionsettings
    global rendered_text_settings
   
    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h
    ImMenu = pygame.image.load('Menu/menu_setting.png')
    ImMenu = pygame.transform.scale(ImMenu, (screen_width, screen_height))
    global screen
    screen.fill(Black)
    screen.blit(ImMenu, (0, 0))
    title_font = pygame.font.Font('8-BIT WONDER.ttf', 60)
    option_font = pygame.font.Font('8-BIT WONDER.ttf', 28)
    for i, option in enumerate(optionsettings):
        if i == current_option:
            rendered_text_settings = option_font.render(option, True, Red)
        else:
            rendered_text_settings = option_font.render(option, True, Black)
        screen.blit(rendered_text_settings, (WIDTH / (1.1) - rendered_text.get_width() / 2, 2*HEIGHT/11 + HEIGHT/(7.8) * i))


def xulymenu_settings():
    global optionsettings
    global COLS
    global ROWS
    global ChosingStartendMode
    global Mode_Findpath
    global Game_mode
    global rendered_text_settings
    Dif_op = 0 
    Game_op = 0 
    Path_op = 0 
    Start_op = 0 
    menu_option = 0
    sound_option = 0
    in_menu = True                        
    difficulty =["20x20", "40x40", "100x100"]
    difficultyVa =[(20,20),(40,40),(100,100)]
    game_modes = ["Player", "Bot","Both"]
    game_modesVa =["Player", "Bot","Both"]
    path_modes = ["DFS", "BFS", "A*star","Dijkstra"]
    path_modesVa = [0,1,2,3]
    start_modes =["Manual","Random"]
    start_modesVa = [1,2]
    sound_modes = ["OnSound","OffSound"]
    while True:
        soluongoptionse = 6
        draw_menu_setting(menu_option)
        pygame.display.update()
        for event in pygame.event.get() : 
            if event.type == pygame.KEYDOWN :
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    menu_option = (menu_option- 1) % soluongoptionse
                elif event.key == pygame.K_DOWN:
                    menu_option = (menu_option + 1) % soluongoptionse
                elif event.key == pygame.K_RETURN and menu_option == 4:
                    sound.toggle_sound()
                elif event.key == pygame.K_RIGHT:
                    #Chọn độ khó
                    if menu_option == 0:
                        Dif_op = (Dif_op + 1)%3
                        optionsettings[menu_option] = difficulty[Dif_op]
                        COLS, ROWS = difficultyVa[Dif_op]
                    #Chọn chế độ chơi máy hay người
                    elif menu_option == 1:
                        Game_op  = (Game_op+1)%3
                        optionsettings[menu_option] = game_modes[Game_op]
                        Game_mode = game_modesVa[Game_op]
                    #Chọn thuật toán tìm kíếm
                    elif menu_option == 2:
                        Path_op = (Path_op+1)%4
                        optionsettings[menu_option] = path_modes[Path_op]
                        Mode_Findpath = path_modesVa[Path_op]
                    #Chọn Start end
                    elif menu_option == 3 : 
                        Start_op = (Start_op + 1)%2
                        optionsettings[menu_option] = start_modes[Start_op]
                        ChosingStartendMode = start_modesVa[Start_op]
                    elif menu_option == 4 :
                        sound_option =(sound_option -1)%2 
                        optionsettings[menu_option] = sound_modes[sound_option]
                        sound.toggle_sound()          
                    elif menu_option == 5 : 
                        return       
                elif event.key == pygame.K_LEFT:
                    # Chọn độ khó
                    if menu_option == 0:
                        Dif_op = (Dif_op - 1)%3
                        optionsettings[menu_option] = difficulty[Dif_op]
                        COLS, ROWS = difficultyVa[Dif_op]
                    #Chọn chế độ chơi máy hay người
                    elif menu_option == 1:
                        Game_op  = (Game_op-1)%3
                        optionsettings[menu_option] = game_modes[Game_op]
                        Game_mode = game_modesVa[Game_op]
                    #Chọn thuật toán tìm kíếm
                    elif menu_option == 2:
                        Path_op = (Path_op-1)%4
                        optionsettings[menu_option] = path_modes[Path_op]
                        Mode_Findpath = path_modesVa[Path_op]
                    #Chọn Start end
                    elif menu_option == 3 : 
                        Start_op = (Start_op -1)%2
                        optionsettings[menu_option] = start_modes[Start_op]
                        ChosingStartendMode = start_modesVa[Start_op] 
                    elif menu_option == 4 :
                        sound_option =(sound_option -1)%2 
                        optionsettings[menu_option] = sound_modes[sound_option]
                        sound.toggle_sound()          
                    elif menu_option == 5 : 
                        return       
                elif event.key == pygame.K_ESCAPE :   
                    xulymenu()
            elif event.type == pygame.MOUSEMOTION:  # Detect mouse movement
                mouse_pos = pygame.mouse.get_pos()
                for i in range(soluongoption):
                    option_rect = pygame.Rect( WIDTH / (1.09) - rendered_text.get_width() / 2, 2*HEIGHT/11 + HEIGHT/(7.8) * i, rendered_text.get_width(), rendered_text.get_height())
                    if option_rect.collidepoint(mouse_pos):
                        menu_option = i    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    mouse_pos = pygame.mouse.get_pos()
                    backbutton = pygame.Rect(0,0,rendered_text.get_width()+100,rendered_text.get_height()+100)
                    if backbutton.collidepoint(mouse_pos):
                        return
                    for i in range(soluongoption):
                        option_rect = pygame.Rect( WIDTH / (1.09) - rendered_text.get_width() / 2, 2*HEIGHT/11 + HEIGHT/(7.8) * i, rendered_text.get_width(), rendered_text.get_height())
                        if option_rect.collidepoint(mouse_pos) :
                            #Chọn độ khó
                            if menu_option == 0:
                                Dif_op = (Dif_op + 1)%3
                                optionsettings[menu_option] = difficulty[Dif_op]
                                COLS, ROWS = difficultyVa[Dif_op]
                            #Chọn chế độ chơi máy hay người
                            elif menu_option == 1:
                                Game_op  = (Game_op+1)%3
                                optionsettings[menu_option] = game_modes[Game_op]
                                Game_mode = game_modesVa[Game_op]
                            #Chọn thuật toán tìm kíếm
                            elif menu_option == 2:
                                Path_op = (Path_op+1)%4
                                optionsettings[menu_option] = path_modes[Path_op]
                                Mode_Findpath = path_modesVa[Path_op]
                            #Chọn Start end
                            elif menu_option == 3 : 
                                Start_op = (Start_op + 1)%2
                                optionsettings[menu_option] = start_modes[Start_op]
                                ChosingStartendMode = start_modesVa[Start_op]
                            elif menu_option == 4 :
                                sound_option =(sound_option +1)%2 
                                optionsettings[menu_option] = sound_modes[sound_option]
                                sound.toggle_sound()          
                            elif menu_option == 5 : 
                                return    
                            
# Hàm hiển thị hộp thoại xác nhận
def confirm_dialog(screen, file_name, file_names, screen_width, screen_height):
    global WIDTH,HEIGHT
    global surface
    pygame.draw.rect(surface, (128, 128, 128, 150), [0, 0, WIDTH, HEIGHT])
   
    pygame.display.update()
    confirm_dialog_box = pygame.image.load('confirm_box.png')
    dialog_rect = confirm_dialog_box.get_rect(center=(screen_width // 2, screen_height // 2))
    button_font = pygame.font.Font(None, 25)
    Load_text = pygame.image.load('confirm_yes.png')
    Load_text = pygame.transform.scale(Load_text,(WIDTH//8,HEIGHT//8))
    Load_rect = Load_text.get_rect(center =((dialog_rect.centerx , dialog_rect.centery + 80)))
    remove_text = pygame.image.load('confirm_no.png')
    remove_text = pygame.transform.scale(remove_text,(WIDTH//8,HEIGHT//8))
    remove_rect = remove_text.get_rect(center=(dialog_rect.centerx + WIDTH//10, dialog_rect.centery + 75))
    surface.blit(confirm_dialog_box, dialog_rect)
    surface.blit(Load_text, Load_rect)
    surface.blit(remove_text, remove_rect)
    screen.blit(surface,(0,0))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if remove_rect.collidepoint(x, y):
                    # Xóa file
                    remove_file(file_name)
                    remove_file_in_database(file_name)
                    print(file_name)
                    if file_name in file_names:
                        file_names.remove(file_name)
                    draw_load_screen(screen,file_names,None)
                elif Load_rect.collidepoint(x, y):
                    continue_game(file_name)
                else: 
                    return
            
            
def Load_Game_Display(screen,file_names):
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
    
    if (len(file_names)!=0):
        y_spacing = (HEIGHT - len(file_names) / num_mazes_per_row * (maze_HEIGHT_mini_maze + MARGIN)) / 2 
    
    # Lấy danh sách các file maze đã lưu
    file_names = load_filegame()
    selected_maze_index = None  # Biến lưu chỉ số của maze hiện tại được chọn
    sound_on_button = pygame.image.load('sound_on.png')
    sound_on_button = pygame.transform.scale(sound_on_button,(WIDTH // 40, HEIGHT // 20))
    sound_on_button_coord = (WIDTH // 500, HEIGHT // 18)
    sound_on_button_rect = sound_on_button.get_rect(topleft = sound_on_button_coord) 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE: 
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    mouse_pos = pygame.mouse.get_pos()
                    backbutton = pygame.Rect(0,0,rendered_text.get_width(),rendered_text.get_height())
                    if backbutton.collidepoint(mouse_pos):
                        return
                    elif sound_on_button_rect.collidepoint(mouse_pos):
                        sound.toggle_sound()

                # Xử lý sự kiện khi người chơi nhấn chuột
                for i, file_name in enumerate(file_names):
                    mouse_pos = pygame.mouse.get_pos()
                    x= x_spacing + (i % num_mazes_per_row) * (maze_WIDTH_mini_maze + MARGIN)
                    y = y_spacing + (i// num_mazes_per_row) * (maze_HEIGHT_mini_maze + MARGIN)
                    if mouse_pos != None:
                        maze_rect = pygame.Rect(x, y, maze_WIDTH_mini_maze, maze_HEIGHT_mini_maze)  # Cập nhật maze_rect ở đây
                        if maze_rect.collidepoint(mouse_pos):
                            confirm_dialog(screen,file_name, file_names, WIDTH,HEIGHT)
                        #selected_maze_index = i  # Lưu chỉ số của maze được chọn
        # Vẽ giao diện load game
        draw_load_screen(screen, file_names, selected_maze_index)

    pygame.quit()
if __name__ == "__main__": 
    #xulymenu()  
    while True:
        if not login_forms.logged_in:
            login_forms.login()
        if login_forms.logged_in:
            xulymenu()
            
    
