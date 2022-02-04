class Dinosaur:

  def __init__(self, name, health):
    self.name = name
    self.attack_power = 25
    self.health = health
    

  def attack(self, robot):
    self.robot = robot
    print("You hit for 25 damage with your claw")
    robot.health -= 25