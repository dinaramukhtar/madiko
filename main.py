import pygame

from game import Game
pygame.init()

screen_size = (1000, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Jungle")

clock = pygame.time.Clock()

screen_10 = screen_size[1] // 10

game = Game.new_game(screen_10=screen_10)


while game.playing:  # Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game.playing = False

    screen.fill((255, 255, 255))

    screen.blit(game.sprites.hero_idle_right, (10, 10))

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
