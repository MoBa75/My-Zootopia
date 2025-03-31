import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, 'r', encoding='utf-8') as handle:
        return json.load(handle)


def get_animals_info(data):
    animals_lst = []
    for animal in data:
        animals_info = {}
        for key, val in animal.items():
            if key == "name":
                animals_info["Name"] = val
            if key == "locations":
                animals_info["Locations"] = val[0]
            if key == "characteristics":
                if val.get("diet", None):
                    animals_info["Diet"] = val["diet"]
                if val.get("type", None):
                    animals_info["Type"] = val["type"]
        animals_lst.append(animals_info)
    return animals_lst


def conect_animal_info(data):
    complete_animals_info = ''
    for animal in data:
        if "Name" in animal:
            for key, val in animal.items():
                complete_animals_info += f"{key}: {val}\n"
        complete_animals_info += "\n"
    return complete_animals_info

def read_html_file(html_data):
    with open(html_data, 'r', encoding='utf-8') as file:
        return file.read()

def chance_html_content(html_content, str_input):
    return html_content.replace('__REPLACE_ANIMALS_INFO__', str_input)


def write_html_file(new_text):
    with open('animals.html', 'w') as file:
        file.write(new_text)


animals_data = load_data('animals_data.json')
info_lst = get_animals_info(animals_data)
animal_str = conect_animal_info(info_lst)
html_data = read_html_file('animals_template.html')
chanced_html = chance_html_content(html_data, animal_str)
write_html_file(chanced_html)



