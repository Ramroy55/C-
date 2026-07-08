import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Use a window if possible, but handle environments without a display
try:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
except pygame.error:
    # This might happen in some restricted environments
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Car Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Car dimensions
car_width = 73
car_height = 144

# Load images or create placeholders
def load_image(file_name, width, height, color):
    if os.path.exists(file_name):
        try:
            img = pygame.image.load(file_name)
            return pygame.transform.scale(img, (width, height))
        except pygame.error:
            pass
    # Fallback to a colored rectangle
    surface = pygame.Surface((width, height))
    surface.fill(color)
    return surface

car_img = load_image('car.png', car_width, car_height, BLUE)
enemy_img = load_image('enemy_car.png', car_width, car_height, RED)

# Car initial position
car_x = (SCREEN_WIDTH - car_width) // 2
car_y = SCREEN_HEIGHT - car_height - 20

# Enemy car initial position
enemy_width = car_width
enemy_height = car_height
enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
enemy_y = -enemy_height

# Car speed
car_speed = 5

# Enemy car speed
enemy_speed = 7

clock = pygame.time.Clock()

def draw_car(x, y):
    screen.blit(car_img, (x, y))

def draw_enemy_car(x, y):
    screen.blit(enemy_img, (x, y))

def game_over():
    try:
        font = pygame.font.SysFont(None, 50)
        text = font.render("Game Over!", True, RED)
        screen.blit(text, (250, 250))
    except:
        print("Game Over!")
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Game Loop
running = True
try:
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= car_speed
        if keys[pygame.K_RIGHT] and car_x < SCREEN_WIDTH - car_width:
            car_x += car_speed

        enemy_y += enemy_speed
        if enemy_y > SCREEN_HEIGHT:
            enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
            enemy_y = -enemy_height

        if car_x < enemy_x + enemy_width and car_x + car_width > enemy_x and car_y < enemy_y + enemy_height and car_y + car_height > enemy_y:
            game_over()

        draw_car(car_x, car_y)
        draw_enemy_car(enemy_x, enemy_y)

        pygame.display.update()
        clock.tick(60)
except KeyboardInterrupt:
    pass

pygame.quit()
sys.exit()
