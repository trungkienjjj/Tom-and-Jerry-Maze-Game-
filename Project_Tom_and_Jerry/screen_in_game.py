from global_variable import * 
from algorithms import * 
from class_file import * 
from maze_generator import *
import login_forms
from save_load_game import * 
from load_game_draw import *
def save_screen(screen):         
    game_clock.pause()
    file_name = ""
    msg = ""  
    msg_start_time = 0 
    paused = True
    while paused:
        mouse_pos = pygame.mouse.get_pos()  # Lấy vị trí chuột
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            with open('database.json', 'r') as f:
                data = json.load(f)
                for account in data:
                    if login_forms.User_name in account:
                        if len(account) > 6:
                            msg = 'You have reached the limit of file'     
                        else:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if save.collidepoint(mouse_pos):
                                    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RETURN}))
                                elif filename_rect.collidepoint(mouse_pos):
                                    continue
                                else:
                                    return None
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_BACKSPACE:
                                    file_name = file_name[:-1]
                                elif event.key == pygame.K_RETURN:
                                    if file_name.strip() == "":
                                        msg = "Please enter a valid file name"               
                                        
                                    elif file_name + TAIL in account:
                                        msg = "This name has existed"              
                                        
                                    else:
                                        msg = 'Save successfully'
                                        surface.blit(font.render(msg, True, (255, 0, 0)), (pause_x + 350, pause_y + 220))
                                        screen.blit(surface,(0,0))
                                        pygame.display.update() 
                                        pygame.time.delay(1000)
                                        game_clock.continue_()
                                        return file_name
                                elif event.key == pygame.K_ESCAPE:  # Quay lại màn hình tạm dừng
                                    return None
                                elif event.unicode != "":
                                    if len(file_name) < 10: 
                                        file_name += event.unicode
                            

      # Hiển thị màn hình chờ lưu
        pause_width = 900
        pause_height = 50
        pause_x = (WIDTH - pause_width) // 2
        pause_y = (HEIGHT - pause_height) // 2

        # Hiển thị màn hình tạm dừng
        pygame.draw.rect(surface, (128, 128, 128, 2), [0, 0, WIDTH, HEIGHT])
        filename_rect = pygame.draw.rect(screen, DarkGray, [pause_x + 100, pause_y, pause_width, pause_height], 0, 10)
        save = pygame.draw.rect(screen, White, [pause_x + 420, pause_y + 70, 280, 50], 0, 10)
        surface.blit(font.render('Save', True, Black), (pause_x + 520, pause_y + 80))

        # Thêm viền đen khi di chuột tới nút "Save"
        if save.collidepoint(mouse_pos):
            pygame.draw.rect(screen, Black, [pause_x + 420, pause_y + 70, 280, 50], 2, 10)

        screen.blit(surface, (0, 0))
        surface.blit(font.render('Enter file name ' + file_name, True, Black), (pause_x + 120, pause_y + 20))  # Nhập tên tệp
        
        if msg:  # Hiển thị thông báo nếu có
            surface.blit(font.render(msg, True, (255, 0, 0)), (pause_x + 300, pause_y + 220))
            screen.blit(surface, (0, 0))
            pygame.display.update()
            pygame.time.delay(1000)
            return
        screen.blit(surface, (0, 0))
        pygame.display.update()



def pause_screen(screen):
    global surface 
    # Tính toán vị trí để hiển thị màn hình pause ở trung tâm màn hình
    pause_width = 600
    pause_height = 50
    pause_x = (WIDTH - pause_width) // 2
    pause_y = (HEIGHT - pause_height) // 2
    # Hiển thị màn hình tạm dừng
    pygame.draw.rect(surface, (128, 128, 128, 2), [0, 0, WIDTH, HEIGHT])
    #pygame.draw.rect(surface, DarkGray, [200, 150, 600, 50], 0, 10)
    menu = pygame.draw.rect(screen, DarkGray, [pause_x+100, pause_y, pause_width, pause_height], 0, 10)
    reset = pygame.draw.rect(screen, White, [pause_x + 100, pause_y + 70, 280, 50], 0, 10)
    save = pygame.draw.rect(screen, White, [pause_x + 420, pause_y + 70, 280, 50], 0, 10)
    surface.blit(font.render('Back to Menu', True, Black), (pause_x + 265, pause_y + 20))
    surface.blit(font.render('Restart', True, Black), (pause_x + 175, pause_y + 80))
    surface.blit(font.render('Save', True, Black), (pause_x + 520, pause_y + 80))
    screen.blit(surface,(0,0))
    mouse_pos = pygame.mouse.get_pos()
    # Kiểm tra xem con chuột có nằm trong phạm vi của nút reset không
    if reset.collidepoint(mouse_pos):
        # Vẽ viền đen xung quanh nút reset
        pygame.draw.rect(screen, (0, 0, 0), reset, 3,10)
    # Kiểm tra xem con chuột có nằm trong phạm vi của nút save không
    elif save.collidepoint(mouse_pos):
        # Vẽ viền đen xung quanh nút save
        pygame.draw.rect(screen, (0, 0, 0), save, 3,10)
    elif menu.collidepoint(mouse_pos):
        pygame.draw.rect(screen,Black,menu,3,10)
    
    pygame.display.update()
    return menu,reset,save


def winning_screen(elapsed_time, steps):
    running = True
    winning_box_y = pygame.display.Info().current_h  # Đặt vị trí ban đầu của winning_bot dưới màn hình
    transition_speed = 100  # Tốc độ di chuyển của winning_bot
    background = pygame.image.load("winning_background.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    d_font = pygame.font.Font("SVN-Coder's Crux.otf", 80)
    directions = ["1", "2", "3", "4", "5"]
    current_direction_firework=0
    cnt = 0
    while running:
        cnt += 1
        print(cnt)
        screen_width = pygame.display.Info().current_w
        screen_height = pygame.display.Info().current_h
        restart_button = pygame.image.load('restart_button.png')
        restart_button = pygame.transform.scale(restart_button, (restart_button.get_width()//2, restart_button.get_height()//2))
        back_button = pygame.image.load('back_button.png')
        back_button = pygame.transform.scale(back_button, (back_button.get_width()//2, back_button.get_height()//2))
        surface = pygame.Surface([screen_width, screen_height], pygame.SRCALPHA)
        winning_box = pygame.image.load('winning_box.png')
        winning_box = pygame.transform.scale(winning_box, (winning_box.get_width()*2, winning_box.get_height()*2))
        
        # Sử dụng background
        screen.blit(background, (0, 0))
        
        # Đặt vị trí của winning_bot
        winning_box_x = (screen_width - winning_box.get_width()) // 2 
        restart_button_x = winning_box_x + winning_box.get_width() // 2 - restart_button.get_width() // 2 + 25*WIDTH//96
        restart_button_y = winning_box_y + winning_box.get_height() // 2 - restart_button.get_height() // 2 + 20*HEIGHT//72
        back_button_x = winning_box_x + winning_box.get_width() // 2 - back_button.get_width() // 2 - 25*WIDTH//256
        back_button_y = winning_box_y + winning_box.get_height() // 2 - back_button.get_height() // 2 + 83*HEIGHT//288

        restart_button_rect = restart_button.get_rect(center=(restart_button_x, restart_button_y))
        back_button_rect = back_button.get_rect(center=(back_button_x, back_button_y))

        # Vẽ winning_box và các nút lên màn hình
        screen.blit(winning_box, (winning_box_x, winning_box_y))
        screen.blit(restart_button, restart_button_rect)
        screen.blit(back_button, back_button_rect)
        
        # Vẽ văn bản lên winning_box
        steps_text = d_font.render(f"Number of steps: {steps}", True, (0, 0, 0))
        time_text = d_font.render(f"Time: {elapsed_time} s", True, (0, 0, 0))
        
        steps_text_rect = steps_text.get_rect(center=(winning_box_x + winning_box.get_width() // 2 + winning_box.get_width()//25, winning_box_y + 170*HEIGHT//432))
        time_text_rect = time_text.get_rect(center=(winning_box_x + winning_box.get_width() // 2 + winning_box.get_width() // 50, winning_box_y + 220*HEIGHT//432))
        
        screen.blit(steps_text, steps_text_rect)
        screen.blit(time_text, time_text_rect)
        test= FireWorks(500)
        test.draw(directions[current_direction_firework])
        current_direction_firework= (current_direction_firework + 1)%5
        # Di chuyển winning_bot từ dưới lên
        if winning_box_y > (screen_height - winning_box.get_height()) // 2:
            winning_box_y -= transition_speed
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if restart_button_rect.collidepoint(x, y):
                    return True
                elif back_button_rect.collidepoint(x, y):
                    return False

def Ask_Choose_Again(grid_cells, cols, rows, TILE, sc, drawer, background):
    global selected_option_choose_again
    global WIDTH
    global surface
    global HEIGHT
    running = True

    while running:
        screen_width = pygame.display.Info().current_w
        screen_height = pygame.display.Info().current_h
        surface = pygame.Surface([screen_width, screen_height], pygame.SRCALPHA)
        AskBot = pygame.image.load('Ask_box2.png')
        shadow_offset = 5
        shadow_color = (0, 0, 0, 100)
        shadow_position = (screen_width // 5 + shadow_offset + WIDTH // 9, screen_height // 4 + shadow_offset)
        pygame.draw.rect(surface, (128, 128, 128, 2), [0, 0, screen_width, screen_height])
        shadow_surface = AskBot.copy()
        shadow_surface.fill(shadow_color, special_flags=pygame.BLEND_RGBA_MULT)
        surface.blit(shadow_surface, shadow_position)
        surface.blit(AskBot, (WIDTH // 5 + WIDTH // 9, HEIGHT // 4))
        screen.blit(surface, (0, 0))
        pygame.display.update()

        option_font = pygame.font.Font("SVN-Coder's Crux.otf", 28)
        
        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        option_rects = []
        for i, option in enumerate(menu_options):
            text_color = White
            if i == selected_option_choose_again:
                text_color = Red
            
            text = option_font.render(option, True, text_color)
            text_rect = text.get_rect(center=(WIDTH // 2 + (i - 0.5) * 130 - 22, HEIGHT // 2 - HEIGHT // 20))
            screen.blit(text, text_rect)
            option_rects.append(text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_option_choose_again = (selected_option_choose_again - 1) % len(menu_options)
                elif event.key == pygame.K_RIGHT:
                    selected_option_choose_again = (selected_option_choose_again + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option_choose_again == 1:
                        intro_transition()
                        screen.blit(background, (0, 0))
                        drawer.draw()
                        [cell.draw(sc, TILE) for cell in grid_cells]
                        pygame.display.flip()
                        pygame.display.update()
                        clock.tick(60)
                        start, end = select_start_end_manually(grid_cells, cols, rows, TILE, sc)
                        print("Manual Position selected")
                        return start, end
                    elif selected_option_choose_again == 0:
                        intro_transition()
                        screen.blit(background, (0, 0))
                        drawer.draw()
                        [cell.draw(sc, TILE) for cell in grid_cells]
                        pygame.display.flip()
                        pygame.display.update()
                        clock.tick(60)
                        start, end = select_start_end(grid_cells, cols, rows)
                        print("Random Position selected")
                        return start, end
            elif event.type == pygame.MOUSEMOTION:
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(event.pos):
                        selected_option_choose_again = i
                        break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos
                    for i, rect in enumerate(option_rects):
                        if rect.collidepoint(mouse_pos):
                            selected_option_choose_again = i
                            if selected_option_choose_again == 1:
                                intro_transition()
                                screen.blit(background, (0, 0))
                                drawer.draw()
                                [cell.draw(sc, TILE) for cell in grid_cells]
                                pygame.display.flip()
                                pygame.display.update()
                                clock.tick(60)
                                start, end = select_start_end_manually(grid_cells, cols, rows, TILE, sc)
                                print("Manual Position selected")
                                return start, end
                            elif selected_option_choose_again == 0:
                                intro_transition()
                                screen.blit(background, (0, 0))
                                drawer.draw()
                                [cell.draw(sc, TILE) for cell in grid_cells]
                                pygame.display.flip()
                                pygame.display.update()
                                clock.tick(60)
                                start, end = select_start_end(grid_cells, cols, rows)
                                print("Random Position selected")
                                return start, end

        pygame.display.update()
def transition(transition_value):
    transition_surf = pygame.Surface((WIDTH, HEIGHT))
    radius = int((30 - abs(transition_value)) * 8)
    pygame.draw.circle(transition_surf, (255, 255, 255), (WIDTH//2, HEIGHT//2), radius)
    return transition_surf

def intro_transition():
    transition_value = 0
    transition_speed = 1 # Adjust this value to control the speed of the transition
    while transition_value < 30:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Update transition value
        transition_value += transition_speed
        # Draw the transition effect
        transition_surf = transition(transition_value)
        transition_surf.set_colorkey((255, 255, 255))  # Set the color key to black for transparency
        screen.blit(transition_surf, (0, 0))
        #pygame.time.delay()
        pygame.display.flip()
        clock.tick(120)

def game_over_time_up(steps):
    running = True
    gameOver_box_y = pygame.display.Info().current_h  # Đặt vị trí ban đầu của winning_bot dưới màn hình
    transition_speed = 80  # Tốc độ di chuyển của winning_bot
    background = pygame.image.load("game_over_bg.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    
    # Tạo phông chữ
    d_font = pygame.font.Font("SVN-Coder's Crux.otf", 80)
    
    while running:
        screen_width = pygame.display.Info().current_w
        screen_height = pygame.display.Info().current_h
        restart_button = pygame.image.load('restart_button.png')
        restart_button = pygame.transform.scale(restart_button, (restart_button.get_width()//2, restart_button.get_height()//2))
        back_button = pygame.image.load('back_button.png')
        back_button = pygame.transform.scale(back_button, (back_button.get_width()//2, back_button.get_height()//2))
        surface = pygame.Surface([screen_width, screen_height], pygame.SRCALPHA)
        gameOver_box = pygame.image.load('game_over_box.png')
        gameOver_box = pygame.transform.scale(gameOver_box, (gameOver_box.get_width()*2, gameOver_box.get_height()*2))


        
        # Sử dụng background
        screen.blit(background, (0, 0))
        
        # Đặt vị trí của winning_bot
        gameOver_box_x = (screen_width - gameOver_box.get_width()) // 2 
        restart_button_x = gameOver_box_x + gameOver_box.get_width() // 2 - restart_button.get_width() // 2 + 25*WIDTH//96
        restart_button_y = gameOver_box_y + gameOver_box.get_height() // 2 - restart_button.get_height() // 2 + 20*HEIGHT//72
        back_button_x = gameOver_box_x + gameOver_box.get_width() // 2 - back_button.get_width() // 2 - back_button.get_width() // 3  - 25*WIDTH//256
        back_button_y = gameOver_box_y + gameOver_box.get_height() // 2 - back_button.get_height() // 2 + 83*HEIGHT//288

        restart_button_rect = restart_button.get_rect(center=(restart_button_x, restart_button_y))
        back_button_rect = back_button.get_rect(center=(back_button_x, back_button_y))

        # Vẽ gameOver_box và các nút lên màn hình
        screen.blit(gameOver_box, (gameOver_box_x, gameOver_box_y))
        screen.blit(restart_button, restart_button_rect)
        screen.blit(back_button, back_button_rect)
        
        # Vẽ văn bản lên gameOver_box
        steps_text = d_font.render(f"Number of steps: {steps}", True, (0, 0, 0))
        time_text = d_font.render(f"Time Up!", True, (0, 0, 0))
        
        steps_text_rect = steps_text.get_rect(center=(gameOver_box_x + gameOver_box.get_width() // 2 + gameOver_box.get_width()//30, gameOver_box_y + 170*HEIGHT//432 + HEIGHT//50))
        time_text_rect = time_text.get_rect(center=(gameOver_box_x + gameOver_box.get_width() // 2 + gameOver_box.get_width()//70, gameOver_box_y + 220*HEIGHT//432 + HEIGHT//50))
        
        screen.blit(steps_text, steps_text_rect)
        screen.blit(time_text, time_text_rect)
        
        # Di chuyển winning_bot từ dưới lên
        if gameOver_box_y > (screen_height - gameOver_box.get_height()) // 2:
            gameOver_box_y -= transition_speed
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if restart_button_rect.collidepoint(x, y):
                    return True
                elif back_button_rect.collidepoint(x, y):
                    return False