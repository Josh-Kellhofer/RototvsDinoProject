from weapon import Weapon

class Robot:

  def __init__(self, name, health):
    self.name = name
    self.health = health
    self.weapon = Weapon("stapler", 25)

  def attack(self, dinosaur):
    dinosaur.health -= self.weapon.attack_power
    print("You hit for 25 damage with your stapler\n")
    

  
      

  
  
       

      


 

  