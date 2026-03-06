import pygame

import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

from logger import log_state

from player import Player

from shot import Shot

from asteroid import Asteroid

from asteroidfield import AsteroidField

from logger import log_event

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Shot.containers = (updatable, drawable, shots)

    Asteroid.containers = (updatable, drawable, asteroids)

    AsteroidField.containers = (updatable)

    asteroidfield = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for rock in asteroids:
            if rock.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                raise sys.exit()
            for bullet in shots:
                if rock.collides_with(bullet):
                    log_event("asteroid_shot")
                    rock.split()
                    bullet.kill()

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = (Clock.tick(60) / 1000)
        




if __name__ == "__main__":
    main()
