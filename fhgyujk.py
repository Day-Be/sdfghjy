import os
import sys

import pygame
import requests

l = 'map'
min_m = 1
max_m = 24
x, y, m = 131.8735300, 43.1056200, 9
max_x = 180.6
min_x = -180.6
max_y = 86.1
min_y = -90
run = True
map_file = "map.png"
print('чтобы переключиться на спутник нажмите d, чтобы переключиться на гибрид нажмите w, '
      'а чтобы вернуться на карту нажмите a.')


def get_map(x1, y1, m1, l1):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={x1},{y1}&z={m1}&l={l1}"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file


pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(get_map(x, y, m, l)), (0, 0))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                if int(m) < max_m:
                    m += 1
                    screen.blit(pygame.image.load(get_map(x, y, m, l)), (0, 0))
                    pygame.display.flip()
            if event.key == pygame.K_PAGEDOWN:
                if int(m) > min_m:
                    m -= 1
                    screen.blit(pygame.image.load(get_map(x, y, m, l)), (0, 0))
                    pygame.display.flip()
            if event.key == pygame.K_UP:
                if int(y) < max_y:
                    y += 0.2
                    screen.blit(pygame.image.load(get_map(x, y, m, l)), (0, 0))
                    pygame.display.flip()
            if event.key == pygame.K_DOWN:
                if int(y) > min_y:
                    y -= 0.2
                    screen.blit(pygame.image.load(get_map(x, y, m, l)), (0, 0))
                    pygame.display.flip()
            if event.key == pygame.K_RIGHT:
                if int(m) < max_x:
                    x += 0.02
                    screen.blit(pygame.image.load(get_map(x, y, m, l)), (0, 0))
                    pygame.display.flip()
            if event.key == pygame.K_LEFT:
                if int(m) > min_x:
                    x -= 0.02
                    screen.blit(pygame.image.load(get_map(x, y, m, l)), (0, 0))
                    pygame.display.flip()
            if event.key == pygame.K_d:
                l = 'sat'
                screen.blit(pygame.image.load(get_map(x, y, m, l)), (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_w:
                l = 'sat,skl'
                screen.blit(pygame.image.load(get_map(x, y, m, l)), (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_a:
                l = 'map'
                screen.blit(pygame.image.load(get_map(x, y, m, l)), (0, 0))
                pygame.display.flip()
pygame.quit()

os.remove(map_file)