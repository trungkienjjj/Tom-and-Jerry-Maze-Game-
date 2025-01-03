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
from queue import PriorityQueue
from random import choice
from pygame.locals import *
from queue import Queue
from global_variable import *
from class_file import*

def DFS_findPath(grid_cells, start, end, cols, rows, visualize):
    stack = [start]
    trace = {start: -1}
    list_visualize = []
    while stack:
        vertex= stack.pop()
        if visualize: 
           list_visualize.append(vertex)
        if vertex == end:
            break  
        if vertex.passed == False:
            vertex.passed = True
            neighbors = vertex.check_neighbors_pass(grid_cells, cols, rows) #check the available directions (wall or not)
            for neighbor in neighbors:
                if not neighbor.passed:
                    stack.append(neighbor)
                    trace[neighbor] = vertex
    for i in range (len(grid_cells)):
        grid_cells[i].passed = False
    u = end
    path  = []
    path.append(u)
    u = trace[u]
    while u != -1:
        path.append(u)
        u = trace[u]
    if visualize:
        return [list_visualize, path[::-1]]
    return path[::-1]
def BFS_findPath(grid_cells, start, end, cols, rows, visualize):
    queue = Queue()
    queue.put(start)
    start.passed = True
    trace = {start: -1}
    visual = []
    while not queue.empty(): 
        vertex = queue.get()
        if visualize:
            visual.append(vertex)
        if vertex == end:
            break
        neighbors = vertex.check_neighbors_pass(grid_cells, cols, rows)
        for neighbor in neighbors:
            if not neighbor.passed:
                queue.put(neighbor)
                trace[neighbor] = vertex
                neighbor.passed = True
    for i in range(len(grid_cells)):
        grid_cells[i].passed = False
    u = end
    path = []
    path.append(u)
    u = trace[u]
    while u != -1:
        path.append(u)
        u = trace[u]
    if visualize:
        return [visual, path[::-1]]
    return path[::-1]


def dis_to_goal(cell1, cell2):
    x1,y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)


def AStar_findPath(grid_cells, start, end, cols, rows, visualize):
    cor_start = (start.x, start.y)
    cor_end = (end.x, end.y)
    g_score = {cell: float('inf') for cell in grid_cells}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in grid_cells}
    f_score[start] = dis_to_goal(cor_start, cor_end)
    visual = []
    
    trace = {start: -1}

    find_index = lambda x, y: x + y * cols
    res = PriorityQueue()
    res.put((dis_to_goal(cor_start, cor_end), dis_to_goal(cor_start, cor_end), (start.x, start.y)))
    while not res.empty():
        vertex_cor = res.get()[2]
        vertex = grid_cells[find_index(vertex_cor[0], vertex_cor[1])]
        if visualize: 
            visual.append(vertex)
        if vertex == end:
            break
        neighbors = vertex.check_neighbors_pass(grid_cells, cols, rows)
        for neighbor in neighbors:
            cor_neighbor = (neighbor.x, neighbor.y)
            temp_g_score = g_score[vertex] + 1
            temp_f_score = temp_g_score + dis_to_goal(cor_neighbor, cor_end)
            if temp_f_score < f_score[neighbor]:
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_f_score
                res.put((f_score[neighbor], dis_to_goal(cor_neighbor,cor_end), cor_neighbor))
                trace[neighbor] = vertex

    u = end
    path = []
    path.append(u)
    u = trace[u]
    while u != -1:
        path.append(u)
        u = trace[u]
    if visualize:
        return [visual, path[::-1]]
    return path[::-1]

def DFS_spread(grid_cells, start, cols, rows):
    stack = [start]
    path = []
    while stack:
        vertex = stack.pop()
        if not vertex.passed:
            path.append(vertex)
            vertex.passed = True
            neighbors = vertex.check_neighbors_pass(grid_cells, cols, rows)
            for neighbor in neighbors:
                if not neighbor.passed:
                    stack.append(neighbor)
    for i in range (len(grid_cells)):
        grid_cells[i].passed = False
    return path     


def Dijkstra_FindPath(grid_cells, start, end, cols, rows, visualize):
    pq = PriorityQueue()
    INF = 10**6
    dist = [INF] * (cols * rows)
    trace = [-1] * (cols * rows)
    visited = [False] * (cols * rows)

    start_index = start.x + start.y * cols
    end_index = end.x + end.y * cols
    dist[start_index] = 0
    visual = []
    pq.put((0, start_index))
   
    while not pq.empty():
        _, u = pq.get()    # tuple u là 1 chiều
        if visualize: 
            visual.append(grid_cells[u])
        if u == end_index:
            break
        visited[u] = True
        u_x, u_y = u % cols, u // cols
        neighbors = grid_cells[u_x + u_y * cols].check_neighbors_pass(grid_cells, cols, rows)
        for neighbor in neighbors:
            v_x, v_y = neighbor.x, neighbor.y
            v = v_x + v_y * cols            # tọa độ 1 chiều của neighbor
            weight = ((u_x - v_x)**2 + (u_y - v_y)**2)**0.5
            if not visited[v] and dist[v] > dist[u] + weight: 
                dist[v] = dist[u] + weight
                pq.put((dist[v], v))
                trace[v] = u
    path = []
    u = end_index 
    while u != -1:
        path.append(grid_cells[u % cols + (u // cols) * cols])
        u = trace[u]
    if visualize:
        return [visual, path[::-1]]
    return path[::-1]





def euclid_distance(cell1, cell2):
    return (cell1.x - cell2.x)**2 + (cell1.y - cell2.y)**2

def select_start_end(grid_cells, cols, rows):
    list_end = []
    while not list_end:
        random_start = random.choice(grid_cells)
        path = DFS_spread(grid_cells, random_start, cols, rows)
        rad = (cols**2 + rows**2)/ 4
        for vertex in path:
            if euclid_distance(vertex, random_start) >= rad:
                list_end.append(vertex)
    random_end = random.choice(list_end)
    # bắt đầu tính thời gian sau khi chọn vị trí start end
    game_clock.start()
    return (random_start, random_end)







def select_start_end_manually(grid_cells, cols, rows, TILE, sc):
    start_color = (0, 255, 0)  # Green
    end_color = (255, 0, 0)  # Red
    bright_color = (255, 255, 0)  # Yellow
    start_selected = False
    end_selected = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                col = (mouse_pos[0] - DELTA_X) // TILE
                row = (mouse_pos[1] - DELTA_Y)// TILE
                index = col + row * cols
                index = min(index, len(grid_cells) - 1)
                index = max(index, 0)
                cell = grid_cells[index]

                if not start_selected:
                    start_selected = True
                    start_cell = cell
                    start_real = Start(start_cell.x,start_cell.y,"Start_animation.png",TILE)
                    start_real.draw(sc,TILE)
                    clock.tick(60)
                    pygame.display.flip()
                    pygame.display.update()
                    pygame.draw.rect(sc, Black, (start_cell.x * TILE + 4 + DELTA_X, start_cell.y * TILE + 4 + DELTA_Y, TILE - 8, TILE - 8 ))
                elif not end_selected:
                    if cell != start_cell:
                        end_selected = True
                        end_cell = cell
                        mouse  = Mouse(end_cell.x,end_cell.y,"Jerry_animationBB.png",TILE)
                        mouse.draw(sc,TILE)
                        pygame.time.delay(400)
        pygame.display.update()
        if start_selected and end_selected:
            # bắt đầu tính thời gian sau khi chọn vị trí start end
            game_clock.start()
            return start_cell, end_cell
        


