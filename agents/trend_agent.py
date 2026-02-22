import pandas as pd
from graph.state import ClimateState

def trend_node(state: ClimateState) -> ClimateState:
    
    df = state["raw_data"]
    
    # Count number of disasters per year
    yearly_counts = (
        df.groupby("Start Year")
        .size()
        .reset_index(name="event_count")
        .sort_values("Start Year")
    )
    
    state["yearly_counts"] = yearly_counts
    
    return state