import pygame
from game import Game
pygame.init()

# fenetre
pygame.display.set_caption("LeJeuDeGxntil")
screen = pygame.display.set_mode((1080, 720))

# importer de charger.....
background = pygame.image.load('assets/bg.jpg')

# importe charger notre banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() / 4

# importer charger notre bouton pour lancer le jeu
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width() / 3.33
play_button_rect.y = screen.get_height() / 2

# charger notre jeu
game = Game()

running = True

# boucle
while running:

    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    # verifier si le jeu a commence
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)
    # verif si notre jeu n'a pas commence
    else:
        # ajouter mon ecran de bvn
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # que l'event est fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # detecter
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter la touche espace
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
