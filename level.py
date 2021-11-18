import pygame
from tiles import Tile
from settings import tile_dimensions,screen_width

from player import Player

class Level:
    def __init__(self,level_data,surface):
        self.display_screen = surface
        self.world_shift = 0
        self.level_creation(level_data)
        self.current_x =0


    def level_creation(self, layout):
        self.blocks = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for y_column_index,row in enumerate(layout):
            for x_column_index, cell in enumerate(row):
                x = x_column_index * tile_dimensions
                y = y_column_index * tile_dimensions
                if cell == 'X':

                    tile = Tile((x,y), tile_dimensions)
                    self.blocks.add(tile)
                if cell == 'P':
                    x = x_column_index * tile_dimensions
                    y = y_column_index * tile_dimensions
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                # if cell == 'C':
                #     img = pygame.image.load(r"C:\Users\Samue\Desktop\New-Nea\Assests\coins\0.png")
                #     new = pygame.transform.scale(img, (100, 100))
                #     new_rect = new.get_rect()
                #     screen.blit((new,new_rect))


    def scroll_x(self):
        player = self.player.sprite
        player_x=player.rect.centerx
        direction_x=player.direction.x

        if player_x < screen_width/4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x> screen_width - (screen_width/4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift =0
            player.speed = 8

    def horizontal_movement_collison(self):
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed

        for sprite in self.blocks.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0 :
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >=0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x<=0):
            player.on_right = False




    def vertical_movement_collison(self):
        player = self.player.sprite

        player.mech_gravity()

        for sprite in self.blocks.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y=0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling=True
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground= False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False



    def run(self):
        #blocks
        self.blocks.update(self.world_shift)
        self.blocks.draw(self.display_screen)
        self.scroll_x()

        #player
        self.player.update()
        self.horizontal_movement_collison()
        self.vertical_movement_collison()
        self.player.draw(self.display_screen)



