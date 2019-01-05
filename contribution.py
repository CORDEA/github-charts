import datetime


class Contribution:
    date: datetime.date
    commits: int

    def __init__(self, date, commits):
        self.date = date
        self.commits = commits

    def __hash__(self):
        return hash(self.date)

    def __eq__(self, other):
        return self.date == other.date
