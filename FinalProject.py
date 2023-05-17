import pandas
from pandas import DataFrame

hero_network_file_path = 'marvel/hero-network.csv'
edges_file_path = 'marvel/edges.csv'
nodes_file_path = 'marvel/nodes.csv'

node_options: dict[int, str] = {
    1: 'Search for hero\'s network of heros and villians.',
    2: 'Search for hero\'s comic book appearance.',
    3: 'To exit!'
}

def read_csv(file_path: str) -> DataFrame: 
    return pandas.read_csv(file_path)


def user_type_options_menu():
    """
    Display the menu dictionary in a pretty way.
    """
    print("\n-- MENU --")
    for obj in node_options:
        print(obj, ' - ', node_options[obj])


def search_hero_comic_appearance(hero: str):
    df = read_csv(edges_file_path)
    print(df[df['hero'].str.contains(hero, case=False)])


def search_heros_network(hero: str):
    df = read_csv(hero_network_file_path)
    print(df[df['hero1'].str.contains(hero, case=False)])


def main():
    print('Welcome to the Marvel universe comic book/hero/villian search!')

    while True:
        user_type_options_menu()
        user_type_choice = int(input('Pick: '))

        if user_type_choice == 1:
            user_input = input('Hero name: ')
            search_heros_network(user_input)
        if user_type_choice == 2:
            user_input = input('Hero name: ')
            search_hero_comic_appearance(user_input)
        if user_type_choice == 3:
            print('Goodbye!')
            break
    

if __name__ == '__main__':
    main()