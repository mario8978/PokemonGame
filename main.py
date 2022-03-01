import pickle
from pokemon import  *
from person import  *

def choose_starter_pokemon(person):
    while True:
        print("hello {}, now you must choose a starter pokemon for your journey".format(person))
        print("1 - charmander \n2- squirtle\n3- bulbasauro")

        poke = input("enter your choice: ")

        if poke == "1":
            newpoke= FirePokemon("charmander",level= 1)
            person.catch(newpoke)
            break
        elif poke == "2":
            newpoke = WaterPokemon("squirtle",level= 1)
            person.catch(newpoke)
            break

        elif poke == "3":
            newpoke = GrassPokemon("bulbasauro",level= 1)
            person.catch(newpoke)
            break

        else:
            print("you type it a invalid command, please type it again")


def save_game(player):
    try:
        with open("database.db","wb") as file:
            pickle.dump(player,file)
            print("Game saved")
    except Exception as error:
        print("sorry, open file error")
        print(error)

def load_game():
    try:
        with open("database.db","rb") as file:
            player = pickle.load(file)
            print("load game")
            return player
    except Exception as error:
        print("sorry, load error")
        print(error)

if __name__ == "__main__":
    player = load_game()

    if not player:
        print("------------------------------------------")
        name = input("welcome to the terminal pokemon game, what's your name?")
        player = Player(name)
        print("------------------------------------------")
        print("Hi {} ,this world is inhabited by pokemons ".format(name))
        player.show_money()

        if player.pokemons :
            print("oh you have some pokemons, congratulations")
        else:
            print("oh you haven't pokemons, you need chose your first pokemon")
            choose_starter_pokemon(player)

            print("now you have your first pokemon you must fight with you old enemy Carmelo")
            enemy = Enemy(nome = "Carmelo", pokemons=[FirePokemon("charmander",level= 1)])
            player.batlle(enemy)

    while True:
        print("------------------------------------------------")
        print("what do you want to do:\n1: explore\n2: battle with a enemy\n3: see your pokes\n0: exit game")
        choice = input()
        if choice == "1":
            player.explore()
            save_game(player)
        elif choice == "2":
            random_enemy = Enemy()
            player.batlle(random_enemy)
            save_game(player)
        elif choice == "3":
            player.showpokemons()
        elif choice == "0":
            print("left the game")
            break
