import sys, pygame, math, random
#~~~~~~~~asteroid game~~~~~~~~#
def start_state():
    size = width, height = 700, 700
    game = {
        "ship": {
            "position": {"x": 350, "y": 350},
            "angle": 0,
            "image": pygame.image.load("space.png"),
            "rect": pygame.image.load("space.png").get_rect()
        },
        "screen": pygame.display.set_mode(size),
        "background": pygame.image.load("AndromedaGalaxy.png"),
        "asteroids": [
            {"image": pygame.image.load("asteroid.png"),
             "pos": {"x": 0, "y": 0},
             "angle": random.randint(0, 90),
             "rect": pygame.image.load("asteroid.png").get_rect()
            },
        ],
        "bullet": {
            "image": pygame.image.load("bullet.png"),
            "pos": {"x": 350, "y": 350},
            "angle": 0,
            "fired": False

        }
    }
    return game


def init(game):
    pygame.display.set_caption("Asteroids")
    ship_rect = game["ship"]["rect"]
    ship_rect.bottom = game["ship"]["position"]["y"]
    ship_rect.right += game["ship"]["position"]["x"]
    screen = game["screen"]
    screen.blit(game["ship"]["image"], ship_rect)
    backgroundRect = game["background"].get_rect()
    screen.blit(game["background"], backgroundRect)
    pygame.display.flip()


# for n in range(1, 3):
#    asteroids.append(pygame.image.load("asteroid.png"))
#    pygame.display.flip()


def gameLoop(game):
    num = random.randint(0, 50)
    if num == 1:
        newAsteroid = {
                "image": pygame.image.load("asteroid.png"),
                "pos": {"x": 0, "y": 0},
                "angle": random.randint(0, 90)
        }
        game["asteroids"].append(newAsteroid)
    ship = game["ship"]
    shipPos = game["ship"]["position"]
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
    bulletAngle = game["bullet"]["angle"]
    bulletAngle = bulletAngle + 180
    bullet = game["bullet"]
    if bullet["fired"] == True:
        bullet["pos"]["x"] += 5 * math.sin(bulletAngle * 0.017453)
        bullet["pos"]["y"] += 5 * math.cos(bulletAngle * 0.017453)

    #draw all the sprites now, so we can use their rects to
    #check for collisions
    draw(game)
    shipRect = game["ship"]["image"].get_rect()
    shipRect.right += 350
    shipRect.bottom += 350
    #now check for any collisions
    #shiprect = ship["image"].get_rect()
    for i in range(len(game["asteroids"])-1, -1, -1):
        asteroid = game["asteroids"][i]
        asteroid["pos"]["x"] += 5 * math.sin(asteroid["angle"] * 0.017453)
        asteroid["pos"]["y"] += 5 * math.cos(asteroid["angle"] * 0.017453)
        asteroidRect = asteroid["rect"]
        if asteroidRect.colliderect(shipRect):
            pygame.quit()
            sys.exit()
        if (asteroid["pos"]["x"] == shipPos["x"]) and (shipPos["y"] == asteroid["pos"]["y"]):
            pygame.quit()
            sys.exit()


def draw(game):
    screen = game["screen"]
    background = game["background"]
    backgroundRect = background.get_rect()
    # Rotate the ship image and then draw it
    ship = game["ship"]
    shipAngle = ship['angle']
    shipImage = ship["image"]
    rotated_surface = pygame.transform.rotate(shipImage, shipAngle)
    surface_centre = rotated_surface.get_rect().center
    draw_centre_x = ship["position"]["x"] - surface_centre[0]
    draw_centre_y = ship["position"]["y"] - surface_centre[1]
    shipRect= shipImage.get_rect()
    shipRect.move(draw_centre_x - shipRect.right, draw_centre_y - shipRect.top)
    shipRect.right += 350
    shipRect.bottom += 350
    screen.blit(background, backgroundRect)
    screen.blit(rotated_surface, shipRect)
    for asteroid in game["asteroids"]:
        asteroidRect = asteroid["image"].get_rect()
        asteroid_x = asteroid["pos"]["x"]
        asteroid_y = asteroid["pos"]["y"]

        asteroid["rect"] = asteroidRect.move(asteroid_x - asteroidRect.right, asteroid_y - asteroidRect.top)

        screen.blit(asteroid["image"], asteroid["rect"])

    # Draw the bullet, if it has been fired
    if game["bullet"]["fired"] == True:
        bullet_rect = game["bullet"]["image"].get_rect()
        bullet_rect.bottom = game["bullet"]["pos"]["y"]
        bullet_rect.right += game["bullet"]["pos"]["x"]
        screen.blit(game["bullet"]["image"], bullet_rect)
    pygame.display.flip()


game = start_state()
pygame.init()
init(game)
while True:
    gameLoop(game)
