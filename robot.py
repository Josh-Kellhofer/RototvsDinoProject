from weapon import Weapon

class Robot:

  def __init__(self, name):
    self.name = name
    self.health = 60
    self.weapon = Weapon("laser blade", 30)

  def attack(self, dinosaur):
      pass

  