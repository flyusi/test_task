import string
import json


def build_inverted_index(text: str) -> list:
    inverted_index = {}

    for line_number, line in enumerate(text.split('\n')):

        for word_position, word in enumerate(line.split()):
            word = word.lower().rstrip(string.punctuation)

            if word not in inverted_index.keys():
                inverted_index[word] = [(line_number, word_position)]

            else:
                inverted_index[word].append((line_number, word_position))

    list_of_dicts = [
        {word: indexes} for word, indexes in inverted_index.items()
    ]

    return list_of_dicts


def search_word(list_of_dicts: list, line_number: int, word_position: int) -> str:
    coordinates = (line_number, word_position)

    for elem in list_of_dicts:
        for word, coordinates_list in elem.items():
            if coordinates in coordinates_list:

                return word


def main():
    list_of_dicts = build_inverted_index(some_text)
    print('Инвертированный индекс по стихотворению "Чепушники"'
          ' Сергея Михалкова построен.')

    if input('Записать данные в файл? Если да - введите "y", '
             'иначе - вывод в консоль').lower() == 'y':

        with open('inverted_index.json', 'w') as file:
            json.dump(
                list_of_dicts,
                file,
                indent=4,
                sort_keys=True,
                ensure_ascii=False
            )

    else:
        print(json.dumps(
            list_of_dicts,
            indent=4,
            sort_keys=True,
            ensure_ascii=False
        ))

    while input('Пробуем поиск?) Если да - введите "y"').lower() == 'y':
        try:
            line_number, word_position = map(int, (input(
                'Введите номер строки и номер позиции слова через пробел:'
            ).split()))

        except TypeError:
            print('Необходимо ввести 2 числовых значения')
            continue

        except Exception:
            print('Что-то пошло не так... '
                  'необходимо ввести 2 числовых значения')
            continue

        word = search_word(list_of_dicts, line_number, word_position)
        if not word:
            print('Слова с таким индексом не найдено')
        else:
            print(word)

    else:
        print('Ок, мы закончили)')


some_text = '''На одной лесной опушке
Жили-были круглый год:
Две старушки,
Две кукушки
И глухой безухий кот.
Две старушки вышивали,
Две кукушки куковали,
Кот сибирский, без ушей,
Полевых ловил мышей.
'''


if __name__ == '__main__':
    main()
