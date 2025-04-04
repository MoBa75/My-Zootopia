
def add_space_before_uppercase(word):
    new_word = ""
    for letter in word:
        if letter.isupper():
            new_word += " "
        new_word += letter
    return new_word[1:]


def serialize_animal(animal, infos):
    complete_animals_info = (f'<li class="cards__item">'
                             f'\n  <div class="card__title">{animal}</div>'
                             f'\n<div class="card__text">'
                             f' \n<ul>')
    for category, detail in infos.items():
        if category == "Color":
            complete_animals_info += (f"<li><strong>{category.capitalize()}</strong>: "
                                      f"{add_space_before_uppercase(detail)}</li>\n")
        else:
            complete_animals_info += (f"<li><strong>{category.capitalize()}"
                                      f"</strong>: {detail}</li>\n")
    complete_animals_info += "  </ul>\n </div>\n</li>\n"
    return complete_animals_info


def read_html_file(html_data):
    with open(html_data, 'r', encoding='utf-8') as file:
        return file.read()


def chance_html_content(html_content, str_input):
    return html_content.replace('__REPLACE_ANIMALS_INFO__', str_input)


def write_html_file(new_text):
    with open('animals.html', 'w') as file:
        file.write(new_text)
