import pygame
from plane_sprites import *


class PlaneGame(object):
    """Plane Game"""

    def __init__(self):
        print("Game init")

        # create game window
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # create game clock
        self.clock = pygame.time.Clock()
        # create sprite and sprite group
        self.__create_sprites()
        # set timer event
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        pass


    def start_game(self):
        print("Game start")

        while True:
            # set freq
            self.clock.tick(FRAME_PER_SEC)
            # event listen
            self.__event_handler()
            # collision measurement
            self.__check_collide()
            # update/draw sprites
            self.__update_sprites()
            # update screen
            pygame.display.update()
            pass

    def __event_handler(self):
        for event in pygame.event.get():
            # if want to exit game
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("right...")
            #     pass

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True, collided = None)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True, collided = None)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("Game over")

        pygame.quit()
        exit()

if __name__ == "__main__":
    # create game object
    game = PlaneGame()

    # start game
    game.start_game()
    pass

# pygame.init()

# screen = pygame.display.set_mode((480, 700))

# bg = pygame.image.load("./images/background.png")
# screen.blit(bg, (0, 0))
# # pygame.display.update()
# hero = pygame.image.load("./images/me1.png")
# screen.blit(hero, (150, 500))
# pygame.display.update()

# # create clock
# clock = pygame.time.Clock()

# # define plane init point
# hero_rect = pygame.Rect(150, 500, 102, 126)


# enemy = GameSprite("./images/enemy1.png")
# enemy1 = GameSprite("./images/enemy1.png", 2)
# enemy_group = pygame.sprite.Group(enemy, enemy1)

# while True:
#     # set freq
#     clock.tick(60)

#     # listen the event
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             print("exit game")
#             pygame.quit()
#             exit()

#     # change plane place
#     hero_rect.y -= 1

#     if hero_rect.bottom <= 0:
#         hero_rect.y = 700

#     screen.blit(bg, (0, 0))
#     screen.blit(hero, hero_rect)

#     # update sprite
#     enemy_group.update()
#     enemy_group.draw(screen)

#     pygame.display.update()


# pygame.quit()
