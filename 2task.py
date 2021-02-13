import os
import sys

import pygame
import requests

min_m = 1
max_m = 8
x, y, m = input(), input(), int(input())
run = True
map_file = "map.png"


def get_map(x1, y1, m1):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={x1},{y1}&z={m1}&l=map"
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
screen.blit(pygame.image.load(get_map(x, y, m)), (0, 0))
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
                    screen.blit(pygame.image.load(get_map(x, y, m)), (0, 0))
                    pygame.display.flip()
            if event.key == pygame.K_PAGEDOWN:
                if int(m) > min_m:
                    m -= 1
                    screen.blit(pygame.image.load(get_map(x, y, m)), (0, 0))
                    pygame.display.flip()
pygame.quit()

os.remove(map_file)

