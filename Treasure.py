import random


#email  osmundehi@gmail.com

# create functions for each levels of difficulty
def easy():
    #hard point: cross road
    #ask for direction input
    cross_road = input(
        "\nYou're at a cross road. Where do you want to go? Type \"left\" or \"right\":  "
    ).lower()
    #create variable for direction input and add the 2 possible direction and create a random variable and create variable to hold random result.
    random_road = ["left", "right"]
    if cross_road == random.choice(random_road):
        lake = input(
            "\nYou've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across:  "
        ).lower()
        if lake == "wait":
            house_colour = input(
                "\nYou arrive at the island unharmed. There is a house with 3 doors. One \"red\", one \"yellow\" and one \"blue\". Which colour do you choose?:  "
            ).lower()
            if house_colour == "red":
                print("\nYou were eaten by beasts. Game over.")
            elif house_colour == "blue":
                print("\nYou burned by fire. Game over.")
            elif house_colour == "yellow":
                print(
                    "\nYou Win! Just because its easy.\nThink otherwise? Play Medium and lose!!!"
                )
            else:
                print("\nGame Over.")
        else:
            print("\nYou get attacked by an angry trout. Game over.")
    else:
        print("\nYou fell into a hole. Game over.")


def medium():
    #hard point: cross road, lake
    #ask for direction input
    cross_road = input(
        "\nYou're at a cross road. Where do you want to go? Type \"left\" or \"right\":  "
    ).lower()
    #create variable for direction input and add the 2 possible direction and create a random variable and create variable to hold random result.
    random_road = ["left", "right"]
    if cross_road == random.choice(random_road):
        lake = input(
            "\nYou've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across:  "
        ).lower()
        random_lake = ["wait", "swim"]
        lake_result = random.choice(random_lake)

        #compare lake and wait and proceed to color determination
        if lake == lake_result:
            house_colour = input(
                "\nYou arrive at the island unharmed. There is a house with 3 doors. One \"red\", one \"yellow\" and one \"blue\". Which colour do you choose?:  "
            ).lower()
            if house_colour == "red":
                print(
                    "\nYou were eaten by beasts. Game over. \n Hahaha!!! Try again sucker!"
                )
            elif house_colour == "blue":
                print(
                    "\nBurned by fire. Game over.\n Hahaha!!! Try again sucker!"
                )
            elif house_colour == "yellow":
                print(
                    "\nYou Win! And you deserve your treasure. \nHowever win more or lose it all when you play Hard."
                )
            else:
                print("\nGame Over. \n Hahaha!!! Try again sucker!")

        #if lake(user input) is not equal to to lake_result(random variable) do the following conditions and use else condition if wrong input by the user
        elif lake == "wait" and lake_result == "swim":
            print(
                "A bear killed you while waiting. Game over. \n Hahaha!!! Try again sucker!"
            )
        elif lake == "swim" and lake_result == "wait":
            print(
                "You were swallowed by a whale. Game Over! \n Hahaha!!! Try again sucker!"
            )
        else:
            print(
                "You were captured by Pirates because you did not follow instructions. \n Hahaha!!! Try again sucker!"
            )
    else:
        print(
            "\nYou fell into a hole. Game over. \n Hahaha!!! Try again sucker!"
        )


def hard():
    #hard point: cross road, lake, lake live or die,
    #ask for direction input
    cross_road = input(
        "\nYou're at a cross road. Where do you want to go? Type \"left\" or \"right\":  "
    ).lower()
    #create variable for direction input and add the 2 possible direction and create a random variable and create variable to hold random result.
    random_road = ["left", "right"]
    if cross_road == random.choice(random_road):
        lake = input(
            "\nYou've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across:  "
        ).lower()
        random_lake = ["wait", "swim"]
        lake_result = random.choice(random_lake)

        #check if input and the random variable are the same, create a random variable to determine to live or die and create variable to hold random result.
        if lake == lake_result:
            live_die = ["live", "die"]
            live_die_result = random.choice(live_die)

            # if random variable(live_die_result) is "live" ask for color input and create variable for and to hold random result
            if live_die_result == "live":
                house_colour = input(
                    "\nYou arrive at the island unharmed. There is a house with 3 doors. One \"red\", one \"yellow\" and one \"blue\". Which colour do you choose?:  "
                ).lower()
                if house_colour == "red":
                    print(
                        "\nYou were eaten by beasts. Game over. \n Hahaha!!! Try again sucker! "
                    )
                elif house_colour == "blue":
                    print(
                        "\nYou burned by fire. Game over. \n Hahaha!!! Try again sucker!"
                    )
                elif house_colour == "yellow":
                    print(
                        "\nYou Win! And you deserve your treasure. \n Become Immortal by wining INSANE, all Kings and Pirates would bow at your feet."
                    )
                else:
                    print("\nGame Over. \n Hahaha!!! Try again sucker!")

            # if random variable(live_die_result) is not "live" use elif conditions, use lake variable to determine the the coresponding response
            elif live_die_result == "die" and lake == "swim":
                print(
                    "Almost at the Island but you were exhausted and drowned. Tough luck, Game Over!"
                )
            elif live_die_result == "die" and lake == "wait":
                print(
                    "Almost at the Island but you were attacked and drowned by Pirates. Tough luck, Game Over!"
                )

        #if lake(user input) is not equal to to lake_result(random variable) do the following conditions and use else condition if wrong input by the user
        elif lake == "wait" and lake_result == "swim":
            print(
                "A bear killed you while waiting. Game over.\n Hahaha!!! Try again"
            )
        elif lake == "swim" and lake_result == "wait":
            print(
                "You were swallowed by a whale. Game Over!\n Hahaha!!! Try again"
            )
        else:
            print(
                "You were captured by Pirates because you did not follow instructions.\n Hahaha!!! Try again"
            )

    #else if the user input is wrong direction or the input and random choice are not the same.
    else:
        print("You fell into a hole. Game Over!")


def insane():
    #ask for direction input
    cross_road = input(
        "\nYou're at a cross road. Where do you want to go? Type \"left\" or \"right\":  "
    ).lower()
    #create variable for direction input and add the 2 possible direction and create a random variable and create variable to hold random result.
    random_road = ["left", "right"]
    if cross_road == random.choice(random_road):
        lake = input(
            "\nYou've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across:  "
        ).lower()
        random_lake = ["wait", "swim"]
        lake_result = random.choice(random_lake)

        #check if input and the random variable are the same, create a random variable to determine to live or die and create variable to hold random result.
        if lake == lake_result:
            live_die = ["live", "die"]
            live_die_result = random.choice(live_die)

            # if random variable(live_die_result) is "live" ask for color input and create variable for and to hold random result
            if live_die_result == "live":
                house_colour = input(
                    "\nYou arrive at the island unharmed. There is a house with 3 doors. One \"red\", one \"yellow\" and one \"blue\". Which colour do you choose?:  "
                ).lower()
                random_house = ["blue", "yellow", "red"]

                house = random.choice(random_house)

                #if color input and and house variable are same
                if house_colour == house:
                    print(
                        "\nYou have come a long way and won the prize. \nYou became Immortal and here are your treasures!\n"
                    )
                    print('''
**************************************************************************
                                                                o .,<>., o
                                                                |\/\/\/\/|
                                                                '========'
                                                                (_ SSSSSSs
                                                                )a'`SSSSSs
                                                               /_   SSSSSS
                                                               .=## SSSSS
                                                               .####  SSSSs
                                                               ###::::SSSSS
                                                              .;:::""""SSS
                                                             .:;:'  . .  \\
                                                            .::/  '     .'|
                                                           .::( .         |
                                                           :::)           \
                                                           /\(            /
                                                          /)            ( |
                                                        .'  \  .       ./ /
                                                     _-'    |\  .        |
                                   _..--..   .  /"---\      | ` |      . |
           -=====================,' _     \=(*#(7.#####()   |  `/_..   , (
                       _.-''``';'-''-) ,.  \ '  '+/// |   .'/   \  ``-.) \
                     ,'  _.-  ((    `-'  `._\    `` \_/_.'  )    /`-._  ) |
                   ,'\ ,'  _.'.`:-.    \.-'                 /   <_L   )"  |
                 _/   `._,' ,')`;  `-'`'                    |     L  /    /
                / `.   ,' ,|_/ / \                          (    <_-'     \
                \ / `./  '  / /,' \                        /|`         `. |
                )\   /`._   ,'`._.-\                       |)            \'
               /  `.'    )-'.-,' )__)                      |\            `|
              : /`. `.._(--.`':`':/ \                      ) \             \
              |::::\     ,'/::;-))  /                      ( )`.            |
              ||:::::  . .::':  :`-(                       |/    .          |
              ||::::|  . :|  |==[]=:                       .        -       \
              |||:::|  : ||  :  |  |                      /\           `     |
  ___ ___     '|;:::|  | |'   \=[]=|                     /  \                \
 |   /_  ||``|||:::::  | ;    | |  |                     \_.'\_               `-.
 :   \_``[]--[]|::::'\_;'     )-'..`._                 .-'\``:: ` .              \
  \___.>`''-.||:.__,'     SSt |_______`>              <_____:::.         . . \  _/
***********************************************************************************
''')
                elif house_colour != house:
                    doom = [
                        "\nYou came all this way to feed your flesh to the beasts.\nGame Over and dont ever comeback!!!",
                        "\nYou came all this way to be burned by fire.\nGame Over and dont ever comeback!!!",
                        "\nYou came all this way to be trapped in a prison.\nGame Over and dont ever comeback!!!"
                    ]
                    print(random.choice(doom))
                else:
                    print(
                        "\nYou came all this way to be trapped in a prison.\nGame Over and dont ever comeback!!!"
                    )

            # if random variable(live_die_result) is not "live" use elif conditions, use lake variable to determine the the coresponding response
            elif live_die_result == "die" and lake == "swim":
                print(
                    "Almost at the Island but you were exhausted and drowned. Tough luck.\nGame Over and dont ever comeback!!!"
                )
            elif live_die_result == "die" and lake == "wait":
                print(
                    "Almost at the Island but you were attacked and drowned by Pirates. Tough luck.\nGame Over and dont ever comeback!!!"
                )

        #if lake(user input) is not equal to to lake_result(random variable) do the following conditions and use else condition if wrong input by the user
        elif lake == "wait" and lake_result == "swim":
            print(
                "A bear killed you while waiting.\nGame Over and dont ever comeback!!!"
            )
        elif lake == "swim" and lake_result == "wait":
            print(
                "You were swallowed by a whale.\nGame Over and dont ever comeback!!!"
            )
        else:
            print(
                "You were captured by Pirates because you did not follow instructions.\nGame Over and dont ever comeback!!!"
            )

    #else if the user input is wrong direction or the input and random choice are not the same.
    else:
        print("You fell into a hole.\nGame Over and dont ever comeback!!!")


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

#functions and while loop checks for user error and ask for a correct input before comparing variables
def t_game():
    print('''
    ***************************************************************************
    *                        Welcome to Treasure Island.                      *
    *                    Your mission is to hunt for the Treasure.            *
    *                            Be warned, you might                         *
    *                          be the hunted as well!!!                       *
    ***************************************************************************
    ''')
    level = input(
        "\nChoose your difficulty level: Type \"easy\", \"medium,\" \"hard\" or \"insane\":  "
    ).lower()
    while level not in ["easy", "medium", "hard", "insane"]:
        level = input(
            "Invalid input. Please choose a valid difficulty level: ").lower()

    print("Let the game begin!")

    if level == "easy":
        easy()
    elif level == "medium":
        medium()
    elif level == "hard":
        hard()
    else:
        insane()


#while loop`to restart the program or terminte if user exit
while True:
    t_game()
    play_again = input(
        "\nDo you want to play again? Type 'Y' or 'N': ").lower()
    if play_again != 'y':
        print("Only the toughest play!!!")
        break
