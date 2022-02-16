import random
from fleet import Fleet
from herd import Herd


class Battlefield:

  def __init__(self):
    self.fleet = Fleet()
    self.herd = Herd()
    
  def run_game(self):
    
    self.display_welcome()
    self.battle()
    battle_on = True
    while battle_on:
        if len(self.fleet.fleet_list) > 0 and len(self.herd.herd_list) > 0:
          self.battle()
        else:
          self.display_winners()
          battle_on = False
   
  def display_welcome(self):
      print("WELCOME TO THE BATTLE OF BEAST VS. MACHINE\n")
      print(" Battling for dominance over the universe")
      print(" are 3 dinosaurs and 3 robots. Who will win?") 
      print(" ***********************************")
      print("    No one knows. Let's find out!\n") 
      print("Robots are slow. Dinosaurs attack first!\n")

  def battle(self):
      
      robot = random.choice(self.fleet.fleet_list)   
      dinosaur = random.choice(self.herd.herd_list) 
                 
      self.dino_turn(dinosaur)
      self.show_dino_opponent_options()
      press_one = input("")
      dinosaur.attack(robot)

      if len(self.fleet.fleet_list)>0:
        self.robot_turn(robot)
        self.show_robot_opponent_options()
      else:
        self.display_winners()
   

      if robot.health <= 0:
        self.fleet.fleet_list.remove(robot)
        print(f"{robot.name} has been defeated!")

      press_one = input(" ")
      if press_one == "1":
        robot.attack(dinosaur)
       
      
      if dinosaur.health <= 0:
        self.herd.herd_list.remove(dinosaur)
        print(f"{dinosaur.name} has been defeated!")

  def dino_turn(self, dinosaur):
        print(f"It is now {dinosaur.name}'s turn to go")

  def robot_turn(self, robot):
        print(f"It is now {robot.name}'s turn to go ")
           
  def show_dino_opponent_options(self):
        print("Press 1 to attack")

  def show_robot_opponent_options(self):
        print("Press 1 to attack")
                  
  def display_winners(self):
      if len(self.fleet.fleet_list) <= 0:
        print("Arrrr! the Dinosaurs have won!")
        print("       GAME OVER")
      elif len(self.herd.herd_list) <= 0:
        print("Robots now rule the Universe!") 
        print("       GAME OVER")
      
      

  