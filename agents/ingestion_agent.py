import pandas as pd
import os
from graph.state import ClimateState

def ingestion_node(state: ClimateState) -> ClimateState:
    
    # Get project root directory dynamically
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_path = os.path.join(project_root, "data", "emdat_raw.csv")
    
    print("Loading data from:", data_path)  # Debug line
    
    df = pd.read_csv(data_path, encoding="latin-1")
    
    # Filter disaster type
    df = df[df["Disaster Type"] == state["disaster_type"]]
    
    # Filter region
    df = df[df["Subregion"] == state["region"]]
    
    state["raw_data"] = df
    
    return state