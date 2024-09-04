import pygame

pygame.init()

SCREEN_WITDH = 1000
SCREEN_HEIGHT = 760

screen = pygame.display.set_mode((SCREEN_WITDH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50 , 50))


run = True
while run:

    screen.fill((0, 0, 0))
    hbox , vbox = 20, 20



    pygame.draw.rect(screen,(255, 0, 0), player)
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-5, 0) #speed to the left

    if player.x < 0 : player.x = 0 #Boundry to the left

    elif key[pygame.K_d]:
        player.move_ip(5, 0) #speed to the right

    if player.x > 950 : player.x = 950 #Boundry to the right

    elif key[pygame.K_w]:
        player.move_ip(0, -5) #speed to the top

    if player.y < 0: player.y = 0 ##Boundry to the top

    elif key[pygame.K_s]:
        player.move_ip(0, 5) #speed to the bottom

    if player.y > 710: player.y = 710 #Boundry to the bottom


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()