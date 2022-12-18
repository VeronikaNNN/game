import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super(Hero, self).__init__()
        self.image = load_image('nagito.png')
        self.rect = self.image.get_rect()
        self.rect.top = 502
        self.dx = 4
        self.dy = 4

    def up(self):
        self.rect.top -= self.dx

    def down(self):
        self.rect.top += self.dx

    def right(self):
        if self.rect.left <= 700:
            self.rect.left += self.dy

    def left(self):
        if self.rect.left >= 4:
            self.rect.left -= self.dy


def main():
    pygame.init()
    size = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Нагито двигается!')
    screen.fill((255, 255, 255))
    all_sprites = pygame.sprite.Group()
    nagito = Hero()
    all_sprites.add(nagito)
    clock = pygame.time.Clock()
    fps = 60
    pygame.mouse.set_visible(False)

    motion = False
    falling = False
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                motion = 'UP'
            if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                motion = 'STOP'
                falling = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                motion = 'RIGHT'
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                motion = 'STOP'

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                motion = 'LEFT'
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                motion = 'STOP'

        if nagito.rect.top >= 300:
            if not falling:
                if motion == 'RIGHT':
                    nagito.right()
                elif motion == 'LEFT':
                    nagito.left()
                elif motion == 'UP':
                    nagito.up()
        else:
            falling = True
        if falling:
            nagito.down()
        if nagito.rect.top > 500:
            falling = False

        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()