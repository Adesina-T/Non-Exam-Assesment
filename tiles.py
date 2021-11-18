import pygame

class Tile (pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        #self.image = pygame.Surface((size,size))
        self.image = pygame.image.load('C:/Users/Samue/Desktop/pcdynasty/graphics/floor.png')
        self.image=pygame.transform.scale(self.image, (75, 70))

        #self.image.fill('brown')
        self.rect = self.image.get_rect(topleft= pos)

    def update(self,x_shift):
        self.rect.x += x_shift
