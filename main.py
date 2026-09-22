import pygame

# parameters
FPS = 60
WIDTH = 700
HEIGHT = 400

# boilerplate
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Panel:
  pos = [10, 10]
  dimensions = [300, 200]
  background = (255, 255, 255)
  rect_obj = pygame.Rect(pos[0], pos[1], dimensions[0], dimensions[1])

class Body:
  pass

class Game:
  running = True
  def handle_input(self):
    # quit game response
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False    

  def draw(self):
    # background
    screen.fill("black")

    # panel
    panel = Panel()
    pygame.draw.rect(screen, panel.background, panel.rect_obj, 2)

    # ignore boilerplate
    pygame.display.flip()
    clock.tick()


game = Game()

while game.running:
  game.draw()
  game.handle_input()

pygame.quit()

