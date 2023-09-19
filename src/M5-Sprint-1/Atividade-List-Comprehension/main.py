def list_comprehension_exercise_1():
    return [number for number in range(11)]


# print(list_comprehension_exercise_1())

def list_comprehension_exercise_2():
    return [
        number for number in range(22)
        if number % 2 == 0 or number % 3 == 0
    ]


# print(list_comprehension_exercise_2())


def list_comprehension_exercise_3():
    return [
        number
        for number in range(-5, 32)
        if not number % 2 == 0 and not number % 5 == 0
    ]


# print(list_comprehension_exercise_3())


def list_comprehension_exercise_4():
    return [number ** 2 for number in range(11)]


# print(list_comprehension_exercise_4())


def list_comprehension_exercise_5(sentence):
    return [letter for letter in sentence if letter.isupper()]


sentence = 'O Rato Rui Gosta De QueiJo FresQuiNho'
# print(list_comprehension_exercise_5(sentence))


def list_comprehension_exercise_6(sentence):
    return [
        word
        for word in sentence.split()
        if len(word) >= 4 and word[0] == "r"
    ]


sentence = 'o rato rui roeu a roupa do rei de roma'
print(list_comprehension_exercise_6(sentence))
