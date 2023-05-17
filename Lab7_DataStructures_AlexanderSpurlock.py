# Name: Alexander Spurlock
# Date: 10/22/2022
# Project: Lab 7 - Data Structures

user_options = {
    1: 'Add',
    2: 'Remove',
    3: 'Display',
    4: 'Exit'
}

candy_list = [
    'Take 5', 'Snickers', 'KitKat', 'Twix', 'Reese\'s', 'Hershey\'s'
]

def user_options_menu():
    """
    Display the menu dictionary in a pretty way.
    """
    print("\n-- MENU --")
    for obj in user_options:
        print(obj, ' - ', user_options[obj])
    print('\nWould you like to add (1), remove (2), re-list (3), or exit (4)?: ')


def display_candy_list():
    """
    Display the candy list in a pretty way.
    """
    print("\n-- CANDY LIST --")
    print(', '.join(candy_list))


def is_in_list(input: str) -> bool:
    """
    Check if the candy is in the list.
    """
    for candy in candy_list:
        if input.casefold() == candy.casefold():
            return True
    return False


def add(input: str):
    """
    Add a candy to the list, if it's not already in the list.
    """
    if not is_in_list(input):
        candy_list.append(input)
        print(input + ' added!')
    else:
        print(input + ' is already in the candy list! Not added.')


def remove(input: str):
    """
    Remove a candy from the list, if it's in the list.
    """
    if is_in_list(input):
        for candy in candy_list:
            if candy.casefold() == input.casefold():
                candy_list.remove(candy)
                print(input + ' removed!')
    else:
        print(input + ' is not in the list! Nothing removed.')


def main():
    # display inital list
    display_candy_list()

    while True:
        # Always display the menu
        user_options_menu()

        try:
            user_input = int(input('CHOICE: '))

            # check if the option is in the dict
            if user_input not in user_options.keys():
                print('Invalid Option. Try again.')
            if user_input == 1:
                user_add_input = input('Enter a candy to add: ')
                add(user_add_input)
            if user_input == 2:
                user_remove_input = input('Enter a candy to remove: ')
                remove(user_remove_input)
            if user_input == 3:
                display_candy_list()
            if user_input == 4:
                print('Goodbye!')
                break
        except:
            print('Must be a number. Try again.')


if __name__ == '__main__':
    # call main on init
    main()
