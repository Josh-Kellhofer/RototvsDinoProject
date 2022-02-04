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
      print(" are 3 dinosaurs and 3 robots. Who will win") 
      print("    No one knows. Let's find out!") 

  def battle(self):
      print(f"Your dinosaur's remaining: {Herd}")
      print(f"Your robots remaining: {Fleet}")

      print("Robots are slow. Dinosaurs attack first!\n")
      robot = random.choice(self.fleet.fleet_list)   
      dinosaur = random.choice(self.herd.herd_list)   
      dino_turn
      show_dino_opponent_options

      
      press_one = input(" ")
      if press_one == 1:
        dinosaur.attack(robot)
      else:
        print("Please press 1 to attack")
      if robot.self.health <= 0:
        Fleet.self.list.remove(robot)
        print(f"{robot} has been defeated!")

        self.robot_turn
        self.show_robot_opponent_options
      
      press_one = input(" ")
      if press_one == 1:
        robot.attack
      else:
        print("Please press 1 to attack")
      if dinosaur.self.health <= 0:
        Herd.self.list.remove(dinosaur)
        print(f"{dinosaur} has been defeated!")

    
        def dino_turn(self, dinosaur):
            self.dinosaur = dinosaur
        print("It is now {dinosaur}'s turn to go")

        def robo_turn(self, robot):
            self.robot = robot
        print("It is now {robot}'s turn to go ")

        def show_dino_opponent_options(self):
            print("Press 1 to attack")

        def show_robo_opponent_options(self):
            print("Press 1 to attack")
    

        def display_winners(self):
            if len(Fleet.self.list) <= 0:
                print("Arrrr! the Dinosaurs have won!")
            elif len(Herd.self.list) <= 0:
                print("Robots now rule the Universe!") 
            #end game
            else: 
                print("The battle rages on!")
            pass

  