import random

# Lists
destinations = ['Killeen', 'Austin', 'Waco', ]
restaurants = ['Ghengis Grill', 'Taqueria', 'Cheesecake Factory']
transportation = ['Car', 'Uber', 'Bus']
entertainment = ['Arcade', 'Top Golf', 'Mall']


food = random.choice(restaurants)
ride = random.choice(transportation)
mode = random.choice(entertainment)


def get_destination(answer):
    if answer == 'y':
        place = random.choice(destinations)
        print(place)
    else:
        print("Oops lets choose another destination for you")


yes = get_destination('y')
no = get_destination('n')
choosing = True

while choosing is True:
    # print("Welcome to the Day Trip Generator! If you don't know what to do for your trip I have you covered! First things first, Im going to choose a destination for you.")

    choice = input("Do you like where you're going? y/n: ")
    if choice == 'y':
        print(yes)
    elif choice == 'n':
        choosing = False
        print(no)
