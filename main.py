import pygame

pygame.init()
print ("setup started")
window = pygame.display.set_mode(size = (600,480))
print("setup ended")
while True:
    #check for all event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #fevha a janela
            quit()
