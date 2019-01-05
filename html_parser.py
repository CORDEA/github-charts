from datetime import datetime
from html.parser import HTMLParser
from typing import List

from contribution import Contribution


class ContributionHTMLParser(HTMLParser):
    contributions: List[Contribution]

    def __init__(self):
        super().__init__()
        self.contributions = []

    def handle_starttag(self, tag, attrs):
        if tag == 'rect':
            dic = dict(attrs)
            self.contributions.append(
                Contribution(datetime.strptime(dic['data-date'], "%Y-%m-%d"), int(dic['data-count'])))
