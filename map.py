import os
import sys

import pygame
import requests


cordx = input()
cordy = input()
span1 = float(input())
span2 = float(input())
map_request = f"http://static-maps.yandex.ru/1.x/?ll={cordx},{cordy}&spn={span1},{span2}&l=map"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 1073741921:
                if float(span1) - 4 > 0:
                    span1 -= 4
                elif float(span1) - 2 > 0:
                    span1 -= 2
                elif float(span1) - 1 > 0:
                    span1 -= 1
                elif float(span1) - 0.5 > 0:
                    span1 -= 0.5
                elif float(span1) - 0.1 > 0:
                    span1 -= 0.1
                elif float(span1) - 0.01 > 0:
                    span1 -= 0.01
                if float(span2) - 4 > 0:
                    span2 -= 4
                elif float(span2) - 2 > 0:
                    span2 -= 2
                elif float(span2) - 1 > 0:
                    span2 -= 1
                elif float(span2) - 0.5 > 0:
                    span2 -= 0.5
                elif float(span2) - 0.1 > 0:
                    span2 -= 0.1
                elif float(span2) - 0.01 > 0:
                    span2 -= 0.01
                pass
            elif event.key == 1073741915:
                if float(span1) + 4 < 40:
                    span1 += 4
                elif float(span1) + 2 < 40:
                    span1 += 2
                elif float(span1) + 1 < 40:
                    span1 += 1
                elif float(span1) + 0.5 < 40:
                    span1 += 0.5
                elif float(span1) + 0.1 < 40:
                    span1 += 0.1
                elif float(span1) + 0.01 < 40:
                    span1 += 0.01
                if float(span2) + 4 < 40:
                    span2 += 4
                elif float(span2) + 2 < 40:
                    span2 += 2
                elif float(span2) + 1 < 40:
                    span2 += 1
                elif float(span2) + 0.5 < 40:
                    span2 += 0.5
                elif float(span2) + 0.1 < 40:
                    span2 += 0.1
                elif float(span2) + 0.01 < 40:
                    span2 += 0.01
            map_request = f"http://static-maps.yandex.ru/1.x/?ll={cordx},{cordy}&spn={span1},{span2}&l=map"
            response = requests.get(map_request)
            if not response:
                print("wtf")
            map_file = "map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
            screen.blit(pygame.image.load(map_file), (0, 0))
            pygame.display.flip()

pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
