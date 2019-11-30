import pygame

pygame.init()
size = width, height = (800, 800)
screen = pygame.display.set_mode(size)


def draw():
    rect_color1 = pygame.Color('white')
    rect_color2 = pygame.Color('blue')
    rect_color3 = pygame.Color('red')
    rect_width = 0
    step = 100
    rect_point1 = [(step, step), (300, 100)]
    rect_point2 = [(step, step*2), (300, 100)]
    rect_point3 = [(step, step * 3), (300, 100)]
    # Рисуем прямоугольник
    pygame.draw.rect(screen, rect_color1, rect_point1, rect_width)
    pygame.draw.rect(screen, rect_color2, rect_point2, rect_width)
    pygame.draw.rect(screen, rect_color3, rect_point3, rect_width)



draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
