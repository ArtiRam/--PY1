def get_count_char(str_):
    str_ = str_.lower()

    dictionary = {}

    for symbol in str_:
        if symbol.isalpha():
            dictionary.update({symbol: str_.count(symbol)})

    return dictionary


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))


def delete(list_, index=None):

    if index is None:
        index = len(list_) - 1

    del list_[index]
    return list_


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
