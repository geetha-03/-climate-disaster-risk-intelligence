from graph.state import ClimateState

def risk_node(state: ClimateState) -> ClimateState:
    
    slope = state["trend_slope"]
    p_value = state["p_value"]
    mk_trend = state["mk_trend"]
    mk_p = state["mk_p_value"]
    t_p = state["t_p_value"]
    
    # Strong evidence case
    if slope > 0 and p_value < 0.05 and mk_trend == "increasing" and mk_p < 0.05:
        risk = "High"
    
    # Moderate evidence
    elif slope > 0 and mk_trend == "increasing":
        risk = "Moderate"
    
    # Decreasing trend
    elif slope < 0 and mk_trend == "decreasing":
        risk = "Decreasing"
    
    else:
        risk = "Stable or Uncertain"
    
    state["risk_level"] = risk

    # T-test
    if mk_p is not None and mk_p < 0.01:
        confidence = "High"
    elif mk_p is not None and mk_p < 0.05:
        confidence = "Moderate"
    else:
        confidence = "Low"

    # Boost confidence if t-test also significant
    if t_p is not None and t_p < 0.05 and confidence != "High":
        confidence = "High"

    state["confidence_level"] = confidence
    
    return state