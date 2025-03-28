import pygame
import time
import random
import tkinter as tk
from tkinter import simpledialog

# Initialize pygame
pygame.init()

# Set display size
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 10
SNAKE_SPEED = 10  # Reduced speed for slower movement

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - DLS Mode")

# Clock to control game speed
clock = pygame.time.Clock()

# Font for displaying score and moves
font = pygame.font.SysFont("bahnschrift", 25)

# Get depth limit from user
root = tk.Tk()
root.withdraw()  # Hide the root window
MOVE_LIMIT = simpledialog.askinteger("Input", "Enter Depth Limit (Move Limit):", minvalue=1, maxvalue=200)
if MOVE_LIMIT is None:
    MOVE_LIMIT = 50  # Default value if user cancels

def display_status(score, moves):
    score_text = font.render("Score: " + str(score), True, WHITE)
    moves_text = font.render("Moves Left: " + str(moves), True, WHITE)
    screen.blit(score_text, [10, 10])
    screen.blit(moves_text, [10, 40])

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def dls_search(x, y, food_x, food_y, depth):
    if depth == 0:
        return None  # No valid path within move limit
    
    possible_moves = [(x + BLOCK_SIZE, y), (x - BLOCK_SIZE, y), (x, y + BLOCK_SIZE), (x, y - BLOCK_SIZE)]
    valid_moves = [move for move in possible_moves if 0 <= move[0] < WIDTH and 0 <= move[1] < HEIGHT]
    
    best_move = None
    min_distance = float("inf")
    
    for move in valid_moves:
        distance = abs(move[0] - food_x) + abs(move[1] - food_y)
        if distance < min_distance:
            min_distance = distance
            best_move = move
    
    return best_move

def game_loop():
    game_over = False
    game_close = False
    
    x = WIDTH // 2
    y = HEIGHT // 2
    moves_left = MOVE_LIMIT
    
    snake_list = []
    length_of_snake = 1

    food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    
    while not game_over:
        while game_close:
            screen.fill(BLACK)
            message = font.render("Game Over! Press Q-Quit or C-Play Again", True, RED)
            screen.blit(message, [WIDTH / 6, HEIGHT / 3])
            display_status(length_of_snake - 1, moves_left)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        
        if moves_left <= 0:
            game_close = True
        
        next_move = dls_search(x, y, food_x, food_y, moves_left)
        if next_move:
            x, y = next_move
        else:
            game_close = True
        
        screen.fill(BLUE)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True
        
        draw_snake(snake_list)
        display_status(length_of_snake - 1, moves_left)
        pygame.display.update()
        
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            length_of_snake += 1
            moves_left -= 5  # Reduce moves available after eating food
        
        moves_left -= 1
        clock.tick(SNAKE_SPEED)
    
    pygame.quit()
    quit()

# Run the game
game_loop()