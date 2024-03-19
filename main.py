import pygame
from pygame_widgets.slider import Slider
import pygame_widgets

import sys
import random
import asyncio

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heart Walking in the Rain")

# set up background
background = pygame.image.load("bg.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

key_ev = [0, 0, 0, 0]

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

MOVE_DELTA = 5

fonts = pygame.sysfont.get_fonts()
emoji_font = [font for font in fonts if "emoji" in font][0]

# title
title_font = pygame.font.SysFont("Microsoft YaHei", 25)
title_text = title_font.render("淋雨+一直走心", True, BLUE)

# Heart image
heart_pos = [WIDTH // 2, HEIGHT // 2]
heart_img = pygame.image.load("heart.png")
heart_img = pygame.transform.scale(heart_img, (80, 80))
heart_rect = heart_img.get_rect()
heart_rect.center = (WIDTH // 2, HEIGHT // 2)

# Rain variables
rain_size = 0
rain_speed = 0
rain_pos = []
MAX_RAIN_SIZE = 70
slider_rainsize = Slider(screen, 100, 50, 600, 10, min=5, max=MAX_RAIN_SIZE, step=1)

# Main game loop
async def main():
    running = True
    while running:
        screen.fill(WHITE)
        screen.blit(background, (0, 0))
        events = pygame.event.get()
        
        # Handle events
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    key_ev[0] = 1
                if event.key == pygame.K_s:
                    key_ev[1] = 1
                if event.key == pygame.K_a:
                    key_ev[2] = 1
                if event.key == pygame.K_d:
                    key_ev[3] = 1
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    key_ev[0] = 0
                if event.key == pygame.K_s:
                    key_ev[1] = 0
                if event.key == pygame.K_a:
                    key_ev[2] = 0
                if event.key == pygame.K_d:
                    key_ev[3] = 0

        # Update heart position
        if key_ev[0]:
            heart_rect.centery -= MOVE_DELTA
        if key_ev[1]:
            heart_rect.centery += MOVE_DELTA
        if key_ev[2]:
            heart_rect.centerx -= MOVE_DELTA
        if key_ev[3]:
            heart_rect.centerx += MOVE_DELTA
        
        rain_speed = 5 + slider_rainsize.getValue() / 10
        rain_size = slider_rainsize.getValue()

        # Update rain
        rain_pos.append([random.randint(0, WIDTH), 0])
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
        if rain_size > MAX_RAIN_SIZE * 0.7:
            crying_text = pygame.font.SysFont(emoji_font, 25).render("😢", True, RED)
            screen.blit(crying_text, (heart_rect.centerx - 17, heart_rect.centery-12))

        slider_rainsize.draw()
        screen.blit(title_text, (WIDTH // 2 - 75, 10))

        # Cap the frame rate
        pygame.time.Clock().tick(60)
        pygame.display.update()
        pygame_widgets.update(events)

        await asyncio.sleep(0.0)

    # Quit Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    asyncio.run(main())
