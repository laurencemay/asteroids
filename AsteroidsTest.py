import sys, pygame, math, random
#~~~~~~~~asteroid game~~~~~~~~#
def start_state():
    size = width, height = 700, 700
    game = {
        "ship": {
            "position": {"x": 350, "y": 350},
            "angle": 0,
            "image": pygame.image.load("space.png"),
            "rect": pygame.image.load("space.png").get_rect(),
            "health":5,
            "hits":0
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
        "bullet":{
            "rect":pygame.image.load("bullet.png").get_rect(),
            "image": pygame.image.load("bullet.png"),
            "pos": {"x": 350, "y": 350},
            "angle": 0,
            "fired": False
            },

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
        bullet = game["bullet"]
        bullet["fired"] = True
        bullet["angle"] = game["ship"]["angle"]
        bullet["pos"]["x"] = 350
        bullet["pos"]["y"] = 350

    bulletAngle = game["bullet"]["angle"]
    bulletAngle = bulletAngle + 180
    bullet = game["bullet"]
    if bullet["fired"] == True:
        bullet["pos"]["x"] += 5 * math.sin(bulletAngle * 0.017453)
        bullet["pos"]["y"] += 5 * math.cos(bulletAngle * 0.017453)
        if bullet["pos"]["x"] > 700 or bullet["pos"]["x"] < 0:
            bullet["fired"] == False
        if bullet["pos"]["y"] > 700 or bullet["pos"]["y"] < 0:
            bullet["fired"] == False
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
        if bullet["rect"].colliderect(asteroidRect) and bullet["fired"] == True:
            game["asteroids"].remove(asteroid)
            ship["hits"] += 1
        if asteroidRect.colliderect(shipRect):
            if asteroid in game["asteroids"]:
                game["asteroids"].remove(asteroid)
            ship["health"] -= 1
            if ship["health"] == 0:
                print("You Died D: you hit " + str(ship["hits"]) + " asteroids")
                pygame.quit()
                sys.exit()


def draw(game):
    screen = game["screen"]
    background = game["background"]
    backgroundRect = background.get_rect()


 #   draw_centre_x = ship["position"]["x"] - surface_centre[0]
 #   draw_centre_y = ship["position"]["y"] - surface_centre[1]
 #   draw_centre = draw_centre_x, draw_centre_y

#    screen.blit(rotated_surface, draw_centre)


    # Rotate the ship image and then draw it
    ship = game["ship"]
    shipAngle = ship['angle']
    shipImage = ship["image"]
    rotated_surface = pygame.transform.rotate(shipImage, shipAngle)
    surface_centre = rotated_surface.get_rect().center
    draw_centre_x = ship["position"]["x"] - surface_centre[0]
    draw_centre_y = ship["position"]["y"] - surface_centre[1]
    shipRect= shipImage.get_rect()
    shipRect = shipRect.move(draw_centre_x - shipRect.right, draw_centre_y - shipRect.top)
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
        bullet = game["bullet"]
        bulletX = bullet["pos"]["x"]
        bulletY = bullet["pos"]["y"]
        bullet["rect"] = bullet_rect.move(bulletX - bullet_rect.right, bulletY - bullet_rect.top)
        screen.blit(game["bullet"]["image"], bullet["rect"])
    pygame.display.flip()
game = start_state()
pygame.init()
init(game)
while True:
    gameLoop(game)
