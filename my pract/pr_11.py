import pygame
pygame.init()
dis=pygame.display.set_mode((500,400))
r = pygame.Rect(150,150,150,200)

dis_over=False
while not dis_over:
    for event in pygame.event.get():
        pygame.draw.rect(dis,(255, 255, 255),r, 10)
        pygame.draw.line(dis,(255,131,24), [150,150],[225,10], 4)
        pygame.draw.line(dis, (255, 131, 24), [298, 150], [225, 10], 4)
        pygame.draw.circle(dis,(255,230,24),[400,100],40,0)
        pygame.draw.circle(dis,(255,152,24,),[387,100], 11, 0)
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
quit()