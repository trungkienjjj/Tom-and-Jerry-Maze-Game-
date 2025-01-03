from numbers import Number
from re import S
from time import sleep
from turtle import position
import pygame
import random
import winsound 
import math
from pygame import font, mixer
import sys
import time
import threading
import os
from queue import PriorityQueue
from random import choice
from pygame.locals import *
from global_variable import *

import json
import csv
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)
Cyan = (0, 255, 255)
Magenta = (255, 0, 255)
Orange = (255, 165, 0)
Purple = (128, 0, 128)
Pink = (255, 192, 203)
Brown = (165, 42, 42)
Teal = (0, 128, 128)
Navy = (0, 0, 128)
Olive = (128, 128, 0)
Lime = (0, 255, 0)
Maroon = (128, 0, 0)
Silver = (192, 192, 192)
Gold = (255, 215, 0)
pygame.display.init()
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h

class MazeDrawer:
    global sc
    global CELLSIZE
    global DELTA_X
    global DELTA_Y
    global COLS
    def __init__(self, cols, rows, cells, interactive):
        TILE = 100
        if cols != 100 : 
          TILE =  Bottom_right_x//cols
        self.tilesheet = pygame.Surface((TILE, TILE*4))
        self.cols= cols
        self.rows = rows
        self.tile = TILE
        self.sc = sc
        self.cells = cells
        self.cell_images = []
        for y in range(4):
            for x in range(4):
                rect = (128 * x, 128 * y, CELLSIZE, CELLSIZE)
                image = pygame.image.load("MazeTileset.png").convert_alpha().subsurface(rect)
                image = pygame.transform.scale(image, (self.tile, self.tile))
                self.cell_images.append(image)
        self.wizard_image = pygame.Surface((self.tile, self.tile))
        self.wizard_image.fill((255, 255, 0))  # Yellow
        # draw the outside walls around the maze
        #self.draw_background()
        # center the maze
        #self.maze_offset_x = (WIDTH - Daisize * TILE) // 2
        #self.maze_offset_y = (HEIGHT - RongSize * TILE) // 2
        self.maze_offset_x = DELTA_X
        self.maze_offset_y = DELTA_Y
        self.visited_cells = []
        self.highlight_surface = pygame.Surface((self.tile, self.tile))
        self.highlight_surface.set_alpha(50)
        self.highlight_surface.fill((255, 255, 0))  # Yellow
        self.darken_surface = pygame.Surface((self.tile, self.tile))
        self.darken_surface.set_alpha(100)
        self.darken_surface.fill((0, 0, 0))  # Black
        self.interactive = interactive
    def Update_TILE(self,tile):
        self.maze_offset_x = DELTA_X
        self.maze_offset_y = DELTA_Y
        self.tile= tile
        self.tilesheet = pygame.Surface((tile, tile*4))
        self.cell_images =[]
        for y in range(4):
            for x in range(4):
                rect = (128 * x, 128 * y, CELLSIZE, CELLSIZE)
                image = pygame.image.load("MazeTileset.png").convert_alpha().subsurface(rect)
                image = pygame.transform.scale(image, (self.tile, self.tile))
                self.cell_images.append(image)
    def draw(self, select_cell=None, visit=True):
        global DELTA_X
        global DELTA_Y
        self.maze_offset_x = DELTA_X
        self.maze_offset_y = DELTA_Y
        self.draw_cells(select_cell, visit)
    def draw_cells(self, select_cell=None, visit=True):
        for index, cell in enumerate(self.cells):
            row_index = index // self.cols
            col_index = index % self.rows
            hasWallTop = cell.walls['top']
            hasWallRight = cell.walls['right']
            hasWallBottom = cell.walls['bottom']
            hasWallLeft = cell.walls['left']

            x = col_index * self.tile
            y = row_index * self.tile

            cell_index = 0
            if hasWallRight:
                cell_index += 1
            if hasWallLeft:
                cell_index += 2
            if hasWallBottom:
                cell_index += 4
            if hasWallTop:
                cell_index += 8
            self.sc.blit(self.cell_images[cell_index], (x + self.maze_offset_x, y + self.maze_offset_y))

            if cell == select_cell:
                if visit:
                    self.visited_cells.append(cell)
                #self.sc.blit(self.highlight_surface, (x + self.maze_offset_x, y + self.maze_offset_y))
                self.sc.blit(self.wizard_image, (x + self.maze_offset_x + self.tile// 2, y + self.maze_offset_y + self.tile// 2))

            #if cell not in self.visited_cells and self.interactive:
             #   self.sc.blit(self.darken_surface, (x + self.maze_offset_x, y + self.maze_offset_y))


path_image1 = pygame.image.load("path2.png")
path_image = pygame.image.load("path1.png") 
class Cell:
    global Bottom_right_x
    global cols
    global rows
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.links = {}
        self.visited = False
        self.passed = False
        self.path = False
        self.seen = False
        self.thickness = 1
        #self.image = pygame.image.load("cell_image.png")  # Load ảnh từ tệp cell_image.png
    def draw_mini_map(self, screen, TILE, maze_x, maze_y,color):
        x, y = maze_x + self.x * TILE, maze_y + self.y * TILE
        # Vẽ các bức tường bằng cách vẽ các hình chữ nhật
        if self.walls['top']:
            pygame.draw.rect(screen, color, pygame.Rect(x, y, TILE, self.thickness))
        if self.walls['right']:
            pygame.draw.rect(screen, color, pygame.Rect(x + TILE - self.thickness, y, self.thickness, TILE))
        if self.walls['bottom']:
            pygame.draw.rect(screen, color, pygame.Rect(x, y + TILE - self.thickness, TILE, self.thickness))
        if self.walls['left']:
            pygame.draw.rect(screen, color, pygame.Rect(x, y, self.thickness, TILE)) 
        if self.path:
            path_rect = pygame.Rect(x, y,TILE*1-TILE//4, TILE*1-TILE//4)
            pygame.draw.rect(screen, pygame.Color('green'), path_rect)
        if self.seen:
            seen_rect = pygame.Rect(x, y,TILE*1-TILE//4, TILE*1-TILE//4)
            pygame.draw.rect(screen, pygame.Color('red'), seen_rect)
    def draw(self, sc, TILE):
        global path_image
        global path_image1
        a, b = self.x * TILE + DELTA_X, self.y * TILE + DELTA_Y
        if self.path:
            path_image = pygame.transform.scale(path_image,(TILE-TILE/3,TILE-TILE/3))
            sc.blit(path_image,(a+TILE/10,b+TILE/10))
        if self.seen:
            path_image1 = pygame.transform.scale(path_image,(TILE-TILE/3,TILE-TILE/3))
            sc.blit(path_image1,(a+TILE/5,b+TILE/5))

    def check_cell(self, x, y, cols, rows):
        find_index = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return self.grid_cells[find_index(x, y)]

    def check_neighbors(self, grid_cells, cols, rows):
        self.grid_cells = grid_cells
        neighbors = []
        top = self.check_cell(self.x, self.y - 1, cols, rows)
        right = self.check_cell(self.x + 1, self.y, cols, rows)
        bottom = self.check_cell(self.x, self.y + 1, cols, rows)
        left = self.check_cell(self.x - 1, self.y, cols, rows)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False

    def check_neighbors_pass(self, grid_cells, cols, rows):
        self.grid_cells = grid_cells
        neighbors = []
        top = self.check_cell(self.x, self.y - 1, cols, rows)
        right = self.check_cell(self.x + 1, self.y, cols, rows)
        bottom = self.check_cell(self.x, self.y + 1, cols, rows)
        left = self.check_cell(self.x - 1, self.y, cols, rows)
        if top and not self.walls['top']:
            neighbors.append(top)
        if right and not self.walls['right']:
            neighbors.append(right)
        if bottom and not self.walls['bottom']:
            neighbors.append(bottom)
        if left and not self.walls['left']:
            neighbors.append(left)
        return neighbors
    


class PlayerAnimation:
    def __init__(self, animation_frames, sprite_sheet_path, cols, rows, cell_size, frame_rate=60):
        self.sprite_sheet = pygame.image.load(sprite_sheet_path)
        self.cols = cols
        self.rows = rows
        self.cell_size = cell_size
        self.frame_width = self.sprite_sheet.get_width() // cols
        self.frame_height = self.sprite_sheet.get_height() // rows
        self.frame_count = cols * rows
        self.current_animation = list(animation_frames.keys())[0]  # Default direction
        self.current_frame = 0
        self.frame_rate = frame_rate  # Desired frame rate in frames per second
        # Determine frames corresponding to each direction
        self.animation_frames = animation_frames
        self.frame_duration =2*(1000 // frame_rate)  # Duration of each frame in milliseconds

        # Variables to track time for frame updates
        self.last_frame_time = pygame.time.get_ticks()

    def get_current_frame(self):
        animation_index = self.animation_frames[self.current_animation][self.current_frame]
        col = animation_index % self.cols
        row = animation_index // self.cols
        x = col * self.frame_width
        y = row * self.frame_height
        x = min(max(0, x), self.sprite_sheet.get_width() - self.frame_width)
        y = min(max(0, y), self.sprite_sheet.get_height() - self.frame_height)
        frame = self.sprite_sheet.subsurface(pygame.Rect(x, y, self.frame_width, self.frame_height))
        return pygame.transform.scale(frame, (self.cell_size, self.cell_size))

    def update(self):
        # Check if it's time to update the frame
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time >= self.frame_duration:
            # Update frame
            self.current_frame = (self.current_frame + 1) % self.cols
            self.last_frame_time = current_time

    def set_direction(self, direction):
        # Set current animation direction
        self.current_animation = direction

class Mouse:
    def __init__(self,x,y,sprite_sheet_path,cell_size):
        self.x = x
        self.y = y
        self.sprite_sheet_path = sprite_sheet_path
        self.cell_size = cell_size
        self.direction = "None"
        tmpBB = {"None":[i for i in range(5)]}
        tmp_die = {"Die":[i for i in range(8) ]}
        self.animation = PlayerAnimation(tmpBB,"Jerry_animationBB.png",5,1,cell_size,3)
        self.animation_die = PlayerAnimation(tmp_die,"mouse_die.png",8,1,cell_size,3)
    def move(self, direction, grid_cells, Daisize, rows):
        self.direction = direction
        self.animation.set_direction(direction)
        self.animation.set_direction(direction)
    def draw(self, screen, TILE):
        # Draw current frame on screen
        self.animation.set_direction(self.direction)
        if self.direction == "None":
            current_frame = self.animation.get_current_frame()
            screen.blit(current_frame, (self.x * TILE + DELTA_X, self.y * TILE + DELTA_Y))
            self.animation.update()
        elif self.direction =="Die":
            current_frame = self.animation_die.get_current_frame()
            screen.blit(current_frame, (self.x * TILE + DELTA_X, self.y * TILE + DELTA_Y))
            self.animation.update()
class Start :
    def __init__(self,x,y,sprite_sheet_path,cell_size):
        self.x = x
        self.y = y
        self.sprite_sheet_path = sprite_sheet_path
        self.cell_size = cell_size
        self.direction = "None"
        tmpBB = {"None":[i for i in range(6)]}
        self.animation = PlayerAnimation(tmpBB,"Start_animation.png",6,1,cell_size,10)
    def draw(self, screen, TILE):
        # Draw current frame on screen
        self.animation.set_direction(self.direction)
        if self.direction == "None":
            current_frame = self.animation.get_current_frame()
            screen.blit(current_frame, (self.x * TILE + DELTA_X, self.y * TILE + DELTA_Y))
            self.animation.update()     
class FireWork:
    def __init__(self, x, y, fire_work_size):
        self.x = x
        self.y = y
        self.direction = "None"

        fire_work = {"1": [i for i in range(6)],
                     "2": [i + 6 for i in range(6)],
                     "3": [i + 2 * 6 for i in range(6)],
                     "4": [i + 3 * 6 for i in range(6)],
                     "5": [i + 4 * 6 for i in range(6)]}
        self.animation = PlayerAnimation(fire_work, "Firework.png", 6, 5, fire_work_size, 200)

    def move(self, direction):
        self.direction = direction
        self.animation.set_direction(direction)

    def draw(self, screen, direction):
        self.move(direction)
        # Draw current frame on screen
        current_frame = self.animation.get_current_frame()
        screen.blit(current_frame, (self.x, self.y))
        self.animation.update()

class FireWorks:
    def __init__(self, fire_work_size):
        self.fire_work_size = fire_work_size
        self.fireworks = [
            FireWork(0, 0, self.fire_work_size),
            FireWork(WIDTH - self.fire_work_size, 0, self.fire_work_size),
            FireWork(0, HEIGHT - self.fire_work_size, self.fire_work_size),
            FireWork(WIDTH- self.fire_work_size, HEIGHT-self.fire_work_size, self.fire_work_size)
        ]

    def draw(self,direction):
        cnt = 0 
        for firework in self.fireworks:
            firework.draw(screen, direction)
            cnt+=1
            if cnt%100 == 0 : 
             pygame.display.update()



        
class Player: 

    def __init__(self, x, y, sprite_sheet_path, cols, rows, cell_size):
        self.x = x
        self.y = y
        self.sprite_sheet_path = sprite_sheet_path
        self.cell_size = cell_size
        self.direction = "None"  # Default direction
        self.moved = False  # Track if player moved
        self.grid_cells = None
        self.cols = cols 
        self.rows = rows
        tmp = {
            "left": [i for i in range(cols)],
            "right": [i + cols for i in range(cols)],
            "down": [i + 2 * cols for i in range(cols)],
            "up": [i + 3 * cols for i in range(cols)]
        }
        tmp2 = {
            "None": [i for i in range(5)]
        }
        tmp3 = {
            "hidden":[i for i in range(3)]
        }
        tmp4 = { 
             "smash":[i for i in range(5)]   
                }
        tmp5 = {
            "laugh":[i for i in range(2)]
        }
        
        self.animation = PlayerAnimation(tmp, self.sprite_sheet_path, cols, rows, cell_size, 10)
        self.animation2 = PlayerAnimation(tmp2, "Tom_animation2.png", cols + 1, rows - 3, cell_size,1)
        self.animationhidden = PlayerAnimation(tmp3,"hidden.png",3,1,cell_size,10)
        self.animationsmash = PlayerAnimation(tmp4,"tom_smash_new.png",5,1,cell_size,10)
        self.animationlaugh = PlayerAnimation(tmp5,"tom_laugh.png",2,1,cell_size,10)
    def updatecamera(self,start):
        global DELTA_X
        global DELTA_Y
        global WIDTH
        global HEIGHT
        x,y = start.x*100-(WIDTH-100*100)/2, start.y*1000-(HEIGHT-100*100)/2
        print(start.x)
        print(start.y)
        dentax = 50*100 - start.x*100
        dentay = 50*100 - start.y*100 
        DELTA_X = (WIDTH-100*100)/2 +dentax
        DELTA_Y = (HEIGHT-100*100)/2 +dentay
        #DELTA_X =(WIDTH  - start.x *100+WIDTH//8)/2
        #DELTA_Y =(HEIGHT - start.y*100+HEIGHT//5)/2
    def returncamera(self):
        global DELTA_X
        global DELTA_Y
        DELTA_X = WIDTH//8   # dời ngang mê cung 
        DELTA_Y = HEIGHT//5  # dời dọc mê cung xuống 
    def move(self, direction, grid_cells, cols, rows):
        global DELTA_Y
        global DELTA_X
        self.grid_cells = grid_cells
        # Move logic
        if direction == 'up' and self.y > 0:
            if not grid_cells[self.x + (self.y - 1) * cols].walls['bottom']:
                pygame.time.delay(10)
                self.y -= 1
                if (cols!= 100):
                    pass
                else:
                    DELTA_Y +=100 
                self.direction = "up"
                self.animation.set_direction(self.direction)
                self.moved = True
        elif direction == 'down' and self.y < rows - 1:
            if not grid_cells[self.x + (self.y + 1) * cols].walls['top']:
                pygame.time.delay(10)
                self.y += 1
                if (cols!= 100):
                    pass
                else:
                    DELTA_Y -=100 
                self.direction = "down"
                self.animation.set_direction(self.direction)
                self.moved = True
        elif direction == 'left' and self.x > 0:
            if not grid_cells[self.x - 1 + self.y * cols].walls['right']:
                pygame.time.delay(10)
                self.x -= 1
                if (cols!= 100):
                    pass
                else:
                    DELTA_X +=100 
                self.direction = "left"
                self.animation.set_direction(self.direction)
                self.moved = True
        elif direction == 'right' and self.x < cols - 1:
            if not grid_cells[self.x + 1 + self.y * cols].walls['left']:
                pygame.time.delay(10)
                self.x += 1
                if (cols!= 100):
                    pass
                else:
                    DELTA_X -=100 
                self.direction = "right"
                self.animation.set_direction(self.direction)
                self.moved = True
        elif direction == "smash" :
            pygame.time.delay(10)
            self.direction = "smash"
            self.animation.set_direction(self.direction)
            self.animationsmash.set_direction(self.direction)
            self.moved = False
        elif direction == "laugh":
            pygame.time.delay(10)
            self.direction = "laugh"
            self.animationlaugh.set_direction(self.direction)
            self.animation.set_direction(self.animation)
            self.animationsmash.set_direction(self.animation)
            self.moved = False
            if  self.y > 0:
                if not grid_cells[self.x + (self.y - 1) * cols].walls['bottom']:
                    pygame.time.delay(10)
                    self.y -= 1
            elif  self.y < rows - 1:
                if not grid_cells[self.x + (self.y + 1) * cols].walls['top']:
                    pygame.time.delay(10)
                    self.y += 1
            elif  self.x > 0:
                if not grid_cells[self.x - 1 + self.y * cols].walls['right']:
                    pygame.time.delay(10)
                    self.x -= 1
            elif  self.x < cols - 1:
                if not grid_cells[self.x + 1 + self.y * cols].walls['left']:
                    pygame.time.delay(10)
                    self.x += 1
        else:
            self.direction = "None"
            self.animation.set_direction(self.direction)
            self.animation2.set_direction(self.direction)
            self.moved = False

    def update(self):
        if self.moved:
            self.animation.update()
            self.moved = False
    
    def draw(self, screen, TILE):
        # Draw current frame on screen
        if self.direction == "None":
            current_frame = self.animation2.get_current_frame()
            screen.blit(current_frame, (self.x * TILE + DELTA_X, self.y * TILE + DELTA_Y))
            self.animation2.update()
        elif self.direction =="smash":
            current_frame = self.animationhidden.get_current_frame()
            screen.blit(current_frame, (self.x * TILE + DELTA_X, self.y * TILE + DELTA_Y))
            self.animationhidden.update()
            pygame.time.delay(10)
            current_frame2 = self.animationsmash.get_current_frame()
            screen.blit(current_frame2,(self.x * TILE + DELTA_X, self.y * TILE + DELTA_Y))
            self.animationsmash.update()
        elif self.direction == "laugh":
            current_frame =self.animationlaugh.get_current_frame()
            screen.blit(current_frame, (self.x * TILE + DELTA_X, self.y * TILE + DELTA_Y))
            self.animationlaugh.update()
        else:
            current_frame = self.animation.get_current_frame()
            screen.blit(current_frame, (self.x * TILE + DELTA_X, self.y * TILE + DELTA_Y))        
class MazeGameLoader:
    global WIDTH
    global HEIGHT
    def __init__(self, width=800, height=600):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.progress = 0
        self.bar_width, self.bar_height = 600, 30
        self.bar_x, self.bar_y = (self.WIDTH - self.bar_width) // 2, (self.HEIGHT - self.bar_height) // 2 + 50
        self.loading_tips = [
            "Tip 1: Don't forget to explore every corner of the maze!",
            "Tip 2: Some paths might seem blocked, but they could be shortcuts!",
            "Tip 3: Keep an eye out for hidden passages behind walls!",
            "Tip 4: If you're stuck, try retracing your steps to find a new route!",
            "Tip 5: Don't rush through the maze - take your time to solve it!"
        ]
        self.tip_timer = 0
        self.tip_delay = 2000
        self.current_tips = []
        self.angle = 0
        self.wave_amplitude = 5
        self.wave_frequency = 0.1
        pygame.init()
        screen_width = pygame.display.Info().current_w
        creen_height = pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Maze Game Loading")
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def run(self):
        running = True
        backgroundLoading = pygame.image.load('backgroundload.jpg')
        screen_width = pygame.display.Info().current_w
        screen_height = pygame.display.Info().current_h
        backgroundLoading = pygame.transform.scale(backgroundLoading, (screen_width, screen_height))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(Black)

            self.screen.blit(backgroundLoading,(0,0))
            self.draw_progress_bar()
            self.render_text()
            self.update_loading_tips()
            self.draw_wave_animation()
            pygame.display.flip()
            self.progress += 0.2
            if self.progress >= 100:
                running = False
            pygame.time.delay(10)

        

    def draw_progress_bar(self):
        # Draw outer border
        outer_border_rect = pygame.Rect(self.bar_x - 2, self.bar_y - 2, self.bar_width + 4, self.bar_height + 4)
        pygame.draw.rect(self.screen, (255, 255, 255), outer_border_rect, 2)
        
        progress_width = int(self.progress / 100 * self.bar_width)
        color_gradient = (min(255, int(255 * (100 - self.progress) / 100)),
                          min(255, int(255 * self.progress / 100)), 200)
        pygame.draw.rect(self.screen, color_gradient, (self.bar_x, self.bar_y, progress_width, self.bar_height))

    def render_text(self):
        percentage_text = self.font.render(f"{int(self.progress)}%", True, (Black))
        text_rect = percentage_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 50))
        self.screen.blit(percentage_text, text_rect)
        dynamic_text = self.font.render("Loading Maze Game...", True, Black)
        dynamic_text_rect = dynamic_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 - 50))
        self.screen.blit(dynamic_text, dynamic_text_rect)
        for i, tip in enumerate(self.current_tips):
            tip_text = self.font.render(tip, True, Black)
            tip_text_rect = tip_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 100 + i * 40))
            self.screen.blit(tip_text, tip_text_rect)

    def update_loading_tips(self):
        if pygame.time.get_ticks() - self.tip_timer > self.tip_delay:
            self.tip_timer = pygame.time.get_ticks()
            self.current_tips = self.loading_tips[:int(self.progress / 20) + 1]

    def draw_wave_animation(self):
        wave_offset = self.wave_amplitude * math.sin(self.angle)
        progress_width = int(self.progress / 100 * self.bar_width)
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (self.bar_x + progress_width - 5, self.bar_y - 5 + wave_offset, 5, self.bar_height + 10))
        self.angle += self.wave_frequency
# Define the TextProgress class
class TextProgress:
    def __init__(self, font, message, color, bgcolor):
        self.font = font
        self.message = message
        self.color = color
        self.bgcolor = bgcolor
        self.offcolor = [c^40 for c in color]
        self.notcolor = [c^0xFF for c in color]
        self.text = font.render(message, 0, (255, 0, 0), self.notcolor)
        self.text.set_colorkey(1)
        self.outline = self.textHollow(font, message, color)
        self.bar = pygame.Surface(self.text.get_size())
        self.bar.fill(self.offcolor)
        width, height = self.text.get_size()
        stripe = Rect(0, height/2, width, height/4)
        self.bar.fill(color, stripe)
        self.ratio = width / 100.0

    def textHollow(self, font, message, fontcolor):
        base = font.render(message, 0, fontcolor, self.notcolor)
        size = base.get_width() + 2, base.get_height() + 2
        img = pygame.Surface(size, 16)
        img.fill(self.notcolor)
        base.set_colorkey(0)
        img.blit(base, (0, 0))
        img.blit(base, (2, 0))
        img.blit(base, (0, 2))
        img.blit(base, (2, 2))
        base.set_colorkey(0)
        base.set_palette_at(1, self.notcolor)
        img.blit(base, (1, 1))
        img.set_colorkey(self.notcolor)
        return img

    def render(self, percent=50):
        surf = pygame.Surface(self.text.get_size())
        if percent < 100:
            surf.fill(self.bgcolor)
            surf.blit(self.bar, (0, 0), (0, 0, percent * self.ratio, 100))
        else:
            surf.fill(self.color)
        surf.blit(self.text, (0, 0))
        surf.blit(self.outline, (-1, -1))
        surf.set_colorkey(self.notcolor)
        return surf

# Function to draw the progress bar
def draw_progress_bar(screen, progress):
    # Create a TextProgress instance
    renderer = TextProgress(pygame.font.Font(None, 60), "EDIT BY DUY MINH", (255, 255, 255), (40, 40, 40))
    # Render the progress bar
    progress_bar = renderer.render(progress)
    # Draw the progress bar on the screen
    screen.blit(progress_bar, (0, 0))
    cnt = 0  # Khai báo biến cnt ở đầu chương trình



