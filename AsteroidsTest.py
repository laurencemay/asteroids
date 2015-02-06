import sys, pygame, math
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
            "asteroids": [
                {"image" : pygame.image.load("asteroid.png"),
                 "pos":{"x":0,"y":0},
                 "angle":37
            },
            ],
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
    ship_rect = game["ship"]["image"].get_rect()
    ship_rect.bottom =game["ship"]["position"]["y"]
    ship_rect.right += game["ship"]["position"]["x"]
    screen=game["screen"]
    screen.blit(game["ship"]["image"], ship_rect)
    backgroundRect = game["background"].get_rect()
    screen.blit(game["background"], backgroundRect)
    pygame.display.flip()

#for n in range(1, 3):
#    asteroids.append(pygame.image.load("asteroid.png"))
#    pygame.display.flip()
    

def gameLoop(game):
    asteroid = game["asteroids"][0]["image"]
    asteroidRect = asteroid.get_rect()
    ship = game["ship"]
    asteroidPos = game["asteroids"][0]["pos"]
    shipPos = game["ship"]["position"]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    shipAngle = ship['angle']
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        ship["angle"] += 2
    elif key[pygame.K_RIGHT]:
        ship["angle"] -= 2

    elif key[pygame.K_SPACE]:
        game["bullet"]["fired"] = True
        game["bullet"]["angle"] = game["ship"]["angle"]
#    rotatedShip = pygame.transform.rotate(ship["image"],ship["angle"])
    bulletAngle = game["bullet"]["angle"]
    bulletAngle = bulletAngle + 180
    bullet = game["bullet"]
    if bullet["fired"] == True:
        bullet["pos"]["x"] += 5 * math.sin(bulletAngle * 0.017453)
        bullet["pos"]["y"] += 5 * math.cos(bulletAngle * 0.017453)
    game["asteroids"][0]["pos"]["x"] += 5 * math.sin(game["asteroids"][0]["angle"] * 0.017453)
    game["asteroids"][0]["pos"]["y"] += 5 * math.cos(game["asteroids"][0]["angle"] * 0.017453)
    draw(game)
    if (asteroidPos["x"] == shipPos["x"]) and (shipPos["y"] == asteroidPos["y"]) :
        pygame.quit()
        sys.exit()
      
def draw(game):
    asteroid = game["asteroids"][0]["image"]
    asteroidRect = asteroid.get_rect()
    screen = game["screen"]
    background = game["background"]
    backgroundRect = background.get_rect()
    asteroidRect.bottom =game["asteroids"][0]["pos"]["y"]
    asteroidRect.right += game["asteroids"][0]["pos"]["x"]
    # Rotate the ship image and then draw it
    ship = game["ship"]
    shipAngle = ship['angle']
    shipImage = ship["image"]
    rotated_surface = pygame.transform.rotate(shipImage, shipAngle)
    surface_centre = rotated_surface.get_rect().center
    draw_centre_x = ship["position"]["x"] - surface_centre[0]
    draw_centre_y = ship["position"]["y"] - surface_centre[1]
    draw_centre = draw_centre_x, draw_centre_y 
    screen.blit(background, backgroundRect)
    screen.blit(rotated_surface, draw_centre)
    screen.blit(asteroid, asteroidRect)
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
                
