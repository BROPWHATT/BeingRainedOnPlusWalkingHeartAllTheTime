import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heart Walking in the Rain")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Heart image
heart_img = pygame.image.load("heart.png")
heart_rect = heart_img.get_rect()
heart_rect.center = (WIDTH // 2, HEIGHT // 2)

# Rain variables
rain_size = 0
rain_speed = 0
rain_pos = []
MAX_RAIN_SIZE = 100

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                rain_size += 5
                if rain_size > MAX_RAIN_SIZE:
                    rain_size = MAX_RAIN_SIZE
                rain_speed = rain_size / 20

    # Update rain
    rain_pos.append([pygame.mouse.get_pos()[0], 0])
    for drop in rain_pos[:]:
        drop[1] += rain_speed
        if drop[1] > HEIGHT:
            rain_pos.remove(drop)

    # Draw rain
    for drop in rain_pos:
        pygame.draw.line(screen, BLUE, drop, (drop[0], drop[1] + rain_size), 2)

    # Draw heart
    screen.blit(heart_img, heart_rect)

    # Check if heart stops to cry
    if rain_size > 80:
        crying_text = pygame.font.SysFont(None, 50).render("😢", True, RED)
        screen.blit(crying_text, (heart_rect.centerx - 20, heart_rect.centery - 100))

    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
