# Alexander Spurlock

# menu
menu = {
    1: {'item_name': 'Burger', 'price': '$200'},
    2: {'item_name': 'Fries', 'price': '$150'},
    3: {'item_name': 'Coke', 'price': '$100'}
}


def display_menu():
    """
    Display the menu dictionary in a pretty way.
    """
    print("\n-- MENU --\n")
    for obj in menu:
        print(obj, ' - ', menu[obj]['item_name'])
    print('\n-- MENU --\n')


def get_price(menu_item_number):
    """
    Return the price of a given menu item number.
    """
    if menu_item_number in menu:
        item = menu[menu_item_number]
        return item.get('price')
    return None


def read_user_input():
    """
    Read user's input.
    """
    is_done = False
    while is_done is False:
        try:
            user_choice = int(
                input(
                    'Enter a menu item (as a number), or 0 if you\'re done. \n'
                    'So, what\'s it going to be?: '
                )
            )
            if user_choice != 0:
                item_price = get_price(user_choice)
                if item_price is not None:
                    print(item_price)
                else:
                    print('That\'s not an item on OUR list.')
            else:
                print('Thank you. Come again.')
                is_done = True
        except:
            print('Please enter a valid item number.')


def main():
    display_menu()
    read_user_input()


if __name__ == "__main__":
    main()
