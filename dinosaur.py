class Dinosaur:

  def __init__(self, name, health):
    self.name = name
    self.attack_power = 25
    self.health = health
    

  def attack(self, robot):
    robot.health -= self.attack_power
    print("You hit for 25 damage with your claw\n")
    