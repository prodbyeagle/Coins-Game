# settings_menu.py

import pygame
import sys
from settings import screen_width, screen_height, fps_limit, volume, fullscreen

pygame.init()

# Initialisiere Pygame Sound
pygame.mixer.init()

# Lade Sounddateien
coin_sound = pygame.mixer.Sound("coin_sound.wav")
upgrade_sound = pygame.mixer.Sound("upgrade_sound.wav")
coin_sound.set_volume(volume)
upgrade_sound.set_volume(volume)

# Setze die Schriftart für den Button-Text
button_font = pygame.font.Font(None, 24)

def settings_menu():
    global screen_width, screen_height, fps_limit, volume, fullscreen

    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Einstellungen")

    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, (255, 0, 0), (50, 50, 300, 30))
        volume_text = button_font.render(f"Lautstärke: {int(volume * 100)}%", True, (0, 0, 0))
        screen.blit(volume_text, (50, 50))

        # Beispiel: Vollbildschirm umschalten
        pygame.draw.rect(screen, (255, 0, 0), (50, 100, 200, 30))
        fullscreen_text = button_font.render(f"Vollbildschirm: {fullscreen}", True, (0, 0, 0))
        screen.blit(fullscreen_text, (50, 100))

        # Beispiel: Zurück zum Spiel-Button
        pygame.draw.rect(screen, (255, 0, 0), (50, 150, 200, 30))
        back_to_game_text = button_font.render("Zurück zum Spiel", True, (0, 0, 0))
        screen.blit(back_to_game_text, (50, 150))

        pygame.display.flip()
        clock.tick(fps_limit)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Überprüfe, ob der Mausklick auf den Zurück zum Spiel-Button liegt
                if 50 <= mouse_pos[0] <= 250 and 150 <= mouse_pos[1] <= 180:
                    running = False

    pygame.quit()
    sys.exit()