import time
import os
import wikipedia



def menu():
    global name
    os.system('cls')
    name = input("Enter your name: ")
    main()


def main():
    os.system('cls')
    print("Hello "+str(name)+" choose from the options below...")
    opt = int(input('''
            
            1) start
            2) help
            3) exit

            enter the option number- '''))

    if opt == 1:
        start()
    elif opt == 2:
        help()
    elif opt == 3:
        exit()
    else:
        input("no such option, press enter...")
        menu()


def start():
    os.system('cls')
    input('''
            Animals present are-
            
             Dog
             Cow
             Lion
             Bear
             Monkey
             Eagle
             Crocodile

            Choose any animal from the list in your mind and press enter...''')
    habitat()


def habitat():
    os.system('cls')
    global place
    placee = int(input('''
                
                From where does your animal belongs?
                1) Land
                2) Water
                3) Tree
                4) Air
                
                Enter the option's digit: '''))
    
    if placee == 1:
        place = "land"
        eating()
    elif placee == 2:
        place = "water"
        eating()
    elif placee == 3:
        place = "tree"
        eating()
    elif placee == 4:
        place = "air"
        eating()
    else:
        input("Option not present, press enter...")
        habitat()

def eating():
    os.system('cls')
    global food
    foode = int(input('''
                        
                Is your animal--

                1) Carnivorous
                2) Omnivorous
                3) Herbivorous
                
                Enter the option's digit: '''))

    if foode == 1:
        food = "carnivorous"
        living()
    elif foode == 2:
        food = "omnivorous"
        living()
    elif foode == 3:
        food = "herbivorous"
        living()
    else:
        input("Option not present, press enter...")
        eating()


def living():
    os.system('cls')
    global nature
    natre = int(input('''
                
                Which category does your animal belongs to?

                1) Domestic
                2) Wild
                3) Both

                Enter the option's digit: '''))

    if natre == 1:
        nature = "domestic"
        compare()
    elif natre == 2:
        nature = "wild"
        compare()
    elif natre == 3:
        nature = "both"
        compare()
    else:
        input("Option not present, press enter...")
        living()



def help():
    os.system('cls')
    print("Hello "+str(name)+" some steps you need to follow are...")
    print('''
            1) In the main menu, simply click on start.
            2) On your screen, names of some animals would be displayed.
            3) Select any animal in your mind and enter the corresponding digit of the animal you have chosen.
            4) Hit enter and in the next few menus, you would be asked some questions.
            5) You need to answer them and at last, it will try to determine the animal you thought.
            6) If the answer was right, hit enter and play again.
            7) If the answer was wrong, write the animal name and we will remember it next time.
            ''')
    input("Press enter to continue...")
    main(name)


def compare():
    os.system('cls')
    if place == "land":
        if food == "carnivorous":
            if nature == "wild":
                ask = input("Is your animal LION?(y/n): ")
                if ask == "y":
                    print("yess, I succeded in reading your mind.")
                    input("press enter to return to main menu...")
                    main()
                elif ask == "n":
                    print("ohh so sad, I failed in reading your mind.")
                    no = input("Can you enter the name of your animal please- ")
                    print("Thanks for your contribution, we will remember it next time.")
                    my_file = open("animal.txt","w+")
                    my_file.write("the name of land, wild and carnivorous animal is " +str(no))
                else:
                    input("Option not present, press enter...")
                    main()
            elif nature == "domestic":
                input("Matching animal is Dog which is omnivorous, press enter...")
                main()
            elif nature == "both":
                input("Matching animal is Dog which is omnivorous, press enter...")
                main()
        elif food == "herbivorous":
            if nature == "domestic":
                ask = input("Is your animal COW?(y/n): ")
                if ask == "y":
                    print("yess, I succeded in reading your mind.")
                    input("press enter to return to main menu...")
                    main()
                elif ask == "n":
                    print("ohh so sad, I failed in reading your mind.")
                    no = input("Can you enter the name of your animal please- ")
                    print("Thanks for your contribution, we will remember it next time.")
                    my_file = open("animal.txt","w+")
                    my_file.write("the name of land, domestic and herbivorous animal is " +str(no))
                else:
                    input("Option not present, press enter...")
                    main()
            elif nature == "wild":
                input("No such animals in list, press enter...")
                main()
            elif nature == "both":
                ask = input("Is your animal COW?(y/n): ")
                if ask == "y":
                    print("yess, I succeded in reading your mind.")
                    input("press enter to return to main menu...")
                    main()
                elif ask == "n":
                    print("ohh so sad, I failed in reading your mind.")
                    no = input("Can you enter the name of your animal please- ")
                    print("Thanks for your contribution, we will remember it next time.")
                    my_file = open("animal.txt","w+")
                    my_file.write("the name of land, domestic and herbivorous animal is " +str(no))
                else:
                    input("Option not present, press enter...")
                    main()
        elif food == "omnivorous":
            if nature == "wild":
                ask = input("Is your animal BEAR?(y/n): ")
                if ask == "y":
                    print("yess, I succeded in reading your mind.")
                    input("press enter to return to main menu...")
                    main()
                elif ask == "n":
                    print("ohh so sad, I failed in reading your mind.")
                    no = input("Can you enter the name of your animal please- ")
                    print("Thanks for your contribution, we will remember it next time.")
                    my_file = open("animal.txt","w+")
                    my_file.write("the name of land, wild and omnivorous animal is " +str(no))
                else:
                    input("Option not present, press enter...")
                    main()
            elif nature == "domestic":
                input("No such animal in the list, press enter...")
                main()
            elif nature == "both":
                input("No such animal in the list, press enter...")
                main()
    elif place == "water":
        if food == "carnivorous":
            if nature == "wild":
                print("The only such animal present in the list is crocodile")
                print("Yuhoo!! I won...")
                main()
            else:
                print("No such animal is the list, press enter...")
                main()
        else:
            print("No such animal in the list, press enter...")
            main()
    elif place == "tree":
        if food == "herbivorous":
            if nature == "wild":
                print("The only such animal in the list is Monkey")
                print("Yuhoo!! I won...")
                main()
            else:
                print("No such animals in the list, press enter...")
                main()
        elif food == "carnivorous":
            print("Matching animal is Eagle which lives in Air.")
            main()
        else:
            print("No such animals in the list, press enter...")
            main()
    elif place == "air":
        if food == "carnivorous":
            if nature == "wild":
                print("The only such animal present in list is Eagle.")
                print("Yuhoo!! I won...")
                main()
            elif nature == "both":
                print("The matching animal is Eagle, No such animals in the list.")
                main()
            elif nature == "domestic":
                print("The matching animal is eagle which is not usually tamed.")
                main()
        else:
            print("No such animal found in the list, press enter...")
            main()



menu()