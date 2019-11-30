import pygame

pygame.init()
size = width, height = (800, 800)
screen = pygame.display.set_mode(size)


def draw():
    # Устанавливаем параметры кирпичей и прослойки между ними
    rect_color = pygame.Color('red')
    rect_width = 0
    step = 100
    rect_point = [(step, step), (300, 100)]
    # Рисуем прямоугольник
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)



draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
