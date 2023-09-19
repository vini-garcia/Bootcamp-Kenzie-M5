from datetime import datetime
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


def data_processing(dict_soccer_team: dict):
    if dict_soccer_team["titles"] < 0:
        raise NegativeTitlesError()

    first_cup = int(dict_soccer_team["first_cup"][:4])

    if first_cup < 1930 or (first_cup - 1930) % 4 != 0:
        raise InvalidYearCupError()

    possible_titles = (datetime.now().year - first_cup) // 4

    if dict_soccer_team["titles"] > possible_titles:
        raise ImpossibleTitlesError()
