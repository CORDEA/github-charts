import datetime
from collections import OrderedDict
from typing import List, Set, Dict, Iterator

import requests

import plotter
from contribution import Contribution
from html_parser import ContributionHTMLParser


def __group(mapped: Iterator[Contribution]) -> Dict[datetime.date, int]:
    grouped = OrderedDict()
    for cont in mapped:
        if cont.date in grouped:
            grouped[cont.date] += cont.commits
        else:
            grouped[cont.date] = cont.commits
    return grouped


def __group_by_month(conts: Set[Contribution]) -> Dict[datetime.date, int]:
    mapped = map(lambda c: Contribution(datetime.date(c.date.year, c.date.month, 1), c.commits), conts)
    return __group(mapped)


def __group_by_year(conts: Set[Contribution]) -> Dict[datetime.date, int]:
    mapped = map(lambda c: Contribution(datetime.date(c.date.year, 1, 1), c.commits), conts)
    return __group(mapped)


def __fetch(date: str) -> List[Contribution]:
    response = requests.get('https://github.com/users/CORDEA/contributions?to=' + date)
    body = response.text
    parser = ContributionHTMLParser()
    parser.feed(body)
    return parser.contributions


def __fetch_all() -> Set[Contribution]:
    conts = []
    for i in range(5, 10):
        conts.extend(__fetch('201' + str(i) + '-01-01'))
    return set(conts)


if __name__ == '__main__':
    conts = __fetch_all()
    gr = __group_by_year(conts)
    # plotter.draw_heatmap(gr)
    plotter.draw_line(gr)
