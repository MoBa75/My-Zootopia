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
                animals_info[key] = val
            if key == "locations":
                animals_info[key] = val[0]
            if key == "characteristics":
                if val.get("diet", None):
                    animals_info["diet"] = val["diet"]
                if val.get("type", None):
                    animals_info["type"] = val["type"]
        animals_lst.append(animals_info)
    return animals_lst


def print_animal_info(data):
    for animal in data:
        if not "type" in animal:
            print(f"Name: {animal["name"]} "
                f"\nDiet: {animal["diet"]} "
                f"\nLocation: {animal["locations"]}\n")
        else:
            print(f"Name: {animal["name"]} "
                f"\nDiet: {animal["diet"]} "
                f"\nLocation: {animal["locations"]} "
                f"\nType: {animal["type"]}\n")


animals_data = load_data('animals_data.json')
info_lst = get_animals_info(animals_data)
print_animal_info(info_lst)


