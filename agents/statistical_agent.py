import numpy as np
from scipy import stats
import pymannkendall as mk
from graph.state import ClimateState

def statistical_node(state: ClimateState) -> ClimateState:
    
    df = state["yearly_counts"]
    
    x = df["Start Year"].values
    y = df["event_count"].values
    
    # ----- Linear Regression -----
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    
    state["trend_slope"] = slope
    state["p_value"] = p_value

    # ----- Mann-Kendall Test -----
    mk_result = mk.original_test(y)
    
    state["mk_trend"] = mk_result.trend
    state["mk_p_value"] = mk_result.p
    
    return state

