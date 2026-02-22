from graph.state import ClimateState
from llm.groq_llm import get_llm

def reflection_node(state: ClimateState) -> ClimateState:
    
    llm = get_llm()
    
    slope = state["trend_slope"]
    p_value = state["p_value"]
    mk_trend = state["mk_trend"]
    mk_p = state["mk_p_value"]
    t_p = state["t_p_value"]
    yearly_data = state["yearly_counts"]
    
    sample_size = len(yearly_data)
    
    prompt = f"""
You are a statistical auditor reviewing climate disaster trend analysis.

Linear Regression:
Slope: {slope}
P-value: {p_value}

Mann-Kendall Test:
Trend: {mk_trend}
P-value: {mk_p}

Mean Shift T-Test:
P-value: {t_p}

Sample size: {sample_size} years

Evaluate:

1. Do all statistical methods agree?
2. Is trend evidence strong, moderate, or weak?
3. Does the T-test support or weaken the trend conclusion?
4. Are there stability concerns?

Guidelines:
- If T-test p-value > 0.05, note that mean shift is not statistically significant.
- Keep analysis concise and balanced.
"""
    
    response = llm.invoke(prompt)
    
    state["reflection_notes"] = response.content
    
    return state