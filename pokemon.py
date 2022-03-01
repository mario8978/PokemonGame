import random

class Pokemon:

    def __init__(self,specie,level=None):
        self.specie = specie
        if level:
            self.level = level
        else :
            self.level = random.randint(1,100)

        self.life = self.level * 10
        self.damage = self.level * 2


    def __str__(self):
         return "{} {}".format(self.specie,self.level)

    def attack(self,enemy):
        real_damage = int((self.damage * random.random() * 1.4))
        enemy.life = enemy.life - real_damage
        print("{} lost {} of life".format(enemy,real_damage))

        if enemy.life <= 0:
            print("{} lost the battle".format(enemy))
            return True
        elif self.life <= 0:
            return False

class EletricPokemon(Pokemon):
    type = "eletric"

    def attack(self,enemy):

        print("{} launched a thunder shock into the {} !!".format(self,enemy))
        return super().attack(enemy)
class FirePokemon(Pokemon):
    type = "fire"

    def attack(self,enemy):
        print("{} launched a fire ball into the {} !!".format(self,enemy))
        return super().attack(enemy)


class WaterPokemon(Pokemon):
    type = "water"

    def attack(self,enemy):
        print("{} launched a water gun into the {} !!".format(self,enemy))
        return super().attack(enemy)


class GrassPokemon(Pokemon):
    type = "grass"

    def attack(self,enemy):
        print("{} launched a razor leaf into the {} !!".format(self,enemy))
        return super().attack(enemy)
