from graph.state import ClimateState
from llm.groq_llm import get_llm

def interpretation_node(state: ClimateState) -> ClimateState:
    
    llm = get_llm()
    
    slope = state["trend_slope"]
    p_value = state["p_value"]
    region = state["region"]
    disaster = state["disaster_type"]
    risk = state["risk_level"]
    reflection = state["reflection_notes"]
    plot_figure = state["plot_figure"]
    t_p = state["t_p_value"]
    confidence = state["confidence_level"]
    
    prompt = f"""You are a climate risk analyst preparing an executive assessment.

            Disaster Type: {disaster}
            Region: {region}

            Linear Regression P-value: {p_value}
            Mann-Kendall Trend: {state["mk_trend"]}
            Mann-Kendall P-value: {state["mk_p_value"]}
            T-Test P-value: {t_p}

            Assigned Risk Level: {risk}
            Confidence Level: {confidence}

            Interpret all statistical results together.

            Guidelines:
            - If T-test p-value > 0.05, explain that there is no strong evidence of an abrupt structural mean shift between early and recent periods. 
                Clarify that this does NOT contradict a gradual monotonic trend detected by Mann-Kendall.
                Avoid stating that the trend may be random if MK p-value is strongly significant (< 0.01).
            - Avoid repeating raw numbers excessively.
            - Provide concise executive-style summary.
            """
    
    response = llm.invoke(prompt)
    
    state["interpretation"] = response.content
    
    return state