# main.py
import pygame
import sys
import random
import time
from settings import screen_width, screen_height, fps_limit, volume
from player import Player
from coin import Coin
from upgrade import Upgrade
from settings_menu import settings_menu

pygame.init()
pygame.mixer.init()

# Fenster erstellen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game @prodbyeagle / @dwhincandi")

coin_icon = pygame.image.load("coin_icon.png")
upgrade_icon = pygame.image.load("upgrade_icon.png")
player_icon = pygame.image.load("player.png")
coin_sound = pygame.mixer.Sound("coin_sound.wav")
upgrade_sound = pygame.mixer.Sound("upgrade_sound.wav")

pygame.display.set_icon(coin_icon)
button_font = pygame.font.Font(None, 24)

player = Player()
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
upgrades = pygame.sprite.Group()

all_sprites.add(player)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

running = True
show_fps = False
show_coords = False
show_hitbox = False
fullscreen = False

buy_upgrade_button_rect = pygame.Rect(10, screen_height - 50, 150, 40)
booster_end_time = 0
upgrade_display_duration_seconds = 5
current_upgrade_display_start_time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((screen_width, screen_height))
            elif event.key == pygame.K_f:
                show_fps = not show_fps
                show_coords = not show_coords
                show_hitbox = not show_hitbox
            elif event.key == pygame.K_s:
                settings_menu()
                pygame.mixer.Sound.set_volume(coin_sound, volume)
                pygame.mixer.Sound.set_volume(upgrade_sound, volume)
            elif event.key == pygame.K_ESCAPE:
                running = False

    if random.randint(0, 1000) < 20:
        coin = Coin()
        coin.rect.x = random.randint(0, screen_width - coin.rect.width)  # Zufällige X-Position
        coin.rect.y = random.randint(0, screen_height - coin.rect.height)  # Zufällige Y-Position
        coins.add(coin)
        all_sprites.add(coin)

    if random.randint(0, 10000) < 5:
        upgrade_type = random.choice(["magnet", "size", "multiplier"])
        upgrade = Upgrade(f"{upgrade_type.capitalize()} Boost", upgrade_type, 5000)
        upgrade.rect.x = random.randint(0, screen_width - upgrade.rect.width)  # Zufällige X-Position
        upgrade.rect.y = random.randint(0, screen_height - upgrade.rect.height)  # Zufällige Y-Position
        upgrades.add(upgrade)
        all_sprites.add(upgrade)
        booster_end_time = time.time() + 5

    for upgrade in upgrades:
        if pygame.sprite.collide_rect(player, upgrade):
            upgrade.apply_upgrade(player)
            upgrade.kill()
            current_upgrade_display_time = upgrade_display_duration_seconds  # Setze die Anzeigezeit für das Upgrade
    
    player.update()
    
    coin_hits = pygame.sprite.spritecollide(player, coins, True)
    for coin in coin_hits:
        player.coins += 1
        coin_sound.play()    

    upgrade_hits = pygame.sprite.spritecollide(player, upgrades, True)
    for upgrade in upgrade_hits:
        player.upgrades.append(upgrade)
        upgrade.apply_upgrade(player)
        print(f"Spieler hat ein Upgrade aufgesammelt: {upgrade.name}")
        upgrade_sound.play()

    # Überprüfe, ob der Booster noch aktiv ist
    if booster_end_time > time.time():
        booster_time_remaining = int(booster_end_time - time.time())
        booster_text = font.render(f"Booster: {booster_time_remaining} Sek.", True, (255, 255, 255))
        screen.blit(booster_text, (screen_width - 200, 10))
    else:
        player.speed = 5

    if booster_end_time > time.time():
        booster_time_remaining = int(booster_end_time - time.time())
        booster_text = font.render(f"Booster: {booster_time_remaining} Sek.", True, (255, 255, 255))
        screen.blit(booster_text, (screen_width - 200, 10))

    player.update()
    screen.fill((67, 71, 80))
    all_sprites.draw(screen)

    # Anzeige der Münzen auf dem HUD
    coins_text = font.render(f"Münzen: {player.coins}", True, (255, 255, 255))
    screen.blit(coins_text, (10, 10))

    fps = int(clock.get_fps())

    if show_fps:
        if fps > 60:
            fps_color = (0, 255, 0)  # Grün
        elif 30 <= fps <= 60:
            fps_color = (255, 255, 0)  # Gelb
        else:
            fps_color = (255, 0, 0)  # Rot
        
        fps_text = font.render(f"FPS: {fps}", True, fps_color)
        screen.blit(fps_text, (10, 30))

    if show_coords:
        player_position = player.get_position()
        coords_text = font.render(f"Player Coords: {player_position}", True, (255, 255, 255))
        screen.blit(coords_text, (10, 60))

    if current_upgrade_display_start_time > 0:
        elapsed_time = time.time() - current_upgrade_display_start_time
        if elapsed_time < upgrade_display_duration_seconds:
            upgrade_display_text = font.render("Upgrade erhalten!", True, (255, 255, 255))
            screen.blit(upgrade_display_text, (screen_width // 2 - 100, screen_height // 2))
        else:
            current_upgrade_display_start_time = 0

    if show_hitbox:
        player.draw_hitbox(screen)

    pygame.display.flip()
    clock.tick(fps_limit)

pygame.quit()
sys.exit()