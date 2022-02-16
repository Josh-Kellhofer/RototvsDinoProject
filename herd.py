from dinosaur import Dinosaur

class Herd:

  def __init__(self):
      self.herd_list = []
      self.create_herd()

  def create_herd(self):
    self.herd_list.append(Dinosaur("Mary", 120))
    self.herd_list.append(Dinosaur("Godzilla", 75))
    self.herd_list.append(Dinosaur("T-Rex", 90))
  


