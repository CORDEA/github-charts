import datetime
from typing import Dict, Set

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from contribution import Contribution


def draw_line(data: Dict[datetime.date, int]):
    sns.set()
    items = dict([(k.year, v) for k, v in data.items()])
    f, ax = plt.subplots()
    sns.barplot(x=list(items.keys()), y=list(items.values()), ax=ax)
    plt.show()


def draw_heatmap(data: Dict[datetime.date, int]):
    sns.set()
    items = []
    for (k, v) in data.items():
        items.append((k.year, k.month, v))
    d = pd.DataFrame(items, columns=['year', 'month', 'commits'])
    frame = d.pivot('month', 'year', 'commits')
    frame.fillna(0, inplace=True)
    frame = frame.astype(np.int64)
    f, ax = plt.subplots()
    sns.heatmap(frame, annot=True, fmt='d', linewidths=.5, ax=ax)
    plt.show()


def draw_stripplot(data: Set[Contribution]):
    sns.set()
    items = []
    for c in data:
        items.append((c.date.year, c.date.month, c.date.day, c.commits))
    data = pd.DataFrame(items, columns=['year', 'month', 'day', 'commits'])
    _, ax = plt.subplots()
    sns.stripplot(x='year', y='commits', data=data, jitter=True, alpha=.15, zorder=1, ax=ax)
    plot = sns.pointplot(
        x='year', y='commits', data=data, palette='dark', markers='d', scale=.75, join=False, ci=None, ax=ax)
    plot.get_figure().savefig('stripplot.png')
