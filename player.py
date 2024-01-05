#player.py
import pygame
from settings import screen_width, screen_height

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.base_image = pygame.image.load("player.png")  # Load the player icon
        self.base_image = pygame.transform.scale(self.base_image, (100, 100))  # Resize the icon
        self.image = self.base_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed = 10
        self.size = 50  # Adjusted initial size
        self.magnet_field = 50 # Adjusted initial magnet field
        self.coins_multi = 0
        self.coins = 0
        self.coins_collected = 0
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

    def apply_upgrade(self, upgrade_type):
        if upgrade_type == "size":
            self.size = int(self.size * 0.98)
            self.image = pygame.transform.scale(self.base_image, (2 * self.size, 2 * self.size))
        elif upgrade_type == "magnet":
            self.magnet_field += 1
            # Vergrößere die Hitbox entsprechend des Magnetfelds
            self.rect.inflate_ip(self.magnet_field, self.magnet_field)
        elif upgrade_type == "multiplier":
            self.coins_multi += 1

    def get_position(self):
        return self.rect.x, self.rect.y

    def draw_hitbox(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

    def collect_coin(self, amount):
        self.coins_collected += amount
        self.coins += amount     