from scipy.stats import ttest_ind
from graph.state import ClimateState
import numpy as np

def mean_shift_node(state: ClimateState) -> ClimateState:

    df = state["yearly_counts"]

    years = df["Start Year"].values
    counts = df["event_count"].values

    median_year = np.median(years)

    early = counts[years <= median_year]
    recent = counts[years > median_year]

    if len(early) > 1 and len(recent) > 1:
        t_stat, p_value = ttest_ind(early, recent, equal_var=False)
        state["t_stat"] = t_stat
        state["t_p_value"] = p_value
    else:
        state["t_stat"] = None
        state["t_p_value"] = None

    return state