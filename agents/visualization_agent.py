import matplotlib.pyplot as plt
import numpy as np
from graph.state import ClimateState

def visualization_node(state: ClimateState) -> ClimateState:

    df = state["yearly_counts"]

    x = df["Start Year"].values
    y = df["event_count"].values

    slope = state["trend_slope"]
    intercept = np.mean(y) - slope * np.mean(x)
    regression_line = slope * x + intercept

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x, y, marker="o", label="Observed")
    ax.plot(x, regression_line, linestyle="--", label="Trend")

    ax.set_title(f"{state['disaster_type']} Frequency in {state['region']}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Events")
    ax.legend()

    fig.tight_layout()

    state["plot_figure"] = fig

    return state