import pygame
import random

pygame.init()
dis = pygame.display.set_mode((500, 400))

font = pygame.font.SysFont(None, 48)


class Snowflake:
    def __init__(self):
        self.x = random.randint(0, 500)
        self.y = random.randint(-50, 0)
        self.speed = random.uniform(-1, 3)

    def fall(self):
        self.y += self.speed
        if self.y > 400:
            self.x = random.randint(0, 500)
            self.y = random.randint(-50, 0)
            self.speed = random.uniform(-1, 1)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), 3)


snowflakes = [Snowflake() for _ in range(50)]

dis_over = False
while not dis_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dis_over = True

    dis.fill((0, 0, 0))


    text = font.render("Снеговик", True, (255, 255, 255))
    dis.blit(text, (180, 10))

    pygame.draw.circle(dis, (255, 255, 255), [250, 320], 80, 0)
    pygame.draw.circle(dis, (255, 255, 255), [250, 220], 60, 0)
    pygame.draw.circle(dis, (255, 255, 255), [250, 135], 40, 0)
    pygame.draw.circle(dis, (0, 0, 0), [250, 320], 5, 0)
    pygame.draw.circle(dis, (0, 0, 0), [250, 300], 5, 0)
    pygame.draw.circle(dis, (0, 0, 0), [250, 280], 5, 0)
    pygame.draw.circle(dis, (0, 0, 0), [250, 260], 5, 0)
    pygame.draw.circle(dis, (0, 0, 0), [250, 240], 5, 0)
    pygame.draw.circle(dis, (0, 0, 0), [250, 220], 5, 0)
    pygame.draw.circle(dis, (0, 0, 0), [235, 135], 5, 0)
    pygame.draw.circle(dis, (0, 0, 0), [265, 135], 5, 0)
    pygame.draw.line(dis, (139, 69, 19), [190, 220], [80, 80], 5)
    pygame.draw.line(dis, (139, 69, 19), [310, 220], [420, 80], 5)
    pygame.draw.polygon(dis, (210, 105, 30), [(250, 150), (290, 145), (250, 140)])




    for flake in snowflakes:
        flake.fall()
        flake.draw(dis)

    pygame.display.update()

pygame.quit()
