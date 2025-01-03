import login_forms
from menu import * 
from global_variable import * 
import json
import pygame
import sys
pygame.display.init()
pygame.font.init()
FONT2 = pygame.font.Font('8-BIT WONDER.ttf', 32)
FONT = pygame.font.SysFont(None, 30)
def get_rank(elapsed_time, steps, size):
    index = 0
    if size == 20:
        size = 0
    elif size == 40:
        size = 1
    else:
        size = 2
    with open('ranking.json' , 'r') as f:
        rank = json.load(f)
        if login_forms.User_name in rank[size] and elapsed_time <= rank[size][login_forms.User_name][0]:
            rank[size][login_forms.User_name] = [elapsed_time, steps]
            rank[size] = dict(sorted(rank[size].items(), key=lambda x: x[1][0]))
        elif login_forms.User_name not in rank[size]:
            rank[size][login_forms.User_name] = [elapsed_time, steps]
            rank[size] = dict(sorted(rank[size].items(), key=lambda x: x[1][0]))

    with open('ranking.json', 'w') as out:
        json.dump(rank, out, indent = 2)

def load_ranking():
    with open('ranking.json', 'r') as f:
        rank = json.load(f)
        return (rank[0].copy(), rank[1].copy(), rank[2].copy())

def draw_ranking(screen, ranking):
    y_offset = HEIGHT//3
    for i, (username, data) in enumerate(ranking.items()):
        text_surface = FONT.render(f"{i+1}.  {username}:   {data[0]}s    {data[1]} steps", True,White)
        screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, y_offset))
        y_offset += 40

def xuly_ranking():
    global screen
    global Back_outgame
    levelsRanking = ["20x20","40x40","100x100"]
    soluongoptionRanking = 3
    current_option_ranking = 0
    clock = pygame.time.Clock()
    running = True
    ranking = load_ranking()
    learboard = pygame.image.load("Ranking2.jpg")    
    learboard = pygame.transform.scale(learboard, (WIDTH, HEIGHT)) 
    idx = 0
    while running:
        screen.fill(White)
        screen.blit(learboard,(0,0))
        screen.blit(Back_outgame,(0,0))
        draw_ranking(screen, ranking[current_option_ranking])   
        text_surface = FONT2.render(levelsRanking[current_option_ranking],True,Black)
        if(current_option_ranking == 2):
            idx=0 
        else:
            idx=10
            
        screen.blit(text_surface, (WIDTH//2-90+idx ,(5/6)*HEIGHT))           
        pygame.display.flip()
        pygame.display.update()
        for event in pygame.event.get() : 
            if event.type == pygame.KEYDOWN :
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_RIGHT:
                    current_option_ranking = (current_option_ranking + 1)% soluongoptionRanking
                elif event.key == pygame.K_LEFT : 
                    current_option_ranking = (current_option_ranking - 1 )% soluongoptionRanking
                elif event.key == pygame.K_ESCAPE :
                    running = False
                    print("return")
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    mouse_pos = pygame.mouse.get_pos()
                    backbutton = pygame.Rect(0,0,rendered_text.get_width()+100,rendered_text.get_height()+100)
                    if backbutton.collidepoint(mouse_pos):
                        return
                    else : 
                        current_option_ranking = (current_option_ranking + 1) % soluongoptionRanking
                        
                
        
