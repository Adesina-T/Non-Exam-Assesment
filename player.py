import pygame
from support import import_folder
from pygame import mixer
#from main import new_player_speed




class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.character_animation_states()
        self.frame_index = 0
        self.animations_speed = 0.15
        self.image = self.animations['Idle'][self.frame_index]
        self.image = pygame.transform.scale(self.image,(150,100))


        self.rect=self.image.get_rect(topleft=pos)


        #player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.7
        self.jump_speed = -15

        #player status
        self.status = 'Idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

        #attack
        self.attack = False

    def character_animation_states(self):
        character_path= 'C:/Users/Samue/Desktop/New-Nea/Fighter/'
        self.animations = {'Idle':[],'Run':[],'Jump':[],'Fall':[],'Attack':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animations_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image



        # rects
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)






    def user_input(self):

        keys = pygame.key.get_pressed()



        if keys[pygame.K_d]:
            self.direction.x =1
            self.facing_right = True
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
        if keys[pygame.K_w] and self.on_ground:
            self.jump()




    def get_status(self):
        if self.direction.y < 0:
            self.status = 'Jump'
        elif self.direction.y > 1 :
            self.status='Fall'
        else:
            if self.direction.x !=0:
                self.status='Run'
            else:
                self.status='Idle'
        if self.attack == True:
            self.status = 'Attack'





    def mech_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.user_input()
        self.get_status()
        self.animate()


