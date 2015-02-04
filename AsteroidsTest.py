import sys, pygame
def start_state():
    size = width, height = 700, 700
    game = {
            "ship" :{
                "position":{"x":350,"y":350},
                "angle":0, 
                "image":pygame.image.load("space.png")
            },
            "screen" : pygame.display.set_mode(size),
            "background":pygame.image.load("AndromedaGalaxy.png"),
            "asteroids": [],
            "bullet" :{
                "image":pygame.image.load("bullet.png"),
                "pos":{"x":350,"y":350},
                "angle":0,
                "fired":False
            }
        }
    return game


def init(game):
    pygame.display.set_caption("Asteroids")
    backgroundRect = game["background"].get_rect()
    ship_rect = game["ship"]["image"].get_rect()
    ship_rect.bottom =game["ship"]["position"]["y"]
    ship_rect.right += game["ship"]["position"]["x"]
    screen=game["screen"]
    screen.blit(game["ship"]["image"], ship_rect)
    screen.blit(game["background"], backgroundRect)
    pygame.display.flip()

#for n in range(1, 3):
#    asteroids.append(pygame.image.load("asteroid.png"))
#    pygame.display.flip()
    

def gameLoop(game):
    screen = game["screen"]
    ship = game["ship"]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        ship["angle"] += 2
    elif key[pygame.K_RIGHT]:
        ship["angle"] -= 2

    elif key[pygame.K_SPACE]:
        game["bullet"]["fired"] = True
        game["bullet"]["angle"] = game["ship"]["angle"]
#    rotatedShip = pygame.transform.rotate(ship["image"],ship["angle"])
    bullet = game["bullet"]
    if bullet["fired"] == True:
        bullet["pos"]["x"] += 1
        bullet["pos"]["y"] += 1

    draw(game)
      
def draw(game):
    screen = game["screen"]
    # Rotate the ship image and then draw it
    ship = game["ship"]
    shipImage = ship["image"]
    shipAngle = ship['angle']
    rotated_surface = pygame.transform.rotate(shipImage, shipAngle)
    surface_centre = rotated_surface.get_rect().center
    draw_centre_x = ship["position"]["x"] - surface_centre[0]
    draw_centre_y = ship["position"]["y"] - surface_centre[1]
    draw_centre = draw_centre_x, draw_centre_y 
    screen.blit(rotated_surface, draw_centre)
 
   # Draw the bullet, if it has been fired
    if game["bullet"]["fired"] == True:
            bullet_rect = game["bullet"]["image"].get_rect()
            bullet_rect.bottom =game["bullet"]["pos"]["y"]
            bullet_rect.right += game["bullet"]["pos"]["x"]
            screen.blit(game["bullet"]["image"],bullet_rect)
    pygame.display.flip()
    

game=start_state()
pygame.init()
init(game)
    
while True:
    gameLoop(game)
                
