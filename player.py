# player.py
import pygame
from settings import screen_width, screen_height

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")  # Lade das Spieler-Icon
        self.image = pygame.transform.scale(self.image, (100, 100))  # Verkleinere das Icon
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed = 1
        self.size = 500
        self.magnet_field = 50090
        self.coins_multi = 1
        self.coins = 0
        self.upgrades = []

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        direction = pygame.math.Vector2(mouse_x - self.rect.centerx, mouse_y - self.rect.centery)

        if direction.length() > 0:
            direction.normalize_ip()

        self.rect.x = round(self.rect.x)
        self.rect.y = round(self.rect.y)

        self.rect.x += direction.x * self.speed
        self.rect.y += direction.y * self.speed

        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, screen_height - self.rect.height))

    def apply_upgrade(self, player):
        if self.type == "size":
            player.size += 5
        elif self.type == "magnet":
            player.magnet_field += 1
        elif self.type == "multiplier":
            player.coins_multi += 1

    def get_position(self):
        return self.rect.x, self.rect.y            