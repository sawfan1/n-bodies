import pygame
import pygame.freetype

pygame.init()

# parameters
FPS = 60
WIDTH = 800
HEIGHT = 600
GAME_FONT = pygame.freetype.Font("fonts/Aloevera.ttf", 20)
SMALL_FONT = pygame.freetype.Font("fonts/Aloevera.ttf", 12)
INPUT_FONT = pygame.freetype.Font("fonts/Aloevera.ttf", 18)
NUMS = pygame.freetype.Font("fonts/Swansea.ttf", 22)
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

  field_text = str(STARTING_MASS)

  # submit button settings
  bd = [60, 25]
  bpos = [pos[0] + dimensions[0]/2 - 30, ipos[1]+40]
  b_object = pygame.Rect(bpos[0], bpos[1], bd[0], bd[1])

  def update(self, new_field_text):
    self.field_text = new_field_text

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

    NUMS.render_to(screen, (self.ipos[0] + 10,self.ipos[1] + 8), self.field_text, WHITE)


class Body:
  position = [200, 200]
  velocity = [2, 0]
  mass = 5

  def __init__(self, pos, vel, mass=5):
    self.position = pos
    self.velocity = vel
    self.mass = mass

class Game:
  running = True
  panel = Panel()
  cur_mass = STARTING_MASS

  bodies = [Body([300, 200], [0, 0]), 
  Body([150, 200], [0, 0]),
  Body([300, 250], [0, 0]),
  Body([300, 100], [0, 0])
            ] # collection of bodies really

  def update_mass(self, new_mass):
    try:
      valid = int(new_mass)
    except:
      self.panel.update(str(self.cur_mass))
      return

    if (valid < 0):
      self.panel.update(str(self.cur_mass))
      return

    self.cur_mass = valid

  def handle_input(self):
    # quit game response
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False

      if event.type == pygame.MOUSEBUTTONDOWN:
        if self.panel.input_obj.collidepoint(event.pos):
          self.panel.text_active = True
        else:
          self.panel.text_active = False

        if self.panel.b_object.collidepoint(event.pos):
          self.update_mass(self.panel.field_text)

      if self.panel.text_active and event.type == pygame.KEYDOWN:
        if (event.key == pygame.K_RETURN):
          self.panel.text_active = False
        elif (event.key == pygame.K_BACKSPACE):
          self.panel.update(self.panel.field_text[:-1])
        else:
          self.panel.update(self.panel.field_text + event.unicode)

      

  def draw(self):
    # background
    screen.fill("black")

    # render all the points
    for body in self.bodies:
      pygame.draw.circle(screen, WHITE, (body.position[0], body.position[1]), 5)

    # ignore boilerplate
    self.panel.render()
    pygame.display.flip()
    clock.tick()


game = Game()

while game.running:
  game.draw()
  game.handle_input()

pygame.quit()

