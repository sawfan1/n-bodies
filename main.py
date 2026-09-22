import pygame
import pygame.freetype

pygame.init()

# parameters
FPS = 60
WIDTH = 800
HEIGHT = 600
GAME_FONT = pygame.freetype.Font("Aloevera.ttf", 20)
SMALL_FONT = pygame.freetype.Font("Aloevera.ttf", 12)
STARTING_MASS = 5

# boilerplate
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# extraneous variables
WHITE = (255, 255, 255)

class Panel:
  margin = 20
  dimensions = [200, 120]
  pos = [WIDTH-dimensions[0]-margin, margin]
  background = WHITE
  text_color = WHITE
  text = "Body mass: (KG)"
  rect_obj = pygame.Rect(pos[0], pos[1], dimensions[0], dimensions[1])

  # input rectangle settings
  ipos = [pos[0] + 15, pos[1] + 45]
  idimensions = [dimensions[0]-30, 30]
  input_obj = pygame.Rect(ipos[0], ipos[1], idimensions[0], idimensions[1])
  text_active = False

  # submit button settings
  bd = [60, 25]
  bpos = [pos[0] + dimensions[0]/2 - 30, ipos[1]+40]
  b_object = pygame.Rect(bpos[0], bpos[1], bd[0], bd[1])

  def render(self):
    pygame.draw.rect(screen, self.background, self.rect_obj, 2)
    GAME_FONT.render_to(screen, (self.pos[0] + 15, self.pos[1] + 15), self.text, WHITE)

    if self.text_active:
      bg = (0, 0, 255)
    else:
      bg = WHITE

    pygame.draw.rect(screen, bg, self.input_obj, 2)
    pygame.draw.rect(screen, WHITE, self.b_object, 2)
    SMALL_FONT.render_to(screen, (self.bpos[0]+15, self.bpos[1]+10), "SET", WHITE)


class Body:
  pass

class Game:
  running = True
  panel = Panel()
  def handle_input(self):
    # quit game response
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False

      if event.type == pygame.MOUSEBUTTONDOWN:
        if self.panel.input_obj.collidepoint(event.pos):
          print("clicked me ")
          self.panel.text_active = True
        else:
          self.panel.text_active = False

  def draw(self):
    # background
    screen.fill("black")

    self.panel.render()
    
    # ignore boilerplate
    pygame.display.flip()
    clock.tick()


game = Game()

while game.running:
  game.draw()
  game.handle_input()

pygame.quit()

