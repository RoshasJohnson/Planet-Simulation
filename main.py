import pygame
import math

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Planet simulation')


class Planet:
    AU = 149.6e6 * 1000  # this is approximately distance between sun and earth
    G = 6.6742e-11  # gravitational constant
    SCALE = 250 / AU  # 1 AU = 100 pixels
    TIMESTEP = 3600 * 24  # 1 day


    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit = []
        self.distance_to_sun = 0
        self.x_vel = 0
        self.x_vel = 0


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


main()
