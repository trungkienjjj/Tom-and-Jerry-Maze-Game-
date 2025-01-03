from class_file import*
from global_variable import*
from sound import*
pygame.init()
pygame.display.init()
soluongoption = 6

rendered_text = option_font.render("Start Game", True, Yellow)
def draw_menu(current_option):
    global option_font
    global soluongoption
    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h
    ImMenu = pygame.image.load('Menu\menu.png')
    ImMenu = pygame.transform.scale(ImMenu, (screen_width, screen_height))
    global screen
    screen.fill(Black)
    screen.blit(ImMenu, (0, 0))
    title_font = pygame.font.Font('8-BIT WONDER.ttf', 60)
    
    options = ["Start Game","Settings","Load Game","Ranking","About", "Exit"]
    for i, option in enumerate(options):
        if i == current_option:
            rendered_text = option_font.render(option, True, Red)
        else:
            rendered_text = option_font.render(option, True, Black)
        screen.blit(rendered_text, (WIDTH / (1.3) - rendered_text.get_width() / 2, 2*HEIGHT/12 + HEIGHT/(8.3) * i))
    
def handle_menu_input(current_option):
    global soluongoption
    mouse_clicked = False
    key_pressed = False
    pygame.display.init()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_option = (current_option - 1) % soluongoption
            elif event.key == pygame.K_DOWN:
                current_option = (current_option + 1) % soluongoption
            elif event.key == pygame.K_RETURN:
                key_pressed = True
        elif event.type == pygame.MOUSEMOTION:  # Detect mouse movement
            mouse_pos = pygame.mouse.get_pos()
            for i in range(soluongoption):
                option_rect = pygame.Rect(WIDTH / (1.3) - rendered_text.get_width() / 2, 2*HEIGHT/12 + HEIGHT/(8.3) * i, rendered_text.get_width(), rendered_text.get_height())
                if option_rect.collidepoint(mouse_pos):
                    current_option = i
                    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button clicked
                mouse_clicked = True

    return current_option, key_pressed, mouse_clicked
