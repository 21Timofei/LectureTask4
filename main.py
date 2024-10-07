import pygame

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Упругое столкновение квадратов")

# Параметры тел (квадраты)
m1, m2 = 1.0, 2.0  # массы тел
size1, size2 = 40, 60  # размеры квадратов (ширина и высота)
x1, y1, x2, y2 = 200, 300, 500, 300  # начальные координаты (верхний левый угол квадратов)
vx1, vy1, vx2, vy2 = 3, 0, 2, 0  # начальные скорости

# Время и скорость обновления
clock = pygame.time.Clock()
running = True


def check_collision(x1, y1, size1, x2, y2, size2):
    # Проверка пересечения границ квадратов
    return (x1 < x2 + size2 and x1 + size1 > x2 and
            y1 < y2 + size2 and y1 + size1 > y2)


def handle_wall_collision(x, y, vx, vy, size, width, height):
    # Столкновение с границами прямоугольной оболочки
    if x <= 0 or x + size >= width:
        vx = -vx
    if y <= 0 or y + size >= height:
        vy = -vy
    return vx, vy


def handle_square_collision(x1, y1, x2, y2, vx1, vy1, vx2, vy2, m1, m2, size1, size2):
    # Если произошло столкновение, меняем скорости тел
    dx, dy = x2 - x1, y2 - y1
    dist_x, dist_y = abs(dx), abs(dy)

    if dist_x > dist_y:
        # Столкновение по оси X
        vx1, vx2 = vx2, vx1
    else:
        # Столкновение по оси Y
        vy1, vy2 = vy2, vy1

    return vx1, vy1, vx2, vy2


# Основной цикл
while running:
    screen.fill((255, 255, 255))  # белый фон

    # Обновление позиций квадратов
    x1 += vx1
    y1 += vy1
    x2 += vx2
    y2 += vy2

    # Проверка столкновений с границами
    vx1, vy1 = handle_wall_collision(x1, y1, vx1, vy1, size1, WIDTH, HEIGHT)
    vx2, vy2 = handle_wall_collision(x2, y2, vx2, vy2, size2, WIDTH, HEIGHT)

    # Проверка столкновения квадратов
    if check_collision(x1, y1, size1, x2, y2, size2):
        vx1, vy1, vx2, vy2 = handle_square_collision(x1, y1, x2, y2, vx1, vy1, vx2, vy2, m1, m2, size1, size2)

    # Рисование квадратов
    pygame.draw.rect(screen, (255, 0, 0), (int(x1), int(y1), size1, size1))
    pygame.draw.rect(screen, (0, 0, 255), (int(x2), int(y2), size2, size2))

    pygame.display.flip()
    clock.tick(60)

    # Выход из программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()