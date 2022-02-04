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
   
  def display_welcome(self):
      print("WELCOME TO THE BATTLE OF BEAST VS. MACHINE\n")
      print(" Battling for dominance over the universe")
      print(" are 3 dinosaurs and 3 robots. Who will win?") 
      print("    No one knows. Let's find out!") 

  def battle(self):
      
      robot = random.choice(self.fleet.fleet_list)   
      dinosaur = random.choice(self.herd.herd_list) 
      
      print("Robots are slow. Dinosaurs attack first!\n")
      
      self.dino_turn(dinosaur)
      self.show_dino_opponent_options()


      # print(f"Your robots remaining: {self.fleet.fleet_list}\n")* Make a for loop instead listing out the remaining names.
      # print(f"Your dinosaur's remaining: {self.herd.herd_list}") 
      
      press_one = input(" ")
      if press_one == 1:
        dinosaur.attack(robot)
      # else:
      #   print("Please press 1 to attack")
          
      # if robot.health <= 0:
      #   self.fleet.fleet_list.remove(robot)
      #   print(f"{robot} has been defeated!")

      # self.robot_turn(robot)
      # self.show_robot_opponent_options() 

      # press_one = input(" ")
      # if press_one == 1:
      #   robot.attack(dinosaur)
      # else:
      #   print("Please press 1 to attack")
      # if dinosaur.health <= 0:
      #   self.herd.herd_list.remove(dinosaur)
      #   print(f"{dinosaur} has been defeated!")

  def dino_turn(self, dinosaur):
        self.dinosaur = dinosaur
        print(f"It is now {dinosaur.name}'s turn to go")

  # def robot_turn(self, robot):
  #       self.robot = robot
  #       print(f"It is now {robot.name}'s turn to go ")
           
  def show_dino_opponent_options(self):
        print("Press 1 to attack")

  # def show_robot_opponent_options(self):
  #       print("Press 1 to attack")
                  
  # def display_winners(self):
  #     if len(self.fleet.fleet_list) <= 0:
  #       print("Arrrr! the Dinosaurs have won!")
  #       print("       GAME OVER")
  #     elif len(self.herd.herd_list) <= 0:
  #       print("Robots now rule the Universe!") 
  #       print("       GAME OVER")
  #           #end game
  #     else: 
  #       print("The battle rages on!")
  #       pass

  