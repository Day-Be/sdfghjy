import os
import sys

import pygame
import requests

x, y, m = 132, 43.2, 9
run = True
map_file = "map.png"


def get_map(m1):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={x},{y}&z={m1}&l=map"
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
screen.blit(pygame.image.load(get_map(m)), (0, 0))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                m += 1
                screen.blit(pygame.image.load(get_map(m)), (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_PAGEDOWN:
                m -= 1
                screen.blit(pygame.image.load(get_map(m)), (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_UP:
                y += 0.02
                screen.blit(pygame.image.load(get_map(m)), (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_DOWN:
                y -= 0.02
                screen.blit(pygame.image.load(get_map(m)), (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_RIGHT:
                x += 0.02
                screen.blit(pygame.image.load(get_map(m)), (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_LEFT:
                x -= 0.02
                screen.blit(pygame.image.load(get_map(m)), (0, 0))
                pygame.display.flip()
pygame.quit()

os.remove(map_file)