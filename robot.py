from weapon import Weapon

class Robot:

  def __init__(self, name, health):
    self.name = name
    self.health = health
    self.weapon = Weapon("stapler", 25)

  def attack(self, dinosaur):
    self.dinosaur = dinosaur
    print(f"You hit {dinosaur} for 25 damage with your stapler")
    dinosaur.health -= 25

  
      

  
  
       

      


 

  