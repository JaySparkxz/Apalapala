import pygame
from support import import_folder
class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0 
        self.animation_speed = 0.20
        self.image = self.animations['Idle'][self.frame_index]

        # ===== TEMP PLAYEr PLACE HOLDER =====
        # self.image = pygame.Surface((32,64))
        # self.image.fill('red')
        # ===== END =====
        
        self.rect = self.image.get_rect(topleft = pos)

        # PLAYER MOVEMENT 
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        # PLAYER STATUS
        self.status = 'Idle'
        self.facing_right = True

    def import_character_assets(self):
        character_path = '../Graphics/Character/'
        self.animations = {'Idle':[],'Run':[],'Crouch_Idle':[],'Crouch_Walk':[],'Hurt':[],'Jump':[],'Land':[],'Death':[], 'Fall':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        # LOOP OVER FRAME INDEX 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0 

        image = animation[int(self.frame_index)]

        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image


    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'Jump'
        elif self.direction.y > 1:
            self.status = 'Fall'
        else:
            if self.direction.x != 0:
                self.status = 'Run'
            else:
                self.status ='Idle'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += int(self.direction.y)

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.get_status()
        self.apply_gravity()
        self.animate()
