from langgraph.graph import StateGraph, END
from graph.state import ClimateState

from agents.ingestion_agent import ingestion_node
from agents.trend_agent import trend_node
from agents.statistical_agent import statistical_node
from agents.interpretation_agent import interpretation_node
from agents.risk_agent import risk_node
from agents.reflection_agent import reflection_node
from agents.visualization_agent import visualization_node
from agents.mean_shift_agent import mean_shift_node


def build_graph():
    
    builder = StateGraph(ClimateState)
    
    builder.add_node("ingestion", ingestion_node)
    builder.add_node("trend", trend_node)
    builder.add_node("statistics", statistical_node)
    builder.add_node("interpretation", interpretation_node)
    builder.add_node("risk", risk_node)
    builder.add_node("reflection", reflection_node)
    builder.add_node("visualization", visualization_node)
    builder.add_node("mean_shift", mean_shift_node)
    
    builder.set_entry_point("ingestion")
    
    builder.add_edge("ingestion", "trend")
    builder.add_edge("trend", "statistics")
    # builder.add_edge("statistics", "interpretation")
    builder.add_edge("interpretation", END)
    
    # builder.add_edge("statistics", "risk")
    # builder.add_edge("risk", "interpretation")

    builder.add_edge("risk", "reflection")
    builder.add_edge("reflection", "interpretation")

    # builder.add_edge("statistics", "visualization")
    builder.add_edge("visualization", "risk")

    builder.add_edge("statistics", "mean_shift")
    builder.add_edge("mean_shift", "visualization")
    
    return builder.compile()