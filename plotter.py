import datetime
from typing import Dict

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


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
