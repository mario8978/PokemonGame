import random
from pokemon import *

NAMES = ["mario","julio","gary","harry","lorena","bruna","marcia"]

POKEMONS = [FirePokemon("charmander"), FirePokemon("charmilion"), FirePokemon("charizard"),
            EletricPokemon("pikachu"), EletricPokemon("maximun"), EletricPokemon("minum")]
class Person:

    def __init__(self,nome = None,pokemons = [],money = 100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NAMES)

        self.pokemons = pokemons

        self.money = money

    def __str__(self):
        return self.nome

    def showpokemons(self):
        if self.pokemons:
            print("{} pokemons".format(self))
            for i,pokemon in enumerate(self.pokemons):
                print("{} - {}".format(i,pokemon))

        else:
            print("{} doesn't have pokemon".format(self))

    def show_money(self):
        print("you have ${}".format(self.money))

    def make_money(self,amount_money):
        self.money += amount_money
        print("you won ${}".format(amount_money))
        self.show_money()

    def choose_pokemon(self):

        if self.pokemons:
            choose_poke = random.choice(self.pokemons)
            print("{} choose {}".format(self,choose_poke))
            return choose_poke

        else:
            print("this player doesn't have a pokemon to choose")


    def batlle(self,person):
        person.showpokemons()
        poke2 = person.choose_pokemon()

        poke1 = self.choose_pokemon()
        print("{} started a battle with {}".format(poke1,poke2))

        if poke1 and poke2:
            while True:
                victory = poke1.attack(poke2)
                if victory:
                    print("{} win the batlle".format(poke1))
                    self.make_money(poke2.level * 5)

                    break
                victory_enemy = poke2.attack(poke1)
                if victory_enemy:
                    print("{} win the batlle".format(poke2))
                    break
        else:
            print("this battle cannot take place")

        pass

class Player(Person):
    type = "person"

    def catch(self,pokemon):
        self.pokemons.append(pokemon)
        print("{} was captured".format(pokemon))

    def explore(self):
        chance = random.random()
        if chance <= 0.4:
            poke = random.choice(POKEMONS)
            print("a {} appeared".format(poke))

            choice = input("you want catch this pokemon?(Y/N)")
            if choice == "Y" or choice == "y":
                if poke.level * random.random() <= 50:
                    self.catch(poke)
                else:
                    print("the pokemon ran away ")
            else:
                print("ok, good trip")
        else:
            print("you didn't find anything")

    def choose_pokemon(self):
        self.showpokemons()

        if self.pokemons:
            while True:
                poke = input("choose a pokemon: ")

                try:
                    choose_poke = int(poke)
                    chosen_pokemon = self.pokemons[choose_poke]
                    print("{} i choose you!!!!".format(chosen_pokemon))
                    return chosen_pokemon
                except:
                    print("invalid command")

        else:
            print("this player doesn't have a pokemon to choose")


class Enemy(Person):
    type = "enemy"
    def __init__(self,nome=None,pokemons = None):
        if not pokemons:
            random_pokemons = []
            for i in range(random.randint(1,6)):
                random_pokemons.append(random.choice(POKEMONS))

            super().__init__(nome=nome,pokemons = random_pokemons)

        else:
            super().__init__(nome=nome,pokemons = pokemons)
