import pygame
import pygame.freetype
from math import sqrt

from helpers import *

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
    self.radius = radius_from_mass(mass)
    self.color = color_from_mass(mass)

class Game:
  running = True
  panel = Panel()
  cur_mass = STARTING_MASS

  bodies = [Body([300, 200], [0, 0], 20),
  Body([150, 200], [5, 1], 40),
  Body([300, 250], [-4, 20], 100),
  Body([300, 100], [3, -20], 70),
  Body([400, 100], [-7, 6], 120),
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
      pygame.draw.circle(screen, body.color, (body.position[0], body.position[1]), body.radius)

    # ignore boilerplate
    self.panel.render()
    pygame.display.flip()
    clock.tick()

  def engine(self):
    G = 20
    dt = 1/FPS
    soften = 3

    accelerations = [[0.0, 0.0] for _ in self.bodies]
    for i, bodyA in enumerate(self.bodies):
      ax = 0
      ay = 0

      for j, bodyB in enumerate(self.bodies):
          if i != j:
              distance = sqrt((bodyA.position[0]-bodyB.position[0])**2 + (bodyA.position[1]-bodyB.position[1])**2)
              if distance > 200:
                  K = 0.4 * distance * G
              else:
                  K = G

              anet = (K * bodyB.mass) / (distance**2 + soften**2) # newtons law
              ax += anet * (bodyB.position[0] - bodyA.position[0]) / distance
              ay += anet * (bodyB.position[1] - bodyA.position[1]) / distance
      accelerations[i] = [ax, ay]

    for k, body in enumerate(self.bodies): # this updates all the positions
        body.velocity[0] += accelerations[k][0] * dt
        body.velocity[1] += accelerations[k][1] * dt
        body.position[0] += body.velocity[0] * dt
        body.position[1] += body.velocity[1] * dt

        if body.position[0]-body.radius < 0 or body.position[0]+body.radius > WIDTH:
          body.velocity[0] *= -1

        if body.position[1]-body.radius < 0 or body.position[1]+body.radius > HEIGHT:
          body.velocity[1] *= -1



game = Game()

while game.running:
  game.draw()
  game.handle_input()
  game.engine()

pygame.quit()
