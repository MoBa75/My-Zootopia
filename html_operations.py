def add_space_before_uppercase(word):
    """
    Separates coherent words of an entry with spaces.
    :param word: dictionary entry as string
    :return: separated words as string
    """
    new_word = ""
    for letter in word:
        if letter.isupper():
            new_word += " "
        new_word += letter
    return new_word[1:]


def serialize_animal(animal, infos):
    """
    Creates the html text for a given animal dictionary entry
    :param animal: animal name as string
    :param infos:  animal information as string
    :return: content in html form as string
    """
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
    """
    Reads a html file
    :param html_data: html file
    :return: complete content of the html file as string
    """
    with open(html_data, 'r', encoding='utf-8') as file:
        return file.read()


def chance_html_content(html_content, str_input):
    """
    Replaces the corresponding section with the newly created html text.
    :param html_content: Content of the html file as string
    :param str_input: The html text to be inserted as string
    :return: regenerated html content as string
    """
    return html_content.replace('__REPLACE_ANIMALS_INFO__', str_input)


def write_html_file(new_text):
    """
    Writs a string to a html file
    :param new_text: regenerated html content as string
    """
    with open('animals.html', 'w') as file:
        file.write(new_text)
