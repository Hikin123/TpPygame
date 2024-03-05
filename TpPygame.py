import pygame
 
 

import time
 
pygame.init()
 
 
display = pygame.display.set_mode((500, 500))

#font = pygame.font.SysFont(None, 40)

text2 = 'appuyez sur une touche'
font = pygame.font.SysFont(None, 40)
img = font.render(text2, True, (255, 0, 0))

rect = img.get_rect()
rect.topleft = (20, 20)
 
display.fill((200, 200, 200))
display.blit(img,rect)
 
pygame.display.update()
running = True
 
 
while running:
       
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
         
        
        if event.type == pygame.KEYDOWN:
             
             text =  'Vous avez appuyé la touche ' + event.unicode   
             text2 = 'appuyez sur une touche'      
             font = pygame.font.SysFont(None, 40)
             img = font.render(text, True, (255, 0, 0))
             img2 = font.render(text2, True, (255, 0, 0))
             rect = img.get_rect()
             rect2 = img2.get_rect()
             rect2.topleft = (40, 20)
             rect.topleft = (40, 250)
             display.fill((200, 200, 200))
             display.blit(img,rect)
             display.blit(img2,rect2)
              
             pygame.display.update()
             
             