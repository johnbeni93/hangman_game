import pygame
import math

#setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HaNgMaN GaMe!")

#button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - ((RADIUS * 2) + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + (GAP * 2) + (((RADIUS * 2) + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + (RADIUS * 2)))
    letters.append([x, y, chr(A + i), True])

#fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 40)

#load images
images = []

for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

#game variables
hangman_status = 0
word = "ELEMENTARY"
guessed = ["E", "L"]


#colors
PURPLE = (153, 102, 255)
WHITE = (255, 255, 255)
BLACK = (255, 255, 255)

#setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(PURPLE)

    #draw word
    display_word = ""
    for letter in word:
      if letter in guessed:
        display_word += letter + " "
      else: 
        display_word += "_ "
    text = WORD_FONT.render(display_word, 1, WHITE)
    win.blit(text, (400, 200))
     


    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
          pygame.draw.circle(win, WHITE, (x, y), RADIUS, 3)
          text = LETTER_FONT.render(ltr, 1, WHITE)
          win.blit(text, ((x - text.get_width() / 2),
                          (y - text.get_height() / 2)))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


while run:
    clock.tick(FPS)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
              x, y, ltr, visible = letter
              if visible:
                dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                if dis < RADIUS:
                  letter[3] = False

pygame.quit()
