from sys import exit
from random import randint
#dedent allows us to use the """ quotations and strips teh wite space from the begining of a line.
#from textwrap import dedent - could use this. 
herohp = 20

def combat_zone():
    print("You have found yourself facing gorgons... how will you test yourself?")
    
    choice = input("random or 3man fight?")
    
    if choice == "random":
        print("test")
    elif choice == "3man":
        for num in range(3):
            print(num)
            combat()
    else:
        print("errr")
    menu()

def combat():
    #set hp for both parties
    gorgon = 20
    hero = herohp
    #hero xp open the file and prep the value
    heroxp_file = open('heroxp.txt','r')
    heroxp = int(heroxp_file.read())
    heroxp_file.close()
    #goron wins open the file and prep the value
    gorgon_file = open('gorgon.txt','r')
    gorgon_wins = int(gorgon_file.read())
    gorgon_file.close()
    #hero wins opens the file and prep the value
    hero_file = open('hero.txt','r')
    hero_wins = int(hero_file.read())
    hero_file.close()

    while hero > 0 and gorgon > 0:
        turn = randint(1,2)
        roll = randint(1,20)
        input("\nPress any key for next attack\n")
        if roll <= 5:
            damage = 0
            print("Miss")
        elif roll >= 6 and roll < 16:  
            damage = randint(1,9)
            print("normal strike!")
        elif roll > 15 and roll <20:
            damage = randint(1,9) * 1.5
            print("beautiful strike!!")
        elif roll == 20:
            damage = randint(1,9) * 2
            print("Critical!")
        if turn == 1:
            #code makes sure XP does not inflence a miss which should equal zero. 
            if roll <=5:
                gorgon = gorgon - (damage)
                print(f"Hero does {damage} damage to Gorgon")
                print(f"new health for gorgon >>{gorgon}<<")
            elif roll > 5:
                print(f"Hero does {damage + heroxp} damage to Gorgon")
                gorgon = gorgon - (damage + heroxp)
                print(f"new health for gorgon >>{gorgon}<<")
        if turn == 2:
            print(f"Gorgon does {damage} damage to Hero")
            hero = hero - damage
            print(f"new health for hero: >>{hero}<<")
    input("\nWE HAVE A WINNER")
    if gorgon > hero:
        print("gorgon wins and you brave warrior are consigned to ashes")
        gorgon_file = open('gorgon.txt','w+')
        gorgon_file.truncate()
        gorgon_wins = (gorgon_wins + 1)
        gorgon_print = str(gorgon_wins)
        gorgon_file.write(gorgon_print)
        gorgon_file.close()

        menu()
    else:
        print("hero wins!")
        print(hero)
        hero +=10
        print(hero)
        #reopens heroxp file in write mode
        xpwins = open('heroxp.txt','w+')
        #wipes previous value in file
        xpwins.truncate()
        #takes hero xp and increments
        heroxp = (heroxp + 1)
        #converts to string to reload to txt file.
        hero_print = str(heroxp)
        #hero_print is the writen then we close the file.
        xpwins.write(hero_print)
        xpwins.close()
        #calculate wins now. 
        hero_file = open('hero.txt','w+')
        hero_file.truncate()
        hero_wins = (hero_wins + 1)
        hero_wins_print = str(hero_wins)
        hero_file.write(hero_wins_print)
        hero_file.close()

 #   menu()

def menu():
    choice = input("fight | run | cheat | check >> ")
    choice = choice.lower()
    if choice == "fight":
        combat_zone()
    elif choice == "run":
        print(f"you had Hero XP. Wuss baby")
    elif choice == "cheat":
        #need to figure something out to boost
        menu()
    elif choice == "check":
        #check needs to be completed
        print(herohp)
        menu()
    elif choice == "quit":
        exit(0)
    else:
        print("code fail")

menu()
