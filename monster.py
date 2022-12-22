import pygame
import random


# creer la classe monstre
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = 0.00000001

    def damage(self, amount):
        # infliger les degats
        self.health -= amount

        # verifier si son nouveau nombre de points de vie est inf ou  = a 0
        if self.health <= 0:
            # Respawn le monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health

    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (87, 244, 10), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        # le deplacement ne se fait que si il n'y pas de collisions avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # infliger des degats au joueur
            self.game.player.damage(self.attack)
