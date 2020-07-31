"""
METHOD:

string = "Abdullah Azzam Olcay"
string.method

-> method tanımını bu şekilde hatırlayabiliriz (TR)
-> This example is for remembering (EN)

-> Şimdide class methodlarını inceleyelim (TR)
-> Consider to method of class now. (EN)
"""
import random as rnd
import os

class Enemy():
    def __init__(self):
        self.health_situation = True  # The intial condition would be True (being alive)
        self.health = rnd.randint(30,70) # generate a number in interval of 30 and 70
        self.defence = rnd.randint(0,10)
        self.power = rnd.randint(20,50)

    # Part of operation (The enemy attacked to me)

    def attack(self,me): # We can invoke the Me() class in the enemy class
        damage = self.power - me.defence
        me.health -= damage
        if me.health <= 0:
            me.health_situation = False # I am dead


class Me():
    def __init__(self):
        self.health_situation = True # The intial condition would be True (being alive)
        self.health = 500 # This number is a constant number
        self.defence = 20
        self.power = 55

    # Part of operation (I attacked to enemy)

    def attack(self,enemy):
        damage = self.power - enemy.defence
        enemy.health -= damage
        if enemy.health <=0:
            enemy.health_situation = False # Enemy is dead
            enemies.remove(enemy)

# We created 'n' enemies
n = int(input("Enter a enemies' number, how many you want"))

enemies = list() # I want to create 10 enemies against to me
for i in range(n):
    enemies.append(Enemy()) # We can append an enemy in this way

# We invoke to class for me
me = Me()


while True:
    os.system("clear")
    # preference of me
    print("ME:\nhealth:{}\ndefence:{}\npower:{}\n".format(me.health,me.defence,me.power))
    # If my health situation is False, its mean that I died
    if me.health_situation == False:
        print("Game Over")
        quit()
    # If all of the enemies are dead, we would win
    if not enemies:
        print("You win")
        quit()

    # n pieces of enemies write in below
    for i in enemies:
        print("{}. Enemy:\nhealth:{}\ndefence:{}\npower:{}\n".format(enemies.index(i),i.health,i.defence,i.power))

    # I can select the enemy, then I attack to enemy
    selection = int(input("Select enemy"))
    enemy = enemies[selection]
    me.attack(enemy)

    # If enemy is here, we can do this operation
    if enemies:
        attack_of_enemy = enemies[rnd.randint(0,len(enemies) - 1)]
        attack_of_enemy.attack(me)

