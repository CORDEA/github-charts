from typing import List

import requests

from contribution import Contribution
from html_parser import ContributionHTMLParser


def fetch() -> List[Contribution]:
    response = requests.get('https://github.com/users/CORDEA/contributions')
    body = response.text
    parser = ContributionHTMLParser()
    parser.feed(body)
    return parser.contributions


if __name__ == '__main__':
    print(fetch())
