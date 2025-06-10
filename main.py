# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import AsteroidField 
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    new_player =  Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    updatables = [new_player]
    drawables = [new_player]

    asteroid_field = AsteroidField()

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        # new_player.update(dt)

        Asteroid.containers(asteroids, updatable, drawable)

        AsteroidField.containers = (updatable,)
        Shot.containers = (shots, updatable, drawable)
        for obj in updatables:
            obj.update(dt)

        screen.fill((0, 0, 0))
        for obj in drawables:
            obj.draw(screen)
            

        pygame.display.flip()

        dt=clock.tick(60) / 1000

        new_player.draw(screen)

        for asteroid in asteroids:
            if new_player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                exit()


        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
                    break



if __name__ == "__main__":
    main()