from typing import List, Set

import requests

from contribution import Contribution
from html_parser import ContributionHTMLParser


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
    __fetch_all()
