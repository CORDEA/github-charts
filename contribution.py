import datetime
from dataclasses import dataclass


@dataclass
class Contribution:
    date: datetime.date
    commits: int
