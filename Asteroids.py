import sys, pygame, time

def init(screen,ship):
    background = pygame.image.load("AndromedaGalaxy.png")
    pygame.display.set_caption("Asteroids")
    backgroundRect = background.get_rect()
    ship_rect = ship.get_rect()
    ship_rect.bottom += 350
    ship_rect.right += 350
    screen.blit(ship, ship_rect)
    screen.blit(background, backgroundRect)
    pygame.display.flip()
    return ship_rect

pygame.init()
size = width, height = 700, 700
screen = pygame.display.set_mode(size)
ship = pygame.image.load("space.png")


asteroids = []
for n in range(1, 3):
    asteroids.append(pygame.image.load("asteroid.png"))
    pygame.display.flip()
    

def gameLoop(shipImage,start_position,screen,ship_angle):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    rotatedShip = pygame.transform.rotate(shipImage,ship_angle)
    screen.blit(rotatedShip, start_position)
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        ship_angle -= 2
    elif key[pygame.K_RIGHT]:
        ship_angle += 2
    pygame.display.flip()
    return ship_angle

    
start_pos = init(screen,ship)
angle = 0
while True:
    angle = gameLoop(ship, start_pos,screen,angle)

pygame.display.flip()
                
