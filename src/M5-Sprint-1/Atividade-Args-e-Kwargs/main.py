def sum_numbers(*args):
    sum = 0
    for number in args:
        sum += number

    return sum


numbers = [1, 2, 3, 4, 5, 6]

result = sum_numbers(*numbers)
# print(result)


def get_multiplied_amount(multiplier, *args):
    sum = 0
    for number in args:
        sum += number

    result = sum * multiplier

    return result


numbers = [1, 2, 3]
multiplier = 2

result = get_multiplied_amount(multiplier, *numbers)
# print(result)


def word_concatenator(*args):
    return " ".join(args)


words = ["Tá", "pegando", "fogo", "bicho!!!"]
concatenated_words = word_concatenator(*words)
# print(concatenated_words)


def inverted_word_factory(*args):
    return " ".join(args)[::-1]


words = ["eae", "amigão", "belezinha?"]

inverted_words = inverted_word_factory(*words)
# print(inverted_words)


def dictionary_separator(**kwargs):
    return (
        list(kwargs.keys()),
        list(kwargs.values()),
    )


user = {"name": "Naruto", "age": 16, "favorite word": "Ichiraku Ramen"}

items = dictionary_separator(**user)
# print(type(items))
# # print(items[0])
# print(items[1])
# print(items)


def dictionary_creator(*args, **kwargs):
    if len(args) < len(kwargs):
        return None

    output_dict = {}
    for index, value in enumerate(kwargs.values()):
        new_key = args[index]
        new_value = value
        output_dict[new_key] = new_value

    return output_dict


change_keys = ["username", "password",
               "address"]

user = {"name": "Williams", "some_key": "1234"}

modified_user = dictionary_creator(*change_keys, **user)
# print(modified_user)


def purchase_logger(**kwargs):
    return f"""
    {kwargs["quantity"]} {kwargs["name"]} bought by {kwargs["price"]}
    """


purchase = {"name": "washing powder", "price": 6.7, "quantity": 4}

purchase_log = purchase_logger(**purchase)
# print(purchase_log)


def world_cup_logger(country, *args):
    sorted_str_list = []

    for arg in sorted(args):
        sorted_str_list.append(str(arg))

    formatted_str = ", ".join(sorted_str_list)

    reverse_split = formatted_str.rsplit(", ", 1)

    return country + " - " + " e ".join(reverse_split)


country = 'Alemanha'
year_list = [2014, 1990, 1974, 1954]

log = world_cup_logger(country, *year_list)
# print(log)
