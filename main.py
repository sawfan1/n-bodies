import pygame
import pygame.freetype

pygame.init()

# parameters
FPS = 60
WIDTH = 800
HEIGHT = 600
GAME_FONT = pygame.freetype.Font("Aloevera.ttf", 24)

# boilerplate
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Panel:
  margin = 20
  dimensions = [200, 100]
  pos = [WIDTH-dimensions[0]-margin, margin]
  background = (255, 255, 255)
  text = "Panel"
  rect_obj = pygame.Rect(pos[0], pos[1], dimensions[0], dimensions[1])

  def render(self):
    pygame.draw.rect(screen, self.panel.background, self.panel.rect_obj, 2)
    GAME_FONT.render_to(screen, (40, 350), self.text, (255, 255 ,240))


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

