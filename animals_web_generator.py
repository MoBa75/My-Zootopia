import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, 'r', encoding='utf-8') as handle:
        return json.load(handle)


def get_animals_info(data):
    animals_lst = {}
    for animal in data:
        for key, val in animal.items():
            if key == "name":
                animals_lst[val] = {}
                name = val
            if key == "locations":
                animals_lst[name]["Locations"] = val[0]
            if key == "characteristics":
                if val.get("diet", None):
                    animals_lst[name]["Diet"] = val["diet"]
                if val.get("type", None):
                    animals_lst[name]["Type"] = val["type"]
                if val.get("color", None):
                    animals_lst[name]["Color"] = val["color"]
                if val.get("skin_type", None):
                    animals_lst[name]["Skin Type"] = val["skin_type"]
    return animals_lst


def add_space_before_uppercase(word):
    new_val = ""
    for letter in word:
        if letter.isupper() and letter != word[0]:
            new_val += " "
        new_val += letter
    return new_val


def serialize_animal(animal, infos):
    complete_animals_info = (f'<li class="cards__item">'
                              f'\n  <div class="card__title">{animal}</div>'
                              f'\n<p class="card__text">\n')
    for key, val in infos.items():
        if key == "Color":
            complete_animals_info += (f"<strong>{key.capitalize()}</strong>: "
                                      f"{add_space_before_uppercase(val)}<br/>\n")
        else:
            complete_animals_info += f"<strong>{key.capitalize()}</strong>: {val}<br/>\n"
    complete_animals_info += " </p>\n</li>\n"
    return complete_animals_info


def connect_animal_info(data):
    complete_animals_info = ''
    for animal, infos in data.items():
        complete_animals_info += serialize_animal(animal, infos)
    # corrects the formatting error happening for ' symbol
    return complete_animals_info.replace("’", "'")


def read_html_file(html_data):
    with open(html_data, 'r', encoding='utf-8') as file:
        return file.read()


def chance_html_content(html_content, str_input):
    return html_content.replace('__REPLACE_ANIMALS_INFO__', str_input)


def write_html_file(new_text):
    with open('animals.html', 'w') as file:
        file.write(new_text)


def main():
    animals_data = load_data('animals_data.json')
    info_lst = get_animals_info(animals_data)
    print(info_lst)
    animal_str = connect_animal_info(info_lst)
    html_data = read_html_file('animals_template.html')
    chanced_html = chance_html_content(html_data, animal_str)
    write_html_file(chanced_html)


if __name__ == "__main__":
    main()

