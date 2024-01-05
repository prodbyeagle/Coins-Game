# main_menu.py
import pygame
import sys
from settings import screen_width, screen_height, fps_limit
from main import main_game

pygame.init()

def menu(screen, clock):
    menu_font = pygame.font.Font(None, 48)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        screen.fill((67, 71, 80))
        title_text = menu_font.render("Survival Game", True, (255, 255, 255))
        start_text = menu_font.render("Press Enter to Start", True, (255, 255, 255))
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 3))
        screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, screen_height // 2))

        pygame.display.flip()
        clock.tick(fps_limit)

if __name__ == "__main__":
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    start_game_func = menu(screen, clock)
    start_game_func(screen, clock)