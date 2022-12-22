import pygame


# definir la class projectile
class Projectile(pygame.sprite.Sprite):

    # definir le constructeur de la class
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 1
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0


    def rotate(self):
        # tourner le projectile sur lui meme
        self.angle += 100
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity

        # verifier si le projectile entre collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimer le projectile
            self.remove()
            # infliger des degats
            monster.damage(self.player.attack)

        # verifier si notre projectile n'est plus present sur l'ecran
        if self.rect.x > 1080:
            # supprimer le projectile
            self.remove()

