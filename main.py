import pygame
import button

pygame.init()

#Screen window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Name")

# Game Font Style
font = pygame.font.SysFont("arialblack", 40)


#Button Images
Start = pygame.image.load('images/Start.png').convert_alpha()
Settings = pygame.image.load('images/Settings.png').convert_alpha()
Quit = pygame.image.load('images/Quit.png').convert_alpha()

#Button Functions
StartButton = button.Button(150, 150, Start, 0.5)
SettingsButton = button.Button(150, 200, Settings, 0.5)
QuitButton = button.Button(150, 250, Quit, 0.5)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

# Menu
run = True
while run:

    StartButton.draw(screen)
    SettingsButton.draw(screen)
    QuitButton.draw(screen)

    """How to get to next screen without overusing nested if?"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()
