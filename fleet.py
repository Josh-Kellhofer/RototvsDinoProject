from robot import Robot

class Fleet:

  def __init__(self):
      self.fleet_list = []
      self.create_fleet()

  def create_fleet(self):
    self.fleet_list.append(Robot("Bob", 120))
    self.fleet_list.append(Robot("Mecha-Godzilla", 75))
    self.fleet_list.append(Robot("Terminator", 90))


 


