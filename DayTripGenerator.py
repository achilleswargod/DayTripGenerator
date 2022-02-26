import random

# Lists
destinations = ['Killeen', 'Austin', 'Waco', 'Belton', 'Temple']
restaurants = ['Ghengis Grill', 'Taqueria', 'Cheesecake Factory']
transportation = ['Car', 'Uber', 'Bus']
entertainment = ['Arcade', 'Top Golf', 'Mall']

# functions


def get_destination():
    place = random.choice(destinations)
    return place


def get_food():
    food = random.choice(restaurants)
    return food


def get_ride():
    ride = random.choice(transportation)
    return ride


def get_entertainment():
    mode = random.choice(entertainment)
    return mode


print("Welcome to the Day Trip Generator! If you don't know what to do for the day, I have you covered! First things first, Im going to choose a destination for you. ")
# Loops
choosing_destination = True
while choosing_destination is True:

    chosen_destination = get_destination()
    choice = input(
        f"We chose {chosen_destination} as tonights destination. Do you like where you're going? y/n: ")

    if choice == 'y':
        choosing_destination = False
        print("Awesome! Next we will choose where you'll be dining.")
    else:
        print("Oops we meant to choose another destination for you.")

choosing_food = True
while choosing_food is True:
    chosen_food = get_food()
    choice = input(
        f"We have chosen {chosen_food} for tonights restaurant, do you like this idea? y/n: ")

    if choice == 'y':
        choosing_food = False
        print("Awesome, now we'll choose your method of transportation.")
    else:
        print("We don't like their food either, lets pick again.")

choosing_ride = True
while choosing_ride is True:
    chosen_ride = get_ride()
    choice = input(
        f"We have chosen {chosen_ride} as your method of transportation, Do you feel comfortable traveling this way? y/n: ")

    if choice == 'y':
        choosing_ride = False
        print("Awesome, now for the last item on our list we will choose tonights entertainment!")
    else:
        print("Oops, our mistake. We shall choose another.")

choosing_entertainment = True
while choosing_entertainment is True:
    chosen_entertainment = get_entertainment()
    choice = input(
        f"We have chosen {chosen_entertainment}, Does this sound like a good place to have fun? y/n: ")

    if choice == 'y':
        choosing_entertainment = False
        print("Awesome! Lets move on!")
    else:
        print("Perhaps another night then, lets try something else.")


choice_confirmation = True
while choice_confirmation is True:
    print(f"So you are going to {chosen_destination} to eat at the {chosen_food}. You will be arriving by {chosen_ride}. To top off the night you'll be going to {chosen_entertainment} for a bit of fun.")

    choice = input("Is this what you would like to do today?: y/n ")

    if choice == 'y':
        choice_confirmation = False
        print("Awesome! Have a great day!")
    else:
        print("Im sorry, I didn't happen to think this far ahead.")
