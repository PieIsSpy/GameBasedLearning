import pygame
import button

pygame.init()

#Screen window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Game Name")

ScreenState = "Main Menu"
PauseGame = False

# Game Font Style
font = pygame.font.SysFont("arialblack", 40)

#Button Images
Start = pygame.image.load('images/Start.png').convert_alpha()
Settings = pygame.image.load('images/Settings.png').convert_alpha()
Quit = pygame.image.load('images/Quit.png').convert_alpha()

#Button Functions
StartButton = button.Button(600, 400, Start, 0.5)
SettingsButton = button.Button(600, 450, Settings, 0.5)
QuitButton = button.Button(600, 500, Quit, 0.5)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

def Settings():
    print('Clicked!')

# Menu
run = True
while run:

    if ScreenState == "Main Menu":
        if StartButton.draw(screen):
            print('Clicked Start Button')

        if SettingsButton.draw(screen):
            print('Settings')

        if QuitButton.draw(screen):
            print("Closed")
            run = False


    # Pressed X on tab
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()