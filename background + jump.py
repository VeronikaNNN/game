import pygame
import os
import sys

fon = pygame.image.load('fon.PNG')


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
        self.rect.top = 400
        self.dx = 4
        self.dy = 4

    def up(self):
        self.rect.top -= self.dx

    def down(self):
        self.rect.top += self.dx


def terminate():
    pygame.quit()
    sys.exit()


def draw_start(color):
    font = pygame.font.Font(None, 30)
    string_rendered = font.render('НАЧАТЬ', 0, color)
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 122
    intro_rect.x = 400
    screen.blit(string_rendered, intro_rect)


def start_screen():
    intro_text = ['ВЕСЁЛЫЕ СТАРТЫ', '',
                  '', '',
                  'РЕКОРДЫ']

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    start = (400, 122, 481, 142)
    for line in intro_text:
        string_rendered = font.render(line, 0, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 400
        text_coord += intro_rect.height
        if line == 'ВЕСЁЛЫЕ СТАРТЫ':
            print(intro_rect)
        screen.blit(string_rendered, intro_rect)
    # draw_start('white')

    while True:
        for event in pygame.event.get():
            cursor_x, cursor_y = pygame.mouse.get_pos()
            if start[0] <= cursor_x <= start[2] and start[1] <= cursor_y <= start[3]:
                draw_start('red')
            else:
                draw_start('white')
            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    start[0] <= event.pos[0] <= start[2] and start[1] <= event.pos[1] <= start[3]:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    pygame.init()
    size = WIDTH, HEIGHT = 1000, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Нагито двигается!')
    screen.blit(fon, (0, 0))
    all_sprites = pygame.sprite.Group()
    nagito = Hero()
    all_sprites.add(nagito)
    clock = pygame.time.Clock()
    fps = 60
    start_screen()
    pygame.mouse.set_visible(False)

    motion = False
    falling = False
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                motion = 'UP'
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                motion = 'STOP'
                falling = True

        if nagito.rect.top >= 300:
            if not falling and motion == 'UP':
                nagito.up()
        else:
            falling = True
        if falling:
            nagito.down()
        if nagito.rect.top > 400:
            falling = False

        screen.blit(fon, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    terminate()