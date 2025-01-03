import pygame
import sys

# Định nghĩa màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
screen_WIDTH = 902
screen_HEIGHT = 602
screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))
pygame.display.set_caption("Menu Example")

# Font cho menu
font = pygame.font.SysFont(None, 40)

# Danh sách các tùy chọn trong menu
menu_options = ["Random", "Manual"]
selected_option_choose_again = 0

def draw_menu():
    
    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h
    
    surface = pygame.Surface([screen_width, screen_height], pygame.SRCALPHA)
    screen.fill(RED)
    AskBot = pygame.image.load('Ask_box2.png')
    shadow_offset = 5  # Độ lệch cho bóng
    shadow_color = (0, 0, 0, 100)  # Màu của bóng, với alpha là 100 để làm cho bóng mờ
    shadow_position = (screen_width // 10 + shadow_offset, screen_height // 8 + shadow_offset)  # Vị trí của bóng
    screen.blit(surface, (0, 0))
    pygame.draw.rect(surface, (128, 128, 128, 2), [0, 0, screen_width, screen_height])
    
    # Vẽ bóng
    shadow_surface = AskBot.copy()
    shadow_surface.fill(shadow_color, special_flags=pygame.BLEND_RGBA_MULT)
    screen.blit(shadow_surface, shadow_position)
    
    screen.blit(AskBot, (screen_width // 10, screen_height // 8))
    
    title_font = pygame.font.Font('8-BIT WONDER.ttf', 20)
    option_font = pygame.font.Font('8-BIT WONDER.ttf', 12)

    for i, option in enumerate(menu_options):
        text = option_font.render(option, True, WHITE if i == selected_option_choose_again else RED)
        text_rect = text.get_rect(center=(screen_WIDTH // 2 + (i - 0.5) * 130 - 22, screen_HEIGHT // 2 - 5))
        screen.blit(text, text_rect)

def handle_events():
    global selected_option_choose_again
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
                if selected_option_choose_again == 0:
                    print("Random Position selected")
                    # Thực hiện random vị trí start và end
                elif selected_option_choose_again == 1:
                    print("Manual Position selected")
                    # Thực hiện chọn vị trí thủ công

def main():
    running = True
    while running:
        handle_events()
        draw_menu()
        pygame.display.update()
def Ask_Choose_Again():
    global selected_option_choose_again
    running = True
    while running:
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
                    if selected_option_choose_again == 0:
                        print("Random Position selected")
                        # Thực hiện random vị trí start và end
                    elif selected_option_choose_again == 1:
                        print("Manual Position selected")
                        # Thực hiện chọn vị trí thủ công
        
        screen_width = pygame.display.Info().current_w
        screen_height = pygame.display.Info().current_h
        
        surface = pygame.Surface([screen_width, screen_height], pygame.SRCALPHA)
        screen.fill(RED)
        AskBot = pygame.image.load('Ask_box2.png')
        shadow_offset = 5  # Độ lệch cho bóng
        shadow_color = (0, 0, 0, 100)  # Màu của bóng, với alpha là 100 để làm cho bóng mờ
        shadow_position = (screen_width // 10 + shadow_offset, screen_height // 8 + shadow_offset)  # Vị trí của bóng
        screen.blit(surface, (0, 0))
        pygame.draw.rect(surface, (128, 128, 128, 2), [0, 0, screen_width, screen_height])
        
        # Vẽ bóng
        shadow_surface = AskBot.copy()
        shadow_surface.fill(shadow_color, special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(shadow_surface, shadow_position)
        
        screen.blit(AskBot, (screen_width // 10, screen_height // 8))
        
        #title_font = pygame.font.Font('8-BIT WONDER.ttf', 20)
        option_font = pygame.font.Font('8-BIT WONDER.ttf', 12)

        for i, option in enumerate(menu_options):
            text = option_font.render(option, True, WHITE if i == selected_option_choose_again else RED)
            text_rect = text.get_rect(center=(screen_WIDTH // 2 + (i - 0.5) * 130 - 22, screen_HEIGHT // 2 - 5))
            screen.blit(text, text_rect)

        pygame.display.update()



