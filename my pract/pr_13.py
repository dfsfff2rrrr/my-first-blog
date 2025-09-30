import pygame
pygame.init()
dis = pygame.display.set_mode((490, 370))

font = pygame.font.SysFont(None, 24)

dis_over = False
while not dis_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dis_over = True

    dis.fill((0, 0, 0))

    cell_number = 1
    for y in range(10, 350, 60):
        for x in range(10, 450, 60):
            rect = pygame.Rect(x, y, 50, 50)
            pygame.draw.rect(dis, (0, 255, 0), rect, 1)

            text = font.render(str(cell_number), True, (0, 255, 0))
            text_rect = text.get_rect(center=rect.center)
            dis.blit(text, text_rect)

            cell_number += 1

    pygame.display.update()
