import json
import html_operations as op


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, 'r', encoding='utf-8') as handle:
        return json.load(handle)


def get_animals_info(animals_data):
    animals_lst = {}
    for animal in animals_data:
        for category, detail in animal.items():
            if category == "name":
                animals_lst[detail] = {}
                name = detail
            if category == "locations":
                animals_lst[name]["Locations"] = detail[0]
            if category == "characteristics":
                if detail.get("diet", None):
                    animals_lst[name]["Diet"] = detail["diet"]
                if detail.get("type", None):
                    animals_lst[name]["Type"] = detail["type"]
                if detail.get("color", None):
                    animals_lst[name]["Color"] = detail["color"]
                if detail.get("skin_type", None):
                    animals_lst[name]["Skin Type"] = detail["skin_type"]
    return animals_lst


def connect_animal_info(animal_info, user_input):
    complete_animals_info = ''
    for animal, infos in animal_info.items():
        if user_input.capitalize() in infos.get("Skin Type", "") or user_input in 'all':
            complete_animals_info += op.serialize_animal(animal, infos)
    # corrects the formatting error happening for ' symbol
    return complete_animals_info.replace("’", "'")


def get_skin_types(animal_info):
    skin_types = []
    for animal, characteristics in animal_info.items():
        if characteristics['Skin Type'] in skin_types:
            continue
        skin_types.append(characteristics['Skin Type'])
    return skin_types


def get_user_input(skin_types):
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
                print("ERROR")
        print("ERROR")


def main():
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
