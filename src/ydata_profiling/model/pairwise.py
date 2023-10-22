from typing import Any, List, Tuple

import pandas as pd

from ydata_profiling.config import Settings
from ydata_profiling.visualisation.plot import scatter_pairwise


def get_scatter_tasks(
    config: Settings, continuous_variables: list
) -> List[Tuple[Any, Any]]:
    if not config.interactions.continuous:
        return []

    targets = config.interactions.targets
    if len(targets) == 0:
        targets = continuous_variables

    tasks = [(x, y) for y in continuous_variables for x in targets]
    return tasks


def get_scatter_plot(
    config: Settings, df: pd.DataFrame, x: Any, y: Any, continuous_variables: list
) -> str:
    if x in continuous_variables:
        if y == x:
            df_temp = df[[x]].dropna()
        else:
            df_temp = df[[x, y]].dropna()
        return scatter_pairwise(config, df_temp[x], df_temp[y], x, y)
    else:
        return ""


def get_spatio_plot(config: Settings, df: pd.DataFrame, x: Any, y: Any) -> str:
    if config.vars.spatio.active:
        df_temp = df[[x, y]].dropna()
        return scatter_pairwise(config, df_temp[x], df_temp[y], x, y)
    else:
        return ""
