from math import floor

def color_from_mass(mass):
  R = max(40, (floor(mass) * 10001) % 255)
  G = max(40, (floor(mass) * 20001) % 255)
  B = max(50, (floor(mass) * 25071) % 255)

  return (R, G, B)

def radius_from_mass(mass):
  # 5 - 100 radius
  radius = max(5, min(floor(mass*mass/1000), 100))
  return radius

if __name__ == "__main__":
  # test
  trial_mass = float(input("Enter a mass: "))
  print("The colour is", color_from_mass(trial_mass))
  print("The radius is", radius_from_mass(trial_mass))


# mass can be any number