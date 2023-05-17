# Alexander Spurlock
# 10/29/2022
# Lab 8: Read/Write files

user_options = {
    1: 'Add',
    2: 'Display',
    3: 'Exit'
}

def main():
    file_path = './Books.txt'
    display_file(file_path)

    while True:
        # Always display the menu
        user_options_menu()
        
        try:
            user_input = int(input('CHOICE: '))

            # check if the option is in the dict
            if user_input not in user_options.keys():
                print('Invalid Option. Try again.')

            if user_input == 1:
                user_add_input = input('Enter a book to add: ')
                write_file(file_path=file_path, data=user_add_input)

            if user_input == 2:
                display_file(file_path=file_path)

            if user_input == 3:
                print('Goodbye!')
                break
            
        except:
            print('Must be a number. Try again.')


def display_file(file_path):
    """
    Display the book list in a pretty way.
    """

    print("\n-- BOOK LIST --")
    counter = 0
    open_file = open(file_path)
    for line in open_file:
        counter += 1
        print(counter, '. ', line)

    open_file.close()


def user_options_menu():
    """
    Display the menu dictionary in a pretty way.
    """
    print("\n-- MENU --")
    for obj in user_options:
        print(obj, ' - ', user_options[obj])
    print('\nWould you like to add (1), re-list (2), or exit (3)?: ')


def write_file(file_path, data):
    """
    Write to file given path to it and the data to write.
    """
    open_file = open(file_path, 'a+')
    open_file.write(data + '\n')
    open_file.close()


if __name__ == '__main__':
    main()