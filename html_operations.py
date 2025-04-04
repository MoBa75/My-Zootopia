
def add_space_before_uppercase(word):
    """
    Inserts a space before each capital letter of the transmitted
    word, thereby dividing the word into several words
    :param word: A word that consists of several words
                 joined together as a string
    :return: multiple word as string
    """
    new_word = ""
    for letter in word:
        if letter.isupper():
            new_word += " "
        new_word += letter
    return new_word[1:]


def serialize_animal(animal, infos):
    """
    Creates the html text for later use according
    to the previous selection criteria
    :param animal: corresponding animal according
                   to the selected criteria as string
    :param infos:  corresponding information about the animal
                   according to the selected criteria as string
    :return: All necessary content in html form as string
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
    Gets all contents of the html file for further use
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
    regenerated html content as string
    :param new_text: regenerated html content as string
    """
    with open('animals.html', 'w') as file:
        file.write(new_text)
