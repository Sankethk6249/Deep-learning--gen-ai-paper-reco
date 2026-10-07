from typing import List

import altair as alt
import numpy as np

from labml import analytics
from labml.analytics import IndicatorCollection


def calculate_percentages(means: List[np.ndarray], names: List[List[str]]):
    normalized = []

    for i in range(len(means)):
        total = np.zeros_like(means[i])
        for j, n in enumerate(names):
            if n[-1][:-1] == names[i][-1][:-1]:
                total += means[j]
        normalized.append(means[i] / (total + np.finfo(float).eps))

    return normalized


def plot_infosets(indicators: IndicatorCollection, *,
                  is_normalize: bool = True,
                  width: int = 600,