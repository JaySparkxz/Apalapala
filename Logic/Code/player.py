import pygame
from support import import_folder
class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        # self.frame_index = 0 
        # self.animation_speed = 0.15
        # self.image = self.animations['Player_Idle'][self.frame_index]

        # ===== TEMP PLAYEr PLACE HOLDER =====
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        # ===== END =====
        
        self.rect = self.image.get_rect(topleft = pos)




        # PLAYER MOVEMENT 
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

    def import_character_assets(self):
        character_path = '../graphics/character/'
        self.animations = {'Player_Idle':[],'Player_Run':[],'Player_Crouch_Idle':[],'Player_Crouch_Walk':[],'Player_Hurt':[],'Player_Jump':[],'Player_Land':[],'Player_Death':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += int(self.direction.y)

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.apply_gravity()
