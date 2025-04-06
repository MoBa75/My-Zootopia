import json
import html_operations as op


def load_data(file_path):
    """
    Loads all data entries from the JSON file.
    :param file_path:
    :return: data entries as dictionary
    """
    with open(file_path, 'r', encoding='utf-8') as handle:
        return json.load(handle)


def get_animals_info(animals_data):
    """
    Extract the desired data entries from the overall database.
    :param animals_data: overall database as dictionary
    :return: desired data as dictionary
    """
    # extrahiert Tier Daten aus den Gesamtdaten
    animal_info = {}
    for animal in animals_data:
        for category, detail in animal.items():
            if category == "name":
                animal_info[detail] = {}
                name = detail
            if category == "locations":
                animal_info[name]["Locations"] = detail[0]
            if category == "characteristics":
                if detail.get("diet", None):
                    animal_info[name]["Diet"] = detail["diet"]
                if detail.get("type", None):
                    animal_info[name]["Type"] = detail["type"]
                if detail.get("color", None):
                    animal_info[name]["Color"] = detail["color"]
                if detail.get("skin_type", None):
                    animal_info[name]["Skin Type"] = detail["skin_type"]
    return animal_info


def connect_animal_info(animal_info, user_input):
    """
    Selects corresponding data entries according to user
    selection and creates the data for later output
    :param animal_info: animal database as dictionary
    :param user_input: corresponding selection of the user as string
    :return: complete data set of the animals to
             be displayed in html form as a string
    """
    # Filter und Auswahl des User wird hier erstellt.
    complete_animals_info = ''
    for animal, infos in animal_info.items():
        if user_input.capitalize() in infos.get("Skin Type", "") or user_input in 'all':
            complete_animals_info += op.serialize_animal(animal, infos)
    # corrects the formatting error happening for ' symbol
    return complete_animals_info.replace("’", "'")


def get_skin_types(animal_info):
    """
    Extracts all skin types from the database.
    :param animal_info: database with animal info as dictionary
    :return: all skin types as list
    """
    skin_types = []
    for animal, characteristics in animal_info.items():
        if characteristics['Skin Type'] in skin_types:
            continue
        skin_types.append(characteristics['Skin Type'])
    return skin_types


def get_user_input(skin_types):
    """
    User query whether database should be filtered by
    skin type and selection of skin type
    :param skin_types: for selection by user as list
    :return: user selection as string
    """
    print("Would you like to filter the animals by their skin type? ")
    while True:
        user_input = input("Please enter 'y' for yes or 'n' for no: ")
        if user_input.lower() == 'n':
            return 'all'
        if user_input.lower() == 'y':
            print('Which skin type do you want to choose?')
            while True:
                user_input = input(f'Please enter one of these skin types: '
                                   f'"{", ".join(skin_types)}": ')
                if user_input.capitalize() in skin_types:
                    return user_input
                print(f"ERROR! '{user_input}' is not a valid skin type!")
        print(f"ERROR! '{user_input}' is not a valid answer!")


def main():
    """Calls all necessary functions and transfers
    the necessary data to execute the program. """
    animals_data = load_data('animals_data.json')
    animal_info = get_animals_info(animals_data)
    skin_types = get_skin_types(animal_info)
    user_input = get_user_input(skin_types)
    animal_str = connect_animal_info(animal_info, user_input)
    html_data = op.read_html_file('animals_template.html')
    chanced_html = op.chance_html_content(html_data, animal_str)
    op.write_html_file(chanced_html)


if __name__ == "__main__":
    main()
