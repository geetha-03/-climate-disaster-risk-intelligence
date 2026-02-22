from graph.climate_graph import build_graph

def run_analysis(region: str, disaster_type: str):

    graph = build_graph()

    initial_state = {
        "query": f"Are {disaster_type}s increasing in {region}?",
        "region": region,
        "disaster_type": disaster_type,
        "raw_data": None,
        "yearly_counts": None,
        "trend_slope": None,
        "p_value": None,
        "mk_trend": None,
        "mk_p_value": None,
        "risk_level": None,
        "reflection_notes": None,
        "plot_figure": None,
        "interpretation": None
    }

    result = graph.invoke(initial_state)

    return result