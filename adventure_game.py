import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You are Harry Potter and couple of your closest friends, "
    "Hermione and Ron.")
    print_pause("This night you decide to take Sorcerer’s Stone, "
    "which helps you to fight with evil.")
    print_pause("You found that there is some trapdoor in the room "
    "with giant dog in the castle, that could leads to the stone.")
    print_pause("You played with magic flute and after dog felt asleep "
    "you jumped into trapdoor in the floor behind the dog.")
    print_pause("You are falling down, down and down.")

def make_choice():
    print_pause("Please enter 1 or 2")

def wrong_choice():
    print_pause("I'm sorry, I don't understand. Please enter 1 or 2")

def wrong_choice_again():
    print_pause("Unfortunately, your choice still is not clear and "
    "we have to stop this journey.")

def end_story():
    print_pause("The end!")
    print_pause("You can try to play later again.")


def task1_choice1():
    print_pause("This is Devil’s Snare!")
    print_pause("The more you strained against it, "
    "the tighter and faster the plant wound around you.")
    print_pause("The plant is curling around your neck, "
    "you cannot breeze and unfortunately, you are dying.")

def task1_choice2():
    print_pause("This is Devil’s Snare!")
    print_pause("2.	You whipped out your wand, waved it, "
    "muttered something, and sent a jet of the bluebell flames.")
    print_pause("In a matter of seconds, you felt loosening its grip "
    "as it cringed away from the light and warmth.")
    print_pause("Wriggling and flailing, it unraveled itself "
    "from their bodies, and you are able to pull free.")

def task1():
    print_pause("Suddenly you landed on something soft, some sort of plant.")
    print_pause("The moment you had landed, the plant had started "
    "to twist snakelike tendrils around your body.")
    choice = input("1.	You decide to pull the plant off your body.\n"
    "2.	You decide to say a spell.")
    print_pause("What are you going to do?")
    make_choice()
    if choice == "1":
        task1_choice1()
    elif choice == "2":
        task1_choice2()
    else:
        wrong_choice()
        if choice == "1":
            task1_choice1()
        elif choice == "2":
            task1_choice2()
        else:
            wrong_choice_again()
            end_story()

intro()

task1()
